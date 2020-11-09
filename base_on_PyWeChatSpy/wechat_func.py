# PyWeChatSpy is cloned from https://github.com/veikai/PyWeChatSpy
# 该项目文件夹clone后放在了base_on_PyWeChatSpy下
from PyWeChatSpy.PyWeChatSpy import WeChatSpy
from PyWeChatSpy.PyWeChatSpy.command import *
# from lxml import etree
# import logging

import re
# import time
import random
from threading import Thread
from urllib.parse import quote

# project内
from data.message import send_mail
from util.func_apscheduler import do_at_sometime
# from util.basic_functions import read_file2list
# from util.week import *
from util.csv2excel import csv_to_xlsx_pd
from util.student_no_wechat import StudentNoWechat
# from application.review_word.receive_word import receive_word
# from application.review_word.get_word import get_word
from util.parser_what_day import tbs_what_day

from data.private_space.mysql_func import *

import traceback
from loguru import logger

wxid_default = 'wxid_oftjmj5649kd22'

# 黑名单
blacklist = []

# logger = logging.getlogger(__file__)
# formatter = logging.Formatter('%(asctime)s [%(threadName)s] %(levelname)s: %(message)s')
# sh = logging.StreamHandler()
# sh.setFormatter(formatter)
# sh.setLevel(logging.DEBUG)
# logger.addHandler(sh)
# logger.setLevel(logging.INFO)

contact_list = []
chatroom_list = []

path_user_list = 'data/private_space/user_list.csv'

preparatory_grades = [18, 19, 20]
engineer_grades = [17, 16, 15]

url_17 = 'solars.top/kb/17/S1/'
url_16 = 'solars.top/kb/16/S3/'
url_15 = 'solars.top/kb/15/S5/'


class Student4inform:  # avoid the circular import
    def __init__(self, name, grade, a_or_b, p_ab_cd, f_ab_cd_e):
        self.name = name  # 微信备注名
        self.grade = grade  # 年级
        self.a_or_b = a_or_b  # 大AB班
        self.p_ab_cd = p_ab_cd  # td班
        self.f_ab_cd_e = f_ab_cd_e  # 法语班


def my_proto_parser(data):
    if data.type == WECHAT_CONNECTED:
        logger.info("微信连接成功")
        # logger.info("-"*10, "展示登录二维码", "-"*10)
        # spy.show_qrcode()
    elif data.type == WECHAT_LOGIN:
        logger.info("微信登录成功")
        spy.get_login_info()
    elif data.type == WECHAT_LOGOUT:
        logger.info("微信登出")
        send_mail()  # wechat登出警告信
    elif data.type == LOGIN_INFO:
        logger.info("登录信息")
        logger.info(data.login_info.wxid)
        logger.info(data.login_info.nickname)
        logger.info(data.login_info.wechatid)
        logger.info(data.login_info.phone)
        logger.info(data.login_info.profilephoto)
        spy.get_contacts()
    elif data.type == CONTACTS:
        logger.info("联系人列表")
        for contact in data.contact_list.contact:
            logger.info(contact.wxid, contact.nickname)
            if contact.wxid.startswith("gh_"):
                # 过滤公众号
                pass
            elif contact.wxid.endswith("chatroom"):
                # 群聊
                chatroom_list.append(contact.wxid)
            else:
                # 普通联系人
                contact_list.append(contact.wxid)
        logger.info(f"共{len(contact_list)}个联系人,{len(chatroom_list)}个群")

    elif data.type == MESSAGE:
        # 消息
        for message in data.message_list.message:
            remark_maybe = ''
            if not message.wxid2:
                remark_maybe = get_remark_from_sql(message.wxid1)
            from_whom = remark_maybe if remark_maybe else message.wxid1
            # logger.info(f"{from_whom}: {message.content}")
            if message.type == 1:
                logger.info(f"{from_whom}: {message.content}")
                if message.wxid1 == "filehelper":
                    spy.send_text("filehelper", "Hello PyWeChatSpy")

                # TODO: 添加信息
                code_add = re.match(r'^(@)(\d{2})([abAB])([a-dA-D])([a-eA-E])$', message.content)
                if code_add and len(message.wxid2) == 0 and message.wxid1 not in blacklist:
                    try:
                        if_add_success = add_user(message.wxid1, int(code_add.group(2)), code_add.group(3).upper(),
                                                  'P' + code_add.group(4).upper(), 'P' + code_add.group(5).upper())
                        if if_add_success:
                            send_msg = '[信息添加成功, 明早将开始自动推送]'
                            if int(code_add.group(2)) in preparatory_grades:
                                send_msg += '\n\n当前在数据库中储存的信息是:' + \
                                            f"\n年级：20{code_add.group(2)}级\n行政班：{code_add.group(3).upper()}班" + \
                                            f"\n习题班：{code_add.group(4).upper()}班\n法语班：{code_add.group(5).upper()}班" + \
                                            f'\n\n若输入有误，请发送"@td"退订后再重新添加信息'
                            send(message.wxid1, send_msg)
                            add_new_remark(message.wxid1)
                        else:
                            send(message.wxid1, '[error]在数据库中已有信息，重复添加无效。\n\n'
                                                '可发送"@信息"查看当前在数据库中储存的信息，若输入有误，请先发送"@td"来退订')
                    except Exception as e:
                        logger.error(str(e))
                        traceback.print_exc()
                elif code_add and message.wxid1 in blacklist and len(message.wxid2) == 0:
                    send(message.wxid1, '[refuse]很抱歉，您已被列入本程序黑名单')

                # TODO: 退订
                if message.content in ['@td', '@TD', '@Td', '@退订']:
                    try:
                        if_delete_success = delete_user(message.wxid1)

                        if if_delete_success:
                            send(message.wxid1, '[退订成功]')
                        else:
                            send(message.wxid1, '[error]出错了')
                    except Exception as e:
                        logger.error(e)

                # TODO: @今天,明天,后天...的课表
                tod_tom_dft = False
                code_situation = re.match(r'^@(.+天)$', message.content)
                if code_situation:
                    situation = code_situation.group(1)
                    user_info_ls = check_user(message.wxid1)
                    try:
                        student = StudentNoWechat(user_info_ls[0], user_info_ls[2], user_info_ls[3], user_info_ls[4],
                                                  user_info_ls[5])
                    except Exception as e:
                        logger.error(e)
                        send(message.wxid1, '未在数据库中检索到该账号的信息, 如果是需要课表推送的话可以向我发送"@说明"来查看使用说明')
                        raise Exception('未在数据库中检索到该账号的信息')

                    if student.name == message.wxid1:
                        if student.grade in preparatory_grades or student.grade in engineer_grades:
                            if situation == "今天":
                                message0 = student.get_schedule(situation=situation,
                                                                date=determine_date(),
                                                                week=determine_week(),
                                                                what_day=determine_what_day())
                                count_ask(message.wxid1, 0)
                                send(message.wxid1, message0)
                                tod_tom_dft = True
                            elif situation == "明天":
                                message0 = student.get_schedule(situation=situation,
                                                                date=determine_date(86400),
                                                                week=determine_week(86400),
                                                                what_day=determine_what_day(86400))
                                count_ask(message.wxid1, 1)
                                send(message.wxid1, message0)
                                tod_tom_dft = True
                            elif situation == "后天":
                                message0 = student.get_schedule(situation=situation,
                                                                date=determine_date(2 * 86400),
                                                                week=determine_week(2 * 86400),
                                                                what_day=determine_what_day(2 * 86400))
                                count_ask(message.wxid1, 2)
                                send(message.wxid1, message0)
                                tod_tom_dft = True
                            elif re.match(r"^大+后天$", situation):
                                n_day_delay = len(situation)
                                date_ht = determine_date(n_day_delay * 86400)
                                message0 = student.get_schedule(situation=situation,
                                                                date=date_ht,
                                                                week=determine_week(n_day_delay * 86400),
                                                                what_day=determine_what_day(n_day_delay * 86400))
                                count_ask(message.wxid1, 3)
                                send(message.wxid1, f"{situation}是{date_ht}\n\n" + message0)
                                tod_tom_dft = True
                        else:
                            send(message.wxid1, 'error,当前程序仅支持15,16,17,18,19,20级')

                # TODO: 星期一
                if message.content[0] == '@' and not tod_tom_dft:
                    situation = message.content[1:]
                    if_date = False
                    delay_for_what_day = 0
                    if situation in tbs_what_day:
                        pass
                    elif situation_match := re.match(r'^(\d{4})[-—./年](\d{1,2})[-—./月](\d{1,2})', situation):
                        date_month = situation_match.group(2)
                        if len(date_month) == 1:
                            date_month = '0' + date_month
                        date_day = situation_match.group(3)
                        if len(date_day) == 1:
                            date_day = '0' + date_day
                        situation = situation_match.group(1) + '-' + date_month + '-' + date_day
                        if_date = True
                    elif situation_match := re.match(r'^(\d{1,2})[-—./月](\d{1,2})', situation):
                        date_month = situation_match.group(1)
                        if len(date_month) == 1:
                            date_month = '0' + date_month
                        date_day = situation_match.group(2)
                        if len(date_day) == 1:
                            date_day = '0' + date_day
                        situation = determine_year() + '-' + date_month + '-' + date_day
                        if_date = True
                    else:
                        situation = ''
                    if situation:
                        try:
                            delay_for_what_day = parse_wd_ref_delay(situation, if_date)
                        except ValueError:
                            send(message.wxid1, '错误：输入不正确')
                            situation = ''
                    if situation:
                        user_info_ls = check_user(message.wxid1)
                        try:
                            student = StudentNoWechat(user_info_ls[0], user_info_ls[2], user_info_ls[3],
                                                      user_info_ls[4], user_info_ls[5])
                        except Exception as e:
                            logger.error(e)
                            send(message.wxid1, '未在数据库中检索到该账号的信息, 如果是需要课表推送的话可以向我发送"@说明"来查看使用说明')
                            raise Exception('未在数据库中检索到该账号的信息')

                        if student.name == message.wxid1:
                            if student.grade in preparatory_grades or student.grade in engineer_grades:
                                date_ht = determine_date(delay_for_what_day)
                                message0 = student.get_schedule(situation=situation,
                                                                date=date_ht,
                                                                week=determine_week(delay_for_what_day),
                                                                what_day=determine_what_day(delay_for_what_day))
                                if -1 < delay_for_what_day < 1:
                                    count_ask(message.wxid1, 0)
                                elif 86399 < delay_for_what_day < 86401:
                                    count_ask(message.wxid1, 1)
                                elif 2 * 86400 - 1 < delay_for_what_day < 2 * 86400 + 1:
                                    count_ask(message.wxid1, 2)
                                else:
                                    count_ask(message.wxid1, 3)
                                if not if_date:
                                    message0 = f"{situation}是{date_ht}\n\n" + message0
                                send(message.wxid1, message0)

                            else:
                                send(message.wxid1, 'error,当前程序仅支持15,16,17,18,19,20级')

                # TODO: 发送当前已填信息
                if message.content == '@信息':
                    user_list_tuple = check_user(message.wxid1)
                    if user_list_tuple:
                        user_list_list = list(user_list_tuple)
                        user_info = "当前在数据库中储存的信息是:\n@" + str(user_list_list[2]) + user_list_list[3] + \
                                    user_list_list[4][-1] + \
                                    user_list_list[5][-1]
                        exp_str = f"\n年级：{user_list_list[2]}级\n行政班：{user_list_list[3]}班" + \
                                  f"\n习题班：{user_list_list[4]}班\n法语班：{user_list_list[5][-1]}班" + \
                                  f'\n\n若输入有误，请发送"@td"退订后再重新添加信息'

                        send(message.wxid1, user_info + exp_str)
                    else:
                        send(message.wxid1, '未在数据库中检索到该账号的信息')

                # TODO: 发送wxid
                if message.content == '@wxid':
                    send(message.wxid1, message.wxid1)

                # TODO: 发送说明文件网址
                if message.content[:3] == '@说明':
                    send(message.wxid1,
                         '点此链接可查看课表推送的详细使用说明👇\nhttps://gitee.com/laorange/wechat_robot/blob/master/README.md')
                    send(message.wxid1, "也可以根据这个页面的提示直接生成启动指令👇\nlaorange.top/code.html")
                elif message.content[:3] == '@指令':
                    send(message.wxid1, '点此链接查看当前支持的所有指令👇\nhttp://laorange.top/kb/wdtbs.html')

                # TODO: 只有发给/来自指定号的口令才生效的功能
                if message.wxid1 == wxid_default:
                    # inform
                    code_inform = re.match(r'^@inform(\d{2})([abfpqABFPQ])([a-eA-E])([\s\S]+)', message.content)
                    if code_inform:
                        logger.info('!' * 5 + 'inform' + '!' * 5)
                        inform(code_inform, message.wxid1)

                    # csv to excel ##使用MySQL后该函数失效
                    # if message.content == '@excel':
                    #     logger.info('csv to excel')
                    #     csv_to_xlsx_pd()

                    # TODO: send user_info list to myself
                    if message.content == '@ul':
                        send(wxid_default, count_user_each_grade())

                    if message.content[:4] == '@dcf' or message.content[:4] == '@dce':
                        try:
                            if message.content[3] == 'e':
                                add_word_to_mysql(if_english=True, word_text=message.content[4:])
                                send(wxid_default, '已添加 英语单词')
                            elif message.content[3] == 'f':
                                add_word_to_mysql(if_english=False, word_text=message.content[4:])
                                send(wxid_default, '已添加 法语单词')
                            else:
                                raise Exception("'@dcf''@dce'判断条件出错")
                        except Exception as e:
                            send(wxid_default, str(e))
                            logger.error(e)
                            traceback.print_exc()
                        # else:
                        #     send(wxid_default, '添加成功')

                    # TODO: 查询法语单词
                    if message.content[:2] == '==':
                        send(wxid_default, 'http://www.frdic.com/dicts/fr/' + quote(message.content[2:]))

                    # TODO: 手动发送复习单词
                    code_review = re.match(r'@review(\d+)', message.content)
                    if code_review:
                        send_review_word(if_english=True, review_word_num=int(code_review.group(1)))
                        send_review_word(if_english=False, review_word_num=int(code_review.group(1)))

                    # TODO: 清除单词的学习记录
                    if message.content == '@clear en' or message.content == 'Clear en':
                        clear_all_review_record(True)
                        send(wxid_default, '已清除英语单词的学习记录')
                    # 清除单词的学习记录
                    elif message.content == '@clear fr' or message.content == 'Clear fr':
                        clear_all_review_record(False)
                        send(wxid_default, '已清除法语单词的学习记录')

                    # TODO: 更新用户备注名
                    if message.content == '@rfr':
                        refresh_remark()

            elif message.type == 3:
                logger.info("图片消息" + f"{from_whom}: {message.content}")
            elif message.type == 37:
                logger.info("好友请求消息" + f"\n{from_whom}: {message.content}")
            else:
                logger.info("其他消息")
                return
    elif data.type == QRCODE:
        logger.info("登录二维码")
        logger.info(data.qrcode.qrcode)
    elif data.type == CONTACT_EVENT:
        logger.info("联系人事件")
        logger.info(data)
    elif data.type == CHATROOM_MEMBERS:
        logger.info("群成员列表")
        member_list = data.chatroom_member_list
        chatroom_wxid = member_list.wxid
        logger.info(chatroom_wxid)
        for member in member_list.contact:
            logger.info(member.wxid, member.nickname)
    elif data.type == CONTACT_DETAILS:
        logger.info("联系人详情")
        user_list = get_user_list_wechat_id()
        for details in data.contact_list.contact:
            if details.wxid in user_list:
                set_remark(details.wxid, details.remark)
            # logger.info("details.wxid", details.wxid)
            # logger.info("details.nickname", details.nickname)
            # logger.info("details.wechatid", details.wechatid)
            # logger.info("details.remark", details.remark)
            # logger.info("details.profilephoto", details.profilephoto)
            # logger.info("details.profilephoto_hd", details.profilephoto_hd)
            # logger.info("details.sex", details.sex)
            # logger.info("details.whats_up", details.whats_up)
            # logger.info("details.country", details.country)
            # logger.info("details.province", details.province)
            # logger.info("details.city", details.city)
            # logger.info("details.source", details.source)
    elif data.type == HEART_BEAT:
        # 心跳
        pass


spy = WeChatSpy(parser=my_proto_parser, key="授权Key", logger=logger)


def send(wxid: str, content: str):
    if len(content) >= 1000:
        content = content[:999]
    if content:
        spy.send_text(wxid, content)


def send_msg_when(wxid: str, content: str, send_time: str):
    """
    定时发送微信消息
    :param wxid: 对方的wxid
    :param content: 内容
    :param send_time: 形如'2020-08-07 17:17:10' ‘%Y-%m-%d %H:%M’的时间
    """
    do_at_sometime(lambda: send(wxid, content), send_time)


def log_in():
    t1 = Thread(target=spy.run)
    t1.start()
    logger.info('start receiving wechat message')


def inform(code_inform, wxid: str):
    # user_list_path = 'data/private_space/user_list.csv'
    user_list = get_user_list_all_data()
    student_ls = []
    for user in user_list:
        user_info_ls = list(user)
        student_ls.append(Student4inform(user_info_ls[0], user_info_ls[2], user_info_ls[3], user_info_ls[4],
                                         user_info_ls[5]))
    for student in student_ls:
        if student.grade == int(code_inform.group(1)):
            if code_inform.group(2) in ['p', 'P']:
                if 'P' + code_inform.group(3).upper() == student.p_ab_cd:
                    send(student.name, code_inform.group(4))
            elif code_inform.group(2) in ['f', 'F']:
                if 'P' + code_inform.group(3).upper() == student.f_ab_cd_e:  # 不知道法语班是不是p开头
                    send(student.name, code_inform.group(4))
            elif code_inform.group(2) in ['a', 'A']:
                if student.a_or_b == 'A':
                    send(student.name, code_inform.group(4))
            elif code_inform.group(2) in ['b', 'B']:
                if student.a_or_b == 'B':
                    send(student.name, code_inform.group(4))
            elif code_inform.group(2) in ['q', 'Q']:
                send(student.name, code_inform.group(4))
            time.sleep(1.1)
    spy.send_text(wxid, 'done')


def add_new_remark(wechat_id):
    spy.get_contact_details(wechat_id, update=True)


def refresh_remark():
    id_for_check = get_user_list_wechat_id()
    for wechat_id in id_for_check:
        spy.get_contact_details(wechat_id, update=False)
        time.sleep(2)


# def check_wxid_info(wxid: str):
#     wxid_detail = spy.get_contact_details(wxid, update=False)
#     logger.info(type(wxid_detail))
#     logger.info(wxid_detail)


def send_review_word_two_language(review_en_word_num: int, review_fr_word_num: int):
    send_review_word(if_english=True, review_word_num=review_en_word_num)
    send_review_word(if_english=False, review_word_num=review_fr_word_num)


def send_review_word(if_english: bool, review_word_num: int):
    word_send = ''
    word_tran = ''

    try:
        word_info_list = get_word_from_mysql(if_english=if_english)
        if word_info_list:
            if review_word_num > len(word_info_list):
                review_word_num = len(word_info_list)
            index_ls = []

            i = 0
            while i < review_word_num:
                index_num = random.randint(0, len(word_info_list) - 1)
                while index_num in index_ls:
                    index_num = random.randint(0, len(word_info_list) - 1)
                possibility = random.random()
                if word_info_list[index_num].possibility >= possibility:
                    if word_send == '':
                        word_send = '  1. ' + word_info_list[index_num].word
                        if if_english:
                            word_tran = '  1. http://dict.eudic.net/dicts/en/' + word_info_list[index_num].word
                        else:
                            word_tran = '  1. http://www.frdic.com/dicts/fr/' + word_info_list[index_num].word
                    else:
                        i_num_str = '  ' + str(i + 1) + '. ' if i + 1 < 10 else str(i + 1) + '. '
                        word_send = word_send + '\n' + i_num_str + word_info_list[index_num].word
                        if if_english:
                            word_tran = word_tran + '\n' + i_num_str + 'http://dict.eudic.net/dicts/en/' + quote(
                                word_info_list[index_num].word)
                        else:
                            word_tran = word_tran + '\n' + i_num_str + 'http://www.frdic.com/dicts/fr/' + quote(
                                word_info_list[index_num].word)

                    review_times_plus1(if_english, word_info_list[index_num].word)

                    word_info_list[index_num].review_times += 1
                    word_info_list[index_num].review_date = determine_date()

                    index_ls.append(index_num)
                    i += 1

            if word_send:
                send(wxid_default, word_tran)
                send(wxid_default, word_send)
                if if_english:
                    logger.info(f'复习了{review_word_num}个英语单词')
                else:
                    logger.info(f'复习了{review_word_num}个法语单词')
    except Exception as e:
        logger.error(e)
        traceback.print_exc()


def clear_all_review_record(if_english: bool):
    word_info_list = get_word_from_mysql(if_english=if_english)
    for word_info in word_info_list:
        clear_review_record(if_english=if_english, word=word_info.word)


# 定制发送
def personalisation():
    # zjc的每日提醒
    wxid_zjc = 'wxid_70vvmt9lxao722'
    send_msg_when(wxid_zjc, '法语听力打卡', determine_date() + ' 09:35:00')


if __name__ == '__main__':
    log_in()
    # t2 = Thread(target=send_msg_when(wxid_default, '测试1222', '2020-08-18 12:22:00'))
    # t2.start()
    # send_file(, 'qrcode_laorange.png')
    # check_wxid_info(wxid_default)
