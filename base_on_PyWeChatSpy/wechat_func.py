# PyWeChatSpy is cloned from https://github.com/veikai/PyWeChatSpy
# 该项目文件夹clone后放在了base_on_PyWeChatSpy下
from PyWeChatSpy.PyWeChatSpy import WeChatSpy
from PyWeChatSpy.PyWeChatSpy.command import *
# from lxml import etree
import logging

import re
import time
import random
from threading import Thread
from urllib.parse import quote

# project内
from data.message import send_mail
from util.func_apscheduler import do_at_sometime
from util.basic_functions import read_file2list
from util.week import determine_date, determine_week, determine_what_day
from util.csv2excel import csv_to_xlsx_pd
from util.student_no_wechat import StudentNoWechat
from application.review_word.receive_word import receive_word
# from application.review_word.get_word import get_word

from data.private_space.mysql_func import *

wxid_default = 'wxid_oftjmj5649kd22'

logger = logging.getLogger(__file__)
formatter = logging.Formatter('%(asctime)s [%(threadName)s] %(levelname)s: %(message)s')
sh = logging.StreamHandler()
sh.setFormatter(formatter)
sh.setLevel(logging.DEBUG)
logger.addHandler(sh)
logger.setLevel(logging.INFO)

contact_list = []
chatroom_list = []

path_user_list = 'data/private_space/user_list.csv'

url_2017 = 'solars.top/kb/17/S1/'
url_2016 = 'solars.top/kb/16/S3/'
url_2015 = 'solars.top/kb/15/S5/'


class Student4inform:  # avoid the circular import
    def __init__(self, name, grade, a_or_b, p_ab_cd, f_ab_cd_e):
        self.name = name  # 微信备注名
        self.grade = grade  # 年级
        self.a_or_b = a_or_b  # 大AB班
        self.p_ab_cd = p_ab_cd  # td班
        self.f_ab_cd_e = f_ab_cd_e  # 法语班


def my_proto_parser(data):
    if data.type == WECHAT_CONNECTED:
        print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "微信连接成功", "-" * 10)
        # print("-"*10, "展示登录二维码", "-"*10)
        # spy.show_qrcode()
    elif data.type == WECHAT_LOGIN:
        print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "微信登录成功", "-" * 10)
        spy.get_login_info()
    elif data.type == WECHAT_LOGOUT:
        print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "微信登出", "-" * 10)
        send_mail()  # wechat登出警告信
    elif data.type == LOGIN_INFO:
        print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "登录信息", "-" * 10)
        print(data.login_info.wxid)
        print(data.login_info.nickname)
        print(data.login_info.wechatid)
        print(data.login_info.phone)
        print(data.login_info.profilephoto)
        spy.get_contacts()
    elif data.type == CONTACTS:
        print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "联系人列表", "-" * 10)
        for contact in data.contact_list.contact:
            print(contact.wxid, contact.nickname)
            if contact.wxid.startswith("gh_"):
                # 过滤公众号
                pass
            elif contact.wxid.endswith("chatroom"):
                # 群聊
                chatroom_list.append(contact.wxid)
            else:
                # 普通联系人
                contact_list.append(contact.wxid)
        print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), f"共{len(contact_list)}个联系人,{len(chatroom_list)}个群",
              "-" * 10)

    elif data.type == MESSAGE:
        # 消息
        for message in data.message_list.message:
            if message.type == 1:
                print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "文本消息", "-" * 10)
                if message.wxid1 == "filehelper":
                    spy.send_text("filehelper", "Hello PyWeChatSpy")

                code_add = re.match(r'^([@。])(20\d{2})([abAB])([a-dA-D])([a-eA-E])$', message.content)
                if code_add and len(message.wxid2) == 0:
                    if code_add.group(1) == '@':
                        try:
                            # with open(path_user_list, 'at') as user_ls:
                            #     user_ls.write(
                            #         message.wxid1 + ',' + code_add.group(2) + ',' + code_add.group(
                            #             3).upper() + ',P' + code_add.group(
                            #             4).upper() + ',P' + code_add.group(5).upper() + '\n')
                            if_add_success = add_user(message.wxid1, int(code_add.group(2)), code_add.group(3).upper(),
                                                      'P' + code_add.group(4).upper(), 'P' + code_add.group(5).upper())
                            if if_add_success:
                                send(message.wxid1, '[信息添加成功]')
                            else:
                                send(message.wxid1, '[error]')
                        except Exception as e:
                            print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), e)

                    elif code_add.group(1) == '。':
                        try:
                            # with open(path_user_list) as user_list_csv:
                            #     user_ls = user_list_csv.readlines()
                            # user_info_str = message.wxid1 + ',' + code_add.group(2) + ',' + code_add.group(
                            #     3).upper() + ',P' + code_add.group(4).upper() + ',P' + code_add.group(5).upper() + '\n'
                            # try:
                            #     if user_info_str in user_ls:
                            #         try:
                            #             user_ls.remove(user_info_str)
                            #         except Exception as e:
                            #             print('[移除失败]', e)
                            #             send(message.wxid1, '[信息删除失败，稍微将为您手动删除]')
                            #             raise Exception('[移除失败]')
                            #     else:
                            #         send(message.wxid1, '[未找到这条信息，请检查后重试；若始终无法成功，则是数据编码出现了问题，稍微我将为您手动删除]')
                            #         raise Exception('[未找到这条信息]')

                            if_delete_success = delete_user(message.wxid1)

                            # except Exception as e:
                            #     print(e)
                            #
                            # else:
                            #     with open(path_user_list, 'wt') as user_ls_csv:
                            #         for user_info in user_ls:
                            #             user_ls_csv.write(user_info)
                            if if_delete_success:
                                send(message.wxid1, '[信息删除成功]')
                            else:
                                send(message.wxid1, '[error]')
                        except Exception as e:
                            print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), e)

                # @今天,明天 获取今天/明天的课表
                if message.content == '@今天' or message.content == '@明天':
                    if_tomorrow = False if message.content == '@今天' else True
                    # user_list_path = 'data/private_space/user_list.csv'
                    # user_list = read_file2list(user_list_path)
                    user_list = get_user_list()
                    student_ls = []
                    for user in user_list:
                        user_info_ls = list(user)
                        student_ls.append(
                            StudentNoWechat(user_info_ls[0], user_info_ls[1], user_info_ls[2], user_info_ls[3],
                                            user_info_ls[4]))
                    for student in student_ls:
                        if student.name == message.wxid1:
                            if student.grade in [2015, 2016, 2017, 2018, 2019, 2020]:
                                message0 = student.get_schedule(date=determine_date(), if_tomorrow=if_tomorrow,
                                                                week=determine_week(), what_day=determine_what_day())
                                send(message.wxid1, message0)

                            else:
                                send(message.wxid1, 'error,当前程序仅支持15,16,17,18,19,20级')

                # 发送当前已填信息
                if message.content == '@信息':
                    user_list_tuple = check_user(message.wxid1)
                    if user_list_tuple:
                        user_list_list = list(user_list_tuple)
                        user_info = str(user_list_list[1]) + user_list_list[2] + user_list_list[3][-1] + user_list_list[4][-1]
                        send(message.wxid1, user_info)
                    else:
                        send(message.wxid1, '未检索到信息')

                # 发送wxid
                if message.content == '@wxid':
                    send(message.wxid1, message.wxid1)

                # 发送说明文件网址
                if message.content[:3] == '@说明':
                    send(message.wxid1,
                         '点此链接可查看本程序的详细说明: https://gitee.com/laorange/wechat_robot/blob/master/README.md')

                # 只有发给/来自指定号的口令才生效的功能
                if message.wxid1 == wxid_default:
                    # inform
                    code_inform = re.match(r'^@inform(20\d{2})([abfpqABFPQ])([a-eA-E])([\s\S]+)', message.content)
                    if code_inform:
                        print('!' * 5 + 'inform' + '!' * 5)
                        inform(code_inform, message.wxid1)

                    # csv to excel
                    if message.content == '@excel':
                        print('csv to excel')
                        csv_to_xlsx_pd()

                    # send user_info list to myself
                    # if message.content == '@ul':
                    #     with open(path_user_list) as user_list_csv:
                    #         user_list_csv_str = user_list_csv.read()
                    #         send(message.wxid1, user_list_csv_str)

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
                        # else:
                        #     send(wxid_default, '添加成功')

                    # 查询法语单词
                    if message.content[:2] == '==':
                        send(wxid_default, 'http://www.frdic.com/dicts/fr/' + quote(message.content[2:]))

                    # 手动发送复习单词
                    code_review = re.match(r'@review(\d+)', message.content)
                    if code_review:
                        send_review_word(if_english=True, review_word_num=int(code_review.group(1)))
                        send_review_word(if_english=False, review_word_num=int(code_review.group(1)))

                    # 清除英语单词的学习记录
                    if message.content == '@clear en' or message.content == 'Clear en':
                        clear_all_review_record(True)
                        send(wxid_default, '已清除英语单词的学习记录')
                    # 清除单词的学习记录
                    elif message.content == '@clear fr' or message.content == 'Clear fr':
                        clear_all_review_record(False)
                        send(wxid_default, '已清除法语单词的学习记录')

            elif message.type == 3:
                print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "图片消息", "-" * 10)
            elif message.type == 37:
                print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "好友请求消息", "-" * 10)
            else:
                print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "其他消息", "-" * 10)
                return
            print(f"来源:{message.wxid1}", end='\t')
            # print("来源2:", message.wxid2)
            # print("消息头:", message.head)
            print(f"消息内容:{message.content}")
    elif data.type == QRCODE:
        print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "登录二维码", "-" * 10)
        print(data.qrcode.qrcode)
    elif data.type == CONTACT_EVENT:
        print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "联系人事件", "-" * 10)
        print(data)
    elif data.type == CHATROOM_MEMBERS:
        print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "群成员列表", "-" * 10)
        member_list = data.chatroom_member_list
        chatroom_wxid = member_list.wxid
        print(chatroom_wxid)
        for member in member_list.contact:
            print(member.wxid, member.nickname)
    elif data.type == CONTACT_DETAILS:
        print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "联系人详情", "-" * 10)
        for details in data.contact_list.contact:
            print(details.wxid)
            print(details.nickname)
            print(details.wechatid)
            print(details.remark)
            print(details.profilephoto)
            print(details.profilephoto_hd)
            print(details.sex)
            print(details.whats_up)
            print(details.country)
            print(details.province)
            print(details.city)
            print(details.source)
    elif data.type == HEART_BEAT:
        # 心跳
        pass


spy = WeChatSpy(parser=my_proto_parser, key="授权Key", logger=logger)


def send(wxid: str, content: str):
    if len(content) >= 1000:
        content = content[:999]
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
    print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), 'start receiving wechat message')


def inform(code_inform, wxid: str):
    user_list_path = 'data/private_space/user_list.csv'
    user_list = read_file2list(user_list_path)
    student_ls = []
    for user in user_list:
        user_info_ls = user.split(',')
        student_ls.append(Student4inform(user_info_ls[0], user_info_ls[1], user_info_ls[2], user_info_ls[3],
                                         user_info_ls[4]))
    for student in student_ls:
        if student.grade == code_inform.group(1):
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
    spy.send_text(wxid, 'done')


# def check_wxid_info(wxid: str):
#     wxid_detail = spy.get_contact_details(wxid, update=False)
#     print(type(wxid_detail))
#     print(wxid_detail)


def send_review_word_two_language(review_en_word_num: int, review_fr_word_num: int):
    send_review_word(if_english=True, review_word_num=review_en_word_num)
    send_review_word(if_english=False, review_word_num=review_fr_word_num)


def send_review_word(if_english: bool, review_word_num: int):
    word_send = ''
    word_tran = ''

    try:
        word_info_list = get_word_from_mysql(if_english=if_english)
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
                print(f'复习了{review_word_num}个英语单词')
            else:
                print(f'复习了{review_word_num}个法语单词')
    except Exception as e:
        print(e)


def clear_all_review_record(if_english: bool):
    word_info_list = get_word_from_mysql(if_english=if_english)
    for word_info in word_info_list:
        clear_review_record(if_english=if_english, word=word_info.word)


if __name__ == '__main__':
    log_in()
    # t2 = Thread(target=send_msg_when(wxid_default, '测试1222', '2020-08-18 12:22:00'))
    # t2.start()
    # send_file(, 'qrcode_laorange.png')
    # check_wxid_info(wxid_default)
