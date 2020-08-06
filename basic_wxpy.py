# 导入模块
from wxpy import *
from pprint import pprint

from robot import get_answer

# 初始化机器人，扫码登陆
bot = Bot(cache_path=True)
bot.enable_puid()
bot.auto_mark_as_read = True

my_friend = bot.friends().search('辣橙')[0]
print(my_friend.puid)

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


bot.join()
