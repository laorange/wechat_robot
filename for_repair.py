﻿# PyWeChatSpy is cloned from https://github.com/veikai/PyWeChatSpy
# 该项目文件夹clone后放在了base_on_PyWeChatSpy下
from PyWeChatSpy.PyWeChatSpy import WeChatSpy
from PyWeChatSpy.PyWeChatSpy.command import *
# from lxml import etree
import logging

# import re
import time
# import random
from threading import Thread
# from urllib.parse import quote

# project内
from data.message import send_mail
from data.private_space.mysql_func import *

# from util.func_apscheduler import do_at_sometime

wxid_default = 'wxid_oftjmj5649kd22'

contact_list = []
chatroom_list = []

path_user_list = 'data/private_space/user_list.csv'

url_17 = 'solars.top/kb/17/S1/'
url_16 = 'solars.top/kb/16/S3/'
url_15 = 'solars.top/kb/15/S5/'

inform_message = 'sorry，正在迁移数据，预计18点38分后恢复。\n\n当前仍可以向我发送"@说明"来查看本程序的使用说明，除此以外其余功能都暂时失效'


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

                # 发送wxid
                if message.content == '@wxid':
                    send(message.wxid1, message.wxid1)

                # 发送说明文件网址
                elif message.content[:3] == '@说明':
                    send(message.wxid1,
                         '点此链接可查看本程序的详细说明: http://laorange.top/kb/readme')

                elif message.content[0] == '@' and message.wxid2 == '' and message.wxid1[-8:] != 'chatroom':
                    send(message.wxid1, inform_message)

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
        user_list_all_data = get_user_list_all_data()
        user_wechat_id_ls = []
        for user in user_list_all_data:
            user_wechat_id_ls.append(user[0])
        for details in data.contact_list.contact:
            if details.wxid in user_wechat_id_ls:
                set_remark(details.wxid, details.remark)
            # print("details.wxid", details.wxid)
            # print("details.nickname", details.nickname)
            # print("details.wechatid", details.wechatid)
            # print("details.remark", details.remark)
            # print("details.profilephoto", details.profilephoto)
            # print("details.profilephoto_hd", details.profilephoto_hd)
            # print("details.sex", details.sex)
            # print("details.whats_up", details.whats_up)
            # print("details.country", details.country)
            # print("details.province", details.province)
            # print("details.city", details.city)
            # print("details.source", details.source)
    elif data.type == HEART_BEAT:
        # 心跳
        pass


spy = WeChatSpy(parser=my_proto_parser, key="授权Key", logger=logger)


def send(wxid: str, content: str):
    spy.send_text(wxid, content)


def log_in():
    t1 = Thread(target=spy.run)
    t1.start()
    print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), 'start receiving wechat message')


def check_wxid_info(wxid: str):
    wxid_detail = spy.get_contact_details(wxid, update=False)
    # print(type(wxid_detail))
    # print(wxid_detail)


if __name__ == '__main__':
    log_in()
    # id_for_check = ['wxid_05y4vxo5az4n22', 'wxid_4fuc7xqgzox722', 'wxid_akeuhced41lg21', 'wxid_apf85yacqnc511',
    #                 'wxid_bjjvb22db76311', 'wxid_fpdcwt46zrzc22', 'wxid_ks1wry1vyb3122', 'wxid_m943tmk85n0022',
    #                 'wxid_qortcjb2mc6922', 'wxid_t84qg4635ueg22', 'wxid_wg1bnt5dc3s132', ]
    # user_list_all_data = get_user_list_all_data()
    # user_wechat_id_ls = []
    # for user in user_list_all_data:
    #     user_wechat_id_ls.append(user[0])
    # id_for_check = user_wechat_id_ls
    #
    # for wechat_id in id_for_check:
    #     print(wechat_id)
    #     check_wxid_info(wechat_id)
    #     # print('\n\n')
    #     time.sleep(3)

    # import pymysql
    # db = pymysql.connect()
    # # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()

    # grade_ls = []
    #
    # sql1 = 'SELECT `wechat_id` FROM `wechat_robot`.`user_list` WHERE `grade` = 20;'
    #
    # db.ping(reconnect=True)
    # cursor.execute(sql1)
    # while True:
    #     row = cursor.fetchone()
    #     if not row:
    #         break
    #     grade_ls.append(str(row[0]))
    #
    # for wechat_id in grade_ls:
    #     print(wechat_id)
    #     check_wxid_info(wechat_id)
    #     print('\n\n')
    #     time.sleep(5)

    # blacklist = ['wxid_l7g2lb2rsop622']
