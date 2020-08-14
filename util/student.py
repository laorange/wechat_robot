# from util.excel2class_schedule import Class

from schedule.schedule2017 import schedule_2017
# from schedule.schedule2018 import schedule_2018
from schedule.schedule2019 import schedule_2019
# from schedule.schedule2020 import schedule_2020

from util.basic_wxpy import send_msg_when
from util.weather import weather

from util.week import week, what_day, date


class ClassFinalInfo:
    def __init__(self):
        self.final_class_fr_name = ''
        self.final_class_ch_name = ''
        self.final_teacher = ''
        self.final_classroom = ''


class Student:
    def __init__(self, name, grade, a_or_b, p_ab_cd, f_ab_cd_e):
        self.name = name  # 微信备注名
        self.grade = grade  # 年级
        self.a_or_b = a_or_b  # 大AB班
        self.p_ab_cd = p_ab_cd  # td班
        self.f_ab_cd_e = f_ab_cd_e  # 法语班

        self.schedule_grade = []
        exec('self.schedule_grade = schedule_' + str(grade))

        self.c0 = ClassFinalInfo()
        self.c1 = ClassFinalInfo()
        self.c2 = ClassFinalInfo()
        self.c3 = ClassFinalInfo()
        self.c4 = ClassFinalInfo()

    def get_schedule(self):
        if what_day == 'Monday':
            what_day_num = 0
        elif what_day == 'Tuesday':
            what_day_num = 1
        elif what_day == 'Wednesday':
            what_day_num = 2
        elif what_day == 'Thursday':
            what_day_num = 3
        elif what_day == 'Friday':
            what_day_num = 4
        elif what_day == 'Saturday':
            pass
        elif what_day == 'Sunday':
            pass
        schedule = self.schedule_grade[what_day_num]

        for i in range(5):  # 第i节课
            if len(schedule[i].class_property) == 0:
                print('这节没课')

            else:
                for final_index in range(len(schedule[i].class_property)):
                    if schedule[i].class_property[final_index] == 'all':
                        if week in schedule[i].correspond_week[final_index]:
                            try:
                                if schedule[i].class_fr_name_ls:
                                    schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                                if schedule[i].class_ch_name_ls:
                                    schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                                if schedule[i].teacher_ls:
                                    schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                if schedule[i].classroom_ls:
                                    schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
                            except Exception as e:
                                print(f'在处理{self.name}的第({i})节课时出错,{e}')

                    elif schedule[i].class_property[final_index] == 'AB':
                        if self.a_or_b == schedule[i].correspond_class[final_index]:
                            if week in schedule[i].correspond_week[final_index]:
                                try:
                                    if schedule[i].class_fr_name_ls:
                                        schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                                    if schedule[i].class_ch_name_ls:
                                        schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                                    if schedule[i].teacher_ls:
                                        schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                    if schedule[i].classroom_ls:
                                        schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
                                except Exception as e:
                                    print(f'在处理{self.name}的第({i})节课时出错,{e}')

                    elif schedule[i].class_property[final_index] == 'P':
                        if self.p_ab_cd == schedule[i].correspond_class[final_index]:
                            if week in schedule[i].correspond_week[final_index]:
                                try:
                                    if schedule[i].class_fr_name_ls:
                                        schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                                    if schedule[i].class_ch_name_ls:
                                        schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                                    if schedule[i].teacher_ls:
                                        schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                    if schedule[i].classroom_ls:
                                        schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
                                except Exception as e:
                                    print(f'在处理{self.name}的第({i})节课时出错,{e}')

                    elif schedule[i].class_property[final_index] == 'F':
                        if self.f_ab_cd_e == schedule[i].correspond_class[final_index]:
                            if week in schedule[i].correspond_week[final_index]:
                                try:
                                    if schedule[i].class_fr_name_ls:
                                        schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                                    if schedule[i].class_ch_name_ls:
                                        schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                                    if schedule[i].teacher_ls:
                                        schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                    if schedule[i].classroom_ls:
                                        schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
                                except Exception as e:
                                    print(f'在处理{self.name}的第({i})节课时出错,{e}')

                exec("self.c" + str(i) + ".final_class_fr_name = schedule[i].final_class_fr_name")
                exec("self.c" + str(i) + ".final_class_ch_name = schedule[i].final_class_ch_name")
                exec("self.c" + str(i) + ".final_teacher = schedule[i].final_teacher")
                exec("self.c" + str(i) + ".final_classroom = schedule[i].final_classroom")

    def send(self):
        try:
            # 7:00通报全天有哪些课，以及第一节课的详细信息
            message_weather = '今天是' + date + '\n' + weather + '\n'

            message0 = '今天的课程表:\n'
            class_ls = [self.c0, self.c1, self.c2, self.c3, self.c4]
            for i in range(5):
                if class_ls[i].final_class_ch_name != '':
                    message0 = message0 + class_ls[i].final_class_ch_name + ', 地点:' + class_ls[i].final_classroom + '\n'
            if message0 == '今天的课程表:\n':
                send_msg_when(self.name, message_weather + '今天全天没有课', date + ' 07:00:00')
                print(self.name, '今天全天没有课')
                raise Exception('今天全天没课')
            else:
                send_msg_when(self.name, message_weather + message0, date + ' 07:00:00')
                print(self.name, message0)

            if self.c0.final_class_ch_name:
                message1 = f'第1,2节课是{self.c0.final_teacher}的{self.c0.final_class_ch_name},地点:{self.c0.final_classroom}'
                send_msg_when(self.name, message1, date + ' 07:00:15')
                print(self.name, message1)

            if class_ls[1].final_class_ch_name:
                message2 = f'第3,4节课是{self.c1.final_teacher}的{self.c1.final_class_ch_name},地点:{self.c1.final_classroom}'
                send_msg_when(self.name, message2, date + ' 09:35:00')
                print(self.name, message2)

            if class_ls[2].final_class_ch_name:
                message3 = f'第5,6节课是{self.c2.final_teacher}的{self.c2.final_class_ch_name},地点:{self.c2.final_classroom}'
                send_msg_when(self.name, message3, date + ' 12:40:00')
                print(self.name, message3)

            if class_ls[3].final_class_ch_name:
                message4 = f'第7,8节课是{self.c3.final_teacher}的{self.c3.final_class_ch_name},地点:{self.c3.final_classroom}'
                send_msg_when(self.name, message4, date + ' 15:05:00')
                print(self.name, message4)

            if class_ls[4].final_class_ch_name:
                message5 = f'别忘了晚上还有一节课哟,第9,10节课是{self.c4.final_teacher}的{self.c4.final_class_ch_name},地点:{self.c4.final_classroom}'
                send_msg_when(self.name, message5, date + ' 17:10:00')
                print(self.name, message5)

        except Exception as e:
            print(e)
