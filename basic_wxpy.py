# 导入模块
from wxpy import *

import time
from pprint import pprint

from robot import get_answer  # chat_robot
from func_aspscheduler import do_at_sometime

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)
bot.enable_puid()
bot.auto_mark_as_read = True

my_friend = bot.friends().search('大号')[0]
print(my_friend.puid)


def send_person(target_person, message):
    target_friend = bot.friends().search(target_person)[0]
    target_friend.send(message)


def send_msg_when(target_person, message, send_time):
    def send():
        target = bot.friends().search(target_person)[0]
        # print(target)
        target.send(message)
    do_at_sometime(func=send, run_date=send_time)


if __name__ == "__main__":
    send_msg_when(target_person='大号', message='7点05了', send_time='2020-08-07 19:05:00')
    # while True:
    #     time.sleep(1)

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


@bot.register(Friend, TEXT)
def print_group_msg(msg):
    print(msg)
    answer = get_answer(msg.text)
    msg.chat.send(answer)

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
    # 判断好友请求中的验证文本
    # if 'wxpy' in msg.text.lower():
    if True:
        # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
        # 或 new_friend = msg.card.accept()
        # 向新的好友发送消息
        msg.chat.send('测试：我自动接受了你的好友请求')

        if msg[:2] == '我是':
            new_friend.set_remark_name(msg.text[2:])
        else:
            new_friend.set_remark_name(msg.text)



# @bot.register(Group, TEXT)
# def print_group_msg(msg):
#     print(msg)
#     # answer = get_answer(msg.text)
#     msg.chat.send(answer)


bot.join()
