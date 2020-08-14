# 导入模块
from wxpy import *
import re
import os

# import time
# from pprint import pprint

# from robot import get_answer  # chat_robot
from util.func_apscheduler import do_at_sometime
from util.basic_functions import read_file2list

path_user_list = 'data/private_space/user_list.csv'

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)
bot.enable_puid()
bot.auto_mark_as_read = True

my_friend = bot.friends().search('大号')[0]
print('已找到:', my_friend.name, "-", my_friend.nick_name)


def send_person(target_person, message):
    target_friend = bot.friends().search(target_person)[0]
    target_friend.send(message)


def send_msg_when(target_person, message, send_time):
    def send():
        target = bot.friends().search(target_person)[0]
        # print(target)
        target.send(message)

    try:
        do_at_sometime(func=send, run_time=send_time)
    except Exception as e:
        print(e)


# hushaoc = bot.friends().search('235d4d80')[0]
# print(hushaoc)

# # 获取简单的好友统计
# friend_total = bot.friends().stats_text()
# pprint(friend_total)
#
# # 获取微信好友
# wx_friend = bot.friends()
# pprint(wx_friend)
# print(len(wx_friend))
#
# # 获取微信群
# wx_group = bot.groups()
# pprint(wx_group)
# print(len(wx_group))
#
# # 获取公众号
# wx_mps = bot.mps()
# pprint(wx_mps)
# print(len(wx_mps))

def bot_register():
    @bot.register(Friend, TEXT)
    def print_group_msg(msg):
        print(msg)
        code_add = re.match(r'^#(20\d{2})([abAB])([a-dA-D])([a-eA-E])$', msg.text)
        if code_add:
            with open(path_user_list, 'at', encoding='UTF-8') as user_ls:
                user_ls.write(
                    msg.chat.name + ',' + code_add.group(1) + ',' + code_add.group(2).upper() + ',P' + code_add.group(
                        3).upper() + ',P' + code_add.group(4).upper() + '\n')
            msg.chat.send('信息添加成功')

        code_delete = re.match(r'^*(20\d{2})([abAB])([a-dA-D])([a-eA-E])$', msg.text)
        if code_delete:
            user_ls = read_file2list('data/private_space/user_list.csv')
            user_info_str = msg.chat.name + ',' + code_add.group(1) + ',' + code_add.group(
                2).upper() + ',P' + code_add.group(3).upper() + ',P' + code_add.group(4).upper()
            if user_info_str in user_ls:
                user_ls.remove(user_ls)
            with open(path_user_list, 'wt') as user_ls:
                for user_info in user_ls:
                    user_ls.write(user_info + '\n')
            msg.chat.send('信息删除成功')

        # test_ls = msg.text.split('.')
        # try:
        #     send_msg_when(test_ls[0], test_ls[1], test_ls[2])
        # except:
        #     print('error')
        #     pass

    # 注册好友请求类消息
    @bot.register(msg_types=FRIENDS)
    # 自动接受验证信息中包含 'wxpy' 的好友请求
    def auto_accept_friends(msg):
        try:
            # 接受好友 (msg.card 为该请求的用户对象)
            new_friend = bot.accept_friend(msg.card)
            # 或 new_friend = msg.card.accept()

            if msg[:2] == '我是':
                new_remark_name = msg.text[2:]
                new_friend.set_remark_name(new_remark_name)

            else:
                new_remark_name = msg.text
                new_friend.set_remark_name(new_remark_name)

            # 向新的好友发送消息
            bot.friends().search(new_remark_name)[0].sent('测试：我自动接受了你的好友请求')
            print("已添加"+new_remark_name)
        except Exception as e:
            print(e)

    # @bot.register(Group, TEXT)
    # def print_group_msg(msg):
    #     print(msg)
    #     # answer = get_answer(msg.text)
    #     msg.chat.send(answer)

    @bot.register(msg_types=[VIDEO, PICTURE, ATTACHMENT])
    def print_group_msg(msg):
        # print('[VIDEO, PICTURE, ATTACHMENT]')
        try:
            os.mkdir('data/download/'+msg.chat.name)
        except FileExistsError:
            pass
        finally:
            msg.get_file(save_path='data/download/'+msg.chat.name+'/'+msg.file_name)
            print('已下载:'+'data/download/'+msg.chat.name+'/'+msg.file_name)

    bot.join()
    # embed()


if __name__ == "__main__":
    bot_register()
