from PyWeChatSpy.PyWeChatSpy import WeChatSpy
from PyWeChatSpy.PyWeChatSpy.command import *
# from lxml import etree
import logging

import re
import time
from threading import Thread

# project内
from data.message import send_mail
from util.func_apscheduler import do_at_sometime
from util.basic_functions import read_file2list

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
        # 查询联系人列表(付费)
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
        # print("-"*10, "获取联系人详情(部分付费)", contact_list[5], "-"*10)
        # spy.get_contact_details(contact_list[5], True)
        # print("设置群名称(付费)", chatroom_list[0])
        # spy.set_chatroom_name(chatroom_list[0], "PyWeChatSpy")
        # print("发送群公告", chatroom_list[0])
        # spy.send_announcement(chatroom_list[0], "本条消息由PyWeChatSpy发出(https://zhuanlan.zhihu.com/p/118674498)")
        # print("创建群聊(付费)")
        # spy.create_chatroom(f"{contact_list[1]},{contact_list[2]},{contact_list[3]}")
        # print("-"*10, "获取群成员列表(付费)", chatroom_list[0], "-"*10)
        # spy.get_chatroom_members(chatroom_list[0])
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
                            with open(path_user_list, 'at') as user_ls:
                                user_ls.write(
                                    message.wxid1 + ',' + code_add.group(2) + ',' + code_add.group(
                                        3).upper() + ',P' + code_add.group(
                                        4).upper() + ',P' + code_add.group(5).upper() + '\n')
                            send(message.wxid1, '信息添加成功')
                        except Exception as e:
                            print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), e)

                    elif code_add.group(1) == '。':
                        try:
                            with open('data/private_space/user_list.csv') as user_list_csv:
                                user_ls = user_list_csv.readlines()
                            user_info_str = message.wxid1 + ',' + code_add.group(2) + ',' + code_add.group(
                                3).upper() + ',P' + code_add.group(4).upper() + ',P' + code_add.group(5).upper() + '\n'
                            try:
                                if user_info_str in user_ls:
                                    try:
                                        user_ls.remove(user_info_str)
                                    except Exception as e:
                                        print('移除失败', e)
                                        send(message.wxid1, '信息删除失败，稍微将为您手动删除')
                                        raise Exception('移除失败')
                                else:
                                    send(message.wxid1, '未找到这条信息，请检查后重试；若始终无法成功，则是数据编码出现了问题，稍微我将为您手动删除')
                                    raise Exception('未找到这条信息')
                            except Exception as e:
                                print(e)
                            else:
                                with open(path_user_list, 'wt') as user_ls_csv:
                                    for user_info in user_ls:
                                        user_ls_csv.write(user_info)
                                send(message.wxid1, '信息删除成功')
                        except Exception as e:
                            print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), e)

            elif message.type == 3:
                print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "图片消息", "-" * 10)
            elif message.type == 37:
                print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "好友请求消息", "-" * 10)
                # 好友请求消息
                # obj = etree.XML(message.content)
                # encryptusername, ticket = obj.xpath("/msg/@encryptusername")[0], obj.xpath("/msg/@ticket")[0]
                # 接收好友请求(付费)
                # spy.accept_new_contact(encryptusername, ticket)
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
            # 添加群成员为好友(付费)
            # 高风险操作 频率较高容易引发微信风控
            # spy.add_contact(
            #     member.wxid,
            #     chatroom_wxid,
            #     "来自PyWeChatSpy(https://zhuanlan.zhihu.com/p/118674498)的问候",
            #     ADD_CONTACT_A)
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
    print('start receiving wechat message')


if __name__ == '__main__':
    log_in()
    t2 = Thread(target=send_msg_when('wxid_oftjmj5649kd22', '测试1222', '2020-08-18 12:22:00'))
    t2.start()
