from schedule.schedule2018 import schedule_2018
from schedule.schedule2019 import schedule_2019
# from schedule.schedule2020 import schedule_2020
from random import randint

from wechat_func import send_msg_when
from util.weather import get_weather
from util.student_no_wechat import StudentNoWechat

url_2017 = 'solars.top/kb/17/S1/'
url_2016 = 'solars.top/kb/16/S3/'
url_2015 = 'solars.top/kb/15/S5/'

preparatory_grades = [2018, 2019, 2020]
engineer_grades = [2017, 2016, 2015]


class Student(StudentNoWechat):
    def __init__(self, name, grade, a_or_b, p_ab_cd, f_ab_cd_e):
        super(Student, self).__init__(name, grade, a_or_b, p_ab_cd, f_ab_cd_e)
        # 为了避免达到发送阈值
        if randint(0, 1):
            self.send_hour = '5'
            self.send_min = str(randint(30, 59))
            self.send_sec = str(randint(0, 59))
        else:
            self.send_hour = '6'
            self.send_min = str(randint(0, 30))
            self.send_sec = str(randint(0, 59))

    def send_weather(self, week: int, date: str):
        try:
            # 发送天气
            print('-' * 9, '↓', self.name, '↓', '-' * 10)
            # 6:30通报全天有哪些课，以及第一节课的详细信息
            weather = get_weather()
            if week == -1:
                message_weather = '今天是' + date + '，新学期即将开始\n' + weather
            else:
                if not self.replacement:
                    message_weather = '今天是' + date + '，这周是本学期的第' + str(week + 1) + '周\n' + weather
                else:
                    message_weather = '今天是' + date + '，这周是本学期的第' + str(week + 1) + '周，今天补的是第' + str(
                        self.week + 1) + '周' + self.what_day + '的课\n' + weather
            print(message_weather)
            send_msg_when(self.name, message_weather,
                          date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
        except Exception as e:
            print("发送天气时出错")
            print(e)

    def send_schedule_auto(self, if_tomorrow: bool, date: str, week: int, what_day: str):
        message0 = self.get_schedule(if_tomorrow, date, week, what_day)

        if_send = True
        # if self.what_day == 'Sunday':
        #     if_send = False
        #     print('周日不发送')
        if date in ['2020-10-01', '2020-10-02', '2020-10-03']:
            if_send = False
            print('国庆假期')

        if self.grade in preparatory_grades and if_send:
            try:
                if len(self.c0.final_class_ch_name) + len(self.c1.final_class_ch_name) + \
                        len(self.c2.final_class_ch_name) + len(self.c3.final_class_ch_name) + \
                        len(self.c4.final_class_ch_name) == 0:
                    print('今天全天没有课')
                    send_msg_when(self.name, '今天全天没有课',
                                  date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
                    raise Exception('今天全天没课')
                else:
                    print(message0)
                send_msg_when(self.name, message0,
                              date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
                print('student info send ----> done\n')

            except Exception as e:
                print(f'student info send ----> fail\n{e}\n')

        if self.grade in engineer_grades and if_send:
            print(message0)
            send_msg_when(self.name, message0,
                          date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
            print('student info send ----> done\n')


# class ClassFinalInfo:
#     def __init__(self):
#         self.final_class_fr_name = ''
#         self.final_class_ch_name = ''
#         self.final_teacher = ''
#         self.final_classroom = ''
#

# class StudentOld:
#     def __init__(self, name, grade, a_or_b, p_ab_cd, f_ab_cd_e):
#         self.name = name  # 微信备注名
#         self.grade = grade  # 年级
#         self.a_or_b = a_or_b  # 大AB班
#         self.p_ab_cd = p_ab_cd  # td班
#         self.f_ab_cd_e = f_ab_cd_e  # 法语班
#
#         self.schedule_grade = []
#         if grade in [2018, 2019, 2020]:
#             try:
#                 exec('self.schedule_grade = schedule_' + str(grade))
#             except Exception as e:
#                 print('在读取{grade}级课表时出错')
#                 print(e)
#
#         self.c0 = ClassFinalInfo()
#         self.c1 = ClassFinalInfo()
#         self.c2 = ClassFinalInfo()
#         self.c3 = ClassFinalInfo()
#         self.c4 = ClassFinalInfo()
#
#         # 为了新增周末补课的补课判断条件
#         self.week = -1
#         self.what_day = 'Sunday'
#         self.real_what_day = 'Sunday'
#         self.replacement = False
#
#         # 为了避免达到发送阈值
#         if randint(0, 1):
#             self.send_hour = '5'
#             self.send_min = str(randint(30, 59))
#             self.send_sec = str(randint(0, 59))
#         else:
#             self.send_hour = '6'
#             self.send_min = str(randint(0, 30))
#             self.send_sec = str(randint(0, 59))
#
#     def get_schedule(self, date: str, week: int, what_day: str):
#         self.real_what_day = what_day
#         try:
#             # ------------对于周末补课的补课判断条件-------------- #
#             if week == 0 and what_day == 'Sunday':
#                 week = 15
#                 what_day = 'Monday'
#                 self.replacement = True
#             elif week == 1 and what_day == 'Sunday':
#                 week = 15
#                 what_day = 'Tuesday'
#                 self.replacement = True
#             elif week == 2 and what_day == 'Sunday':
#                 week = 15
#                 what_day = 'Wednesday'
#                 self.replacement = True
#             elif week == 3 and what_day == 'Sunday':
#                 week = 15
#                 what_day = 'Thursday'
#                 self.replacement = True
#             elif date == '2020-10-04':
#                 week = 15
#                 what_day = 'Friday'
#                 self.replacement = True
#             elif date == '2020-10-05':
#                 week = 15
#                 what_day = 'Saturday'
#                 self.replacement = True
#             elif date == '2020-10-06':
#                 week = 16
#                 what_day = 'Monday'
#                 self.replacement = True
#             elif date == '2020-10-07':
#                 week = 16
#                 what_day = 'Tuesday'
#                 self.replacement = True
#             elif week == 5 and what_day == 'Sunday':
#                 week = 16
#                 what_day = 'Wednesday'
#                 self.replacement = True
#             elif week == 6 and what_day == 'Sunday':
#                 week = 16
#                 what_day = 'Thursday'
#                 self.replacement = True
#             elif week == 7 and what_day == 'Sunday':
#                 week = 16
#                 what_day = 'Friday'
#                 self.replacement = True
#             elif week == 8 and what_day == 'Sunday':
#                 week = 16
#                 what_day = 'Saturday'
#                 self.replacement = True
#             elif week == 9 and what_day == 'Sunday':
#                 week = 17
#                 what_day = 'Monday'
#                 self.replacement = True
#             elif week == 10 and what_day == 'Sunday':
#                 week = 17
#                 what_day = 'Tuesday'
#                 self.replacement = True
#             elif week == 11 and what_day == 'Sunday':
#                 week = 17
#                 what_day = 'Wednesday'
#                 self.replacement = True
#             elif week == 12 and what_day == 'Sunday':
#                 week = 17
#                 what_day = 'Thursday'
#                 self.replacement = True
#             elif week == 13 and what_day == 'Sunday':
#                 week = 17
#                 what_day = 'Friday'
#                 self.replacement = True
#             elif week == 14 and what_day == 'Sunday':
#                 week = 17
#                 what_day = 'Saturday'
#                 self.replacement = True
#             # ------------对于周末补课的补课判断条件-------------- #
#             self.week = week
#             self.what_day = what_day
#
#             # what_day_num = -1
#             if what_day == 'Monday':
#                 what_day_num = 0
#             elif what_day == 'Tuesday':
#                 what_day_num = 1
#             elif what_day == 'Wednesday':
#                 what_day_num = 2
#             elif what_day == 'Thursday':
#                 what_day_num = 3
#             elif what_day == 'Friday':
#                 what_day_num = 4
#             elif what_day == 'Saturday':
#                 what_day_num = 5
#             elif what_day == 'Sunday':
#                 raise Exception('按照原计划，周日不推送')
#             else:
#                 raise Exception(f"get_schedule时，输入星期格式错误,what_day:{what_day}")
#
#             if self.grade in [2018, 2019, 2020]:
#                 schedule = self.schedule_grade[what_day_num]
#             elif self.grade == 2015:
#                 send_msg_when(self.name, '可点击该链接查看课表:\n' + url_2015 + '\n'
#                                                                       '注:进入网页后显示的图片可能不是当前周的课表\n'
#                                                                       '点击图片左侧切换到上一周，点击图片右侧切换到下一周',
#                               date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
#                 raise Exception('\n普通的课表推送仅限于预科阶段')
#             elif self.grade == 2016:
#                 send_msg_when(self.name, '可点击该链接查看课表:\n' + url_2016 + '\n'
#                                                                       '注:进入网页后显示的图片可能不是当前周的课表\n'
#                                                                       '点击图片左侧切换到上一周，点击图片右侧切换到下一周',
#                               date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
#                 raise Exception('\n普通的课表推送仅限于预科阶段')
#             elif self.grade == 2017:
#                 send_msg_when(self.name, '可点击该链接查看课表:\n' + url_2017 + '\n'
#                                                                       '注:进入网页后显示的图片可能不是当前周的课表\n'
#                                                                       '点击图片左侧切换到上一周，点击图片右侧切换到下一周',
#                               date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
#                 raise Exception('\n普通的课表推送仅限于预科阶段')
#             else:
#                 raise Exception('\n普通的课表推送仅限于预科阶段')
#
#             # 对schedule_ls的final系列的初始化
#             for i in range(5):
#                 schedule[i].final_class_fr_name = ''
#                 schedule[i].final_class_ch_name = ''
#                 schedule[i].final_teacher = ''
#                 schedule[i].final_classroom = ''
#
#             for i in range(5):  # 第i节课
#                 if len(schedule[i].class_property) == 0:
#                     print(f'{self.name}:今天第{(i + 1) * 2 - 1},{(i + 1) * 2}没课')
#
#                 else:
#                     if schedule[i].class_property:
#                         for final_index in range(len(schedule[i].class_property)):
#                             if schedule[i].class_property[final_index] == 'all':
#                                 if week in schedule[i].correspond_week[final_index]:
#                                     try:
#                                         if schedule[i].class_fr_name_ls:
#                                             schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
#                                         if schedule[i].class_ch_name_ls:
#                                             schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
#                                         if schedule[i].teacher_ls:
#                                             schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
#                                         if schedule[i].classroom_ls:
#                                             schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
#                                     except Exception as e:
#                                         print(f'在处理{self.name}的第({i})节课时出错,{e}')
#
#                             elif schedule[i].class_property[final_index] == 'AB':
#                                 if self.a_or_b == schedule[i].correspond_class[final_index]:
#                                     if week in schedule[i].correspond_week[final_index]:
#                                         try:
#                                             if schedule[i].class_fr_name_ls:
#                                                 schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[
#                                                     final_index]
#                                             if schedule[i].class_ch_name_ls:
#                                                 schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[
#                                                     final_index]
#                                             if schedule[i].teacher_ls:
#                                                 schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
#                                             if schedule[i].classroom_ls:
#                                                 schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
#                                         except Exception as e:
#                                             print(f'在处理{self.name}的第({i})节课时出错,{e}')
#
#                             elif schedule[i].class_property[final_index] == 'P':
#                                 if self.p_ab_cd == schedule[i].correspond_class[final_index]:
#                                     if week in schedule[i].correspond_week[final_index]:
#                                         try:
#                                             if schedule[i].class_fr_name_ls:
#                                                 schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[
#                                                     final_index]
#                                             if schedule[i].class_ch_name_ls:
#                                                 schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[
#                                                     final_index]
#                                             if schedule[i].teacher_ls:
#                                                 schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
#                                             if schedule[i].classroom_ls:
#                                                 schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
#                                         except Exception as e:
#                                             print(f'在处理{self.name}的第({i})节课时出错,{e}')
#
#                             elif schedule[i].class_property[final_index] == 'F':
#                                 if self.f_ab_cd_e == schedule[i].correspond_class[final_index]:
#                                     if week in schedule[i].correspond_week[final_index]:
#                                         try:
#                                             if schedule[i].class_fr_name_ls:
#                                                 schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[
#                                                     final_index]
#                                             if schedule[i].class_ch_name_ls:
#                                                 schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[
#                                                     final_index]
#                                             if schedule[i].teacher_ls:
#                                                 schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
#                                             if schedule[i].classroom_ls:
#                                                 schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
#                                         except Exception as e:
#                                             print(f'在处理{self.name}的第({i})节课时出错,{e}')
#
#                         exec("self.c" + str(i) + ".final_class_fr_name = schedule[i].final_class_fr_name")
#                         exec("self.c" + str(i) + ".final_class_ch_name = schedule[i].final_class_ch_name")
#                         exec("self.c" + str(i) + ".final_teacher = schedule[i].final_teacher")
#                         exec("self.c" + str(i) + ".final_classroom = schedule[i].final_classroom")
#
#         except Exception as e:
#             print(e)
#
#     def send_weather(self, week: int, date: str):
#         try:
#             # 发送天气
#             print('-' * 9, '↓', self.name, '↓', '-' * 10)
#             # 6:30通报全天有哪些课，以及第一节课的详细信息
#             weather = get_weather()
#             if week == -1:
#                 message_weather = '今天是' + date + '，新学期即将开始\n' + weather
#             else:
#                 if not self.replacement:
#                     message_weather = '今天是' + date + '，这周是本学期的第' + str(week + 1) + '周\n' + weather
#                 else:
#                     message_weather = '今天是' + date + '，这周是本学期的第' + str(week + 1) + '周，今天补的是第' + str(
#                         self.week + 1) + '周' + self.what_day + '的课\n' + weather
#             print(message_weather)
#             send_msg_when(self.name, message_weather,
#                           date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
#         except Exception as e:
#             print("发送天气时出错")
#             print(e)
#
#     def send_schedule(self, date: str):
#         if self.grade in [2018, 2019, 2020]:
#             try:
#                 if self.what_day == 'Sunday':
#                     raise Exception('按照原计划，周日不推送')
#
#                 message0 = '今天的课程表:'
#                 class_ls = [self.c0, self.c1, self.c2, self.c3, self.c4]
#                 for i in range(5):
#                     if class_ls[i].final_class_ch_name != '':
#                         if class_ls[i].final_classroom != '':
#                             if class_ls[i].final_teacher != '':
#                                 message0 = message0 + '\n' + f'第{str(2 * (i + 1) - 1)},{str(2 * (i + 1))}节课是{class_ls[i].final_teacher}老师的{class_ls[i].final_class_ch_name}，地点:{class_ls[i].final_classroom}'
#                             else:
#                                 message0 = message0 + '\n' + f'第{str(2 * (i + 1) - 1)},{str(2 * (i + 1))}节课是{class_ls[i].final_class_ch_name}，地点:{class_ls[i].final_classroom}'
#                         else:
#                             if class_ls[i].final_teacher != '':
#                                 message0 = message0 + '\n' + f'第{str(2 * (i + 1) - 1)},{str(2 * (i + 1))}节课是{class_ls[i].final_teacher}老师的{class_ls[i].final_class_ch_name}'
#                             else:
#                                 message0 = message0 + '\n' + f'第{str(2 * (i + 1) - 1)},{str(2 * (i + 1))}节课是{class_ls[i].final_class_ch_name}'
#                     elif i == 4:
#                         pass  # 如果晚上没课，则不显示第五条
#                     else:
#                         message0 = message0 + '\n' + f'第{str(2 * (i + 1) - 1)},{str(2 * (i + 1))}节课没课'
#                 if len(self.c0.final_class_ch_name) + len(self.c1.final_class_ch_name) + \
#                         len(self.c2.final_class_ch_name) + len(self.c3.final_class_ch_name) + \
#                         len(self.c4.final_class_ch_name) == 0:
#                     print('今天全天没有课')
#                     send_msg_when(self.name, '今天全天没有课',
#                                   date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
#                     raise Exception('今天全天没课')
#                 else:
#                     print(message0)
#
#                 # if self.c0.final_class_ch_name:
#                 #     message1 = f'第1,2节课是{self.c0.final_teacher}老师的{self.c0.final_class_ch_name}，地点:{self.c0.final_classroom}'
#                 #     print(message1)
#                 #     send_msg_when(self.name, message0 + '\n\n' + message1,
#                 #                   date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
#                 # else:
#                 #     send_msg_when(self.name, message0,
#                 #                   date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
#                 #
#                 # if class_ls[1].final_class_ch_name:
#                 #     message2 = f'第3,4节课是{self.c1.final_teacher}老师的{self.c1.final_class_ch_name}，地点:{self.c1.final_classroom}'
#                 #     print(message2)
#                 #     send_msg_when(self.name, message2, date + ' 09:35:' + self.send_sec)
#                 #
#                 # if class_ls[2].final_class_ch_name:
#                 #     message3 = f'第5,6节课是{self.c2.final_teacher}老师的{self.c2.final_class_ch_name}，地点:{self.c2.final_classroom}'
#                 #     print(message3)
#                 #     send_msg_when(self.name, message3, date + ' 11:40:' + self.send_sec)
#                 #
#                 # if class_ls[3].final_class_ch_name:
#                 #     message4 = f'第7,8节课是{self.c3.final_teacher}老师的{self.c3.final_class_ch_name}，地点:{self.c3.final_classroom}'
#                 #     print(message4)
#                 #     send_msg_when(self.name, message4, date + ' 15:05:' + self.send_sec)
#                 #
#                 # if class_ls[4].final_class_ch_name:
#                 #     message5 = f'别忘了晚上还有一节课哟，第9,10节课是{self.c4.final_teacher}老师的{self.c4.final_class_ch_name}，地点:{self.c4.final_classroom}'
#                 #     print(message5)
#                 #     send_msg_when(self.name, message5, date + ' 17:10:' + self.send_sec)
#
#                 send_msg_when(self.name, message0,
#                               date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec)
#                 print('student info send ----> done\n')
#
#             except Exception as e:
#                 print(f'student info send ----> fail\n{e}\n')
#
#     def test_send(self, date: str, send_time: str):
#         send_msg_when(self.name, '测试', date + ' ' + send_time)


# ----------------------------------------------------------------- #
# ----------------------------------------------------------------- #
# ----------------------------------------------------------------- #


if __name__ == "__main__":
    # student2 = Student('张三', 2019, 'A', 'PA', 'PA')
    # student1 = Student('张三', 2019, 'B', 'PC', 'PC')
    # # student2.get_schedule(14, 'Friday')
    # # student1.get_schedule(14, 'Friday')
    # raise Exception('test')
    pass
