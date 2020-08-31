# from schedule.schedule2017 import schedule_2017
from schedule.schedule2018 import schedule_2018
from schedule.schedule2019 import schedule_2019
# from schedule.schedule2020 import schedule_2020

# from wechat_func import send_msg_when
from util.weather import get_weather


class ClassFinalInfo:
    def __init__(self):
        self.final_class_fr_name = ''
        self.final_class_ch_name = ''
        self.final_teacher = ''
        self.final_classroom = ''


class StudentNoWechat:
    def __init__(self, name, grade, a_or_b, p_ab_cd, f_ab_cd_e):
        self.name = name  # 微信备注名
        self.grade = grade  # 年级
        self.a_or_b = a_or_b  # 大AB班
        self.p_ab_cd = p_ab_cd  # td班
        self.f_ab_cd_e = f_ab_cd_e  # 法语班

        self.schedule_grade = []
        if grade in ['2018', '2019', '2020']:
            try:
                exec('self.schedule_grade = schedule_' + str(grade))
            except Exception as e:
                print('在读取{grade}级课表时出错')
                print(e)

        self.c0 = ClassFinalInfo()
        self.c1 = ClassFinalInfo()
        self.c2 = ClassFinalInfo()
        self.c3 = ClassFinalInfo()
        self.c4 = ClassFinalInfo()

    def get_schedule(self, if_tomorrow: bool, week: int, what_day: str):
        if if_tomorrow:
            valid_what_day_ls = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            total_what_day_ls = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            if what_day in valid_what_day_ls:
                today_index = valid_what_day_ls.index(what_day)
                what_day = total_what_day_ls[today_index + 2]
            elif what_day == 'Sunday':
                week += 1
                what_day = 'Monday'
            elif what_day == 'Saturday':
                return '明天是星期天，当前数据未记录周日的课表信息'
            else:
                raise Exception('what_day输入错误')

        what_day_num = -1
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
            what_day_num = 5
        elif what_day == 'Sunday':
            pass
        else:
            raise Exception(f"get_schedule时，输入星期格式错误,what_day:{what_day}")
        schedule = self.schedule_grade[what_day_num]

        for i in range(5):  # 第i节课
            if len(schedule[i].class_property) == 0:
                print(f'{self.name}:今天第{(i + 1) * 2 - 1},{(i + 1) * 2}没课')

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

    def return_tomorrow_schedule(self):
        if self.grade in ['2018', '2019', '2020']:
            try:
                message0 = '明天的课程表:'
                class_ls = [self.c0, self.c1, self.c2, self.c3, self.c4]
                for i in range(5):
                    if class_ls[i].final_class_ch_name != '':
                        if class_ls[i].final_classroom != '':
                            message0 = message0 + '\n' + str(i + 1) + '. ' + class_ls[i].final_class_ch_name + '，地点:' + class_ls[i].final_classroom
                        else:
                            message0 = message0 + '\n' + str(i + 1) + '. ' + class_ls[i].final_class_ch_name
                    elif i == 4:
                        pass  # 如果晚上没课，则不显示第五条
                    else:
                        message0 = message0 + '\n' + str(i + 1) + '. '
                if len(self.c0.final_class_ch_name) + len(self.c1.final_class_ch_name) + len(self.c2.final_class_ch_name) + len(self.c3.final_class_ch_name) + len(self.c4.final_class_ch_name) == 0:
                    print('student tomorrow info send ----> None')
                    message0 = '明天全天没有课'
                return message0

            except Exception as e:
                print(f'student tomorrow info send ----> fail\n{e}\n')
