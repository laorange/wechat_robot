from excel2class_schedule import Class

from schedule2017 import schedule_2017
# from schedule2018 import schedule_2018
from schedule2019 import schedule_2019
# from schedule2020 import schedule_2020

from basic_wxpy import send_msg_when

import time

time


class ClassFinalInfo:
    def __init__(self):
        self.final_class_fr_name = ''
        self.final_class_ch_name = ''
        self.final_teacher = ''
        self.final_classroom = ''


class Student:
    def __init__(self, name, grade, a_or_b, p_ab_cd, f_ab_cd_e):
        self.name = name # 微信备注名
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

    def get_schedule(self, week, what_day):
        if what_day == 'Monday':
            week_num = 0
        if what_day == 'Tuesday':
            week_num = 1
        if what_day == 'Wednesday':
            week_num = 2
        if what_day == 'Thursday':
            week_num = 3
        if what_day == 'Friday':
            week_num = 4
        if what_day == 'Saturday':
            pass
        if what_day == 'Sunday':
            pass
        schedule = self.schedule_grade[week_num]
        
        for i in range(5):  # 第i节课
            if len(schedule[i].class_property) == 0:
                print('这节没课')
    
            else:
                for final_index in range(len(schedule[i].class_property)):
                    if schedule[i].class_property[final_index] == 'all':
                        if week in schedule[i].correspond_week[final_index]:
                            schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                            schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                            schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                            schedule[i].final_classroom = schedule[i].classroom_ls[final_index]

                    elif schedule[i].class_property[final_index] == 'AB':
                        if self.a_or_b == schedule[i].correspond_class[final_index]:
                            if week in schedule[i].correspond_week[final_index]:
                                schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                                schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                                schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                schedule[i].final_classroom = schedule[i].classroom_ls[final_index]

                    elif schedule[i].class_property[final_index] == 'P':
                        if self.p_ab_cd == schedule[i].correspond_class[final_index]:
                            if week in schedule[i].correspond_week[final_index]:
                                schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                                schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                                schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                schedule[i].final_classroom = schedule[i].classroom_ls[final_index]

                    elif schedule[i].class_property[final_index] == 'F':
                        if self.f_ab_cd_e == schedule[i].correspond_class[final_index]:
                            if week in schedule[i].correspond_week[final_index]:
                                schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                                schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                                schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                schedule[i].final_classroom = schedule[i].classroom_ls[final_index]

                exec("self.c"+str(i)+".final_class_fr_name = schedule[i].final_class_fr_name")
                exec("self.c"+str(i)+".final_class_ch_name = schedule[i].final_class_ch_name")
                exec("self.c"+str(i)+".final_teacher = schedule[i].final_teacher")
                exec("self.c"+str(i)+".final_classroom = schedule[i].final_classroom")

    # def send(self):
    #     # 7:00通报全天有哪些课，以及第一节课的详细信息
    #     message0 = '今天是'
    #     self.c0 =
    #     self.c1 =
    #     self.c2 =
    #     self.c3 =
    #     self.c4 =





    # def __call__(self, week, what_day, class_num):
    #     schedule = get_today_schedule(self.grade, what_day)
    #     print(schedule)
    #     target_class = schedule[class_num]
    #     target_class.determine_finally(self.grade, self.a_or_b, self.p_ab_cd, self.f_ab_cd_e, week, what_day, class_num)
    # 
    #     if target_class.class_property is None:
    #         print('这节没课哟')
    #         return '', '', ''
    #     else:
    #         print('这节课是{}的{},地点在:{}'.format(target_class.final_teacher,
    #                                         target_class.final_class_ch_name,
    #                                         target_class.final_classroom))
    #         return target_class.final_teacher, target_class.final_class_ch_name, target_class.final_classroom
    # 
    # # return get_class(self.grade, self.a_or_b, self.p_ab_cd, self.f_ab_cd_e, week, what_day, class_num)
