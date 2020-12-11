# from util.wechat_func import send

import csv

path = "C:\\Users\\Administrator\\Desktop\\consult_times.csv"
with open(path, encoding='UTF-8') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]


class User:
    def __init__(self, ls):
        # rank, remark, wxid, ask_today, ask_tom, ask_dat, ask_far, total_times
        self.rank = ls[0]
        self.remark = ls[1]
        self.wxid = ls[2]
        self.ask_today = ls[3]
        self.ask_tom = ls[4]
        self.ask_dat = ls[5]
        self.ask_far = ls[6]
        self.total_times = ls[7]
        self.msg = f"""[旺柴]小彩蛋来啦
[旺柴]10月12日傍晚17点48分
[旺柴]某个悄悄加上的小模块开始生效
[旺柴]现在它来了

[旺柴]查询次数统计
[旺柴]10.12 ~ 12.11
[旺柴]在这60天里，
[旺柴]共有85位用户总查询次数≥6次，
您的总查询次数是 {self.total_times}次，
[旺柴]其中：
@今天 {self.ask_today}次
@明天 {self.ask_tom}次
@后天 {self.ask_dat}次
# 其他 {self.ask_far}次
位列 第{self.rank}名

http://laorange.top/kb/statistic

[旺柴]出现了11次
[旺柴]提前祝大家考试顺利，假期愉快！
"""


user_list_more_than_5 = []

for i in range(1, len(rows)):
    user = User(rows[i])
    user_list_more_than_5.append(user)

if __name__ == '__main__':
    for user in user_list_more_than_5:
        print(user.remark, user.wxid, user.msg)
