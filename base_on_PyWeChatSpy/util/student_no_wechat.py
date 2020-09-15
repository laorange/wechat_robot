from schedule.schedule2018 import schedule_2018
from schedule.schedule2019 import schedule_2019
# from schedule.schedule2020 import schedule_2020

# from wechat_func import send_msg_when
from util.weather import get_weather

url_2017 = 'solars.top/kb/17/S1/'
url_2016 = 'solars.top/kb/16/S3/'
url_2015 = 'solars.top/kb/15/S5/'

preparatory_grades = [2018, 2019, 2020]
engineer_grades = [2017, 2016, 2015]
url_engineer_grades = [url_2017, url_2016, url_2015]


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
        if grade in [2018, 2019, 2020]:
            try:
                exec('self.schedule_grade = schedule_' + str(grade))
            except Exception as e:
                print(f'在读取{grade}级课表时出错')
                print(e)

        self.c0 = ClassFinalInfo()
        self.c1 = ClassFinalInfo()
        self.c2 = ClassFinalInfo()
        self.c3 = ClassFinalInfo()
        self.c4 = ClassFinalInfo()

        self.if_tomorrow = False

        # 为了新增周末补课的补课判断条件
        self.week = -1
        self.what_day = 'Sunday'
        self.replacement = False

    def get_schedule(self, if_tomorrow: bool, date: str, week: int, what_day: str):
        self.if_tomorrow = if_tomorrow
        try:
            if self.if_tomorrow:
                valid_what_day_ls = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
                total_what_day_ls = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
                if what_day in valid_what_day_ls:
                    today_index = valid_what_day_ls.index(what_day)
                    what_day = total_what_day_ls[today_index + 2]
                elif what_day == 'Sunday':
                    week += 1
                    what_day = 'Monday'
                elif what_day == 'Saturday':
                    what_day = 'Sunday'
                else:
                    raise Exception('what_day输入错误')

            # ------------对于周末补课的补课判断条件-------------- #
            if week == 0 and what_day == 'Sunday':
                week = 15
                what_day = 'Monday'
                self.replacement = True
            elif week == 1 and what_day == 'Sunday':
                week = 15
                what_day = 'Tuesday'
                self.replacement = True
            elif week == 2 and what_day == 'Sunday':
                week = 15
                what_day = 'Wednesday'
                self.replacement = True
            elif week == 3 and what_day == 'Sunday':
                week = 15
                what_day = 'Thursday'
                self.replacement = True
            elif week == 5 and what_day == 'Sunday':
                week = 16
                what_day = 'Wednesday'
                self.replacement = True
            elif week == 6 and what_day == 'Sunday':
                week = 16
                what_day = 'Thursday'
                self.replacement = True
            elif week == 7 and what_day == 'Sunday':
                week = 16
                what_day = 'Friday'
                self.replacement = True
            elif week == 8 and what_day == 'Sunday':
                week = 16
                what_day = 'Saturday'
                self.replacement = True
            elif week == 9 and what_day == 'Sunday':
                week = 17
                what_day = 'Monday'
                self.replacement = True
            elif week == 10 and what_day == 'Sunday':
                week = 17
                what_day = 'Tuesday'
                self.replacement = True
            elif week == 11 and what_day == 'Sunday':
                week = 17
                what_day = 'Wednesday'
                self.replacement = True
            elif week == 12 and what_day == 'Sunday':
                week = 17
                what_day = 'Thursday'
                c = True
            elif week == 13 and what_day == 'Sunday':
                week = 17
                what_day = 'Friday'
                self.replacement = True
            elif week == 14 and what_day == 'Sunday':
                week = 17
                what_day = 'Saturday'
                self.replacement = True
            if if_tomorrow:
                if date == '2020-10-03':
                    week = 15
                    what_day = 'Friday'
                    self.replacement = True
                elif date == '2020-10-04':
                    week = 15
                    what_day = 'Saturday'
                    self.replacement = True
                elif date == '2020-10-05':
                    week = 16
                    what_day = 'Monday'
                    self.replacement = True
                elif date == '2020-10-06':
                    week = 16
                    what_day = 'Tuesday'
                    self.replacement = True
            else:
                if date == '2020-10-04':
                    week = 15
                    what_day = 'Friday'
                    self.replacement = True
                elif date == '2020-10-05':
                    week = 15
                    what_day = 'Saturday'
                    self.replacement = True
                elif date == '2020-10-06':
                    week = 16
                    what_day = 'Monday'
                    self.replacement = True
                elif date == '2020-10-07':
                    week = 16
                    what_day = 'Tuesday'
                    self.replacement = True
            # ------------对于周末补课的补课判断条件-------------- #
            self.week = week
            self.what_day = what_day

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

            # 工程师阶段
            if self.grade in preparatory_grades:
                schedule = self.schedule_grade[what_day_num]
            elif self.grade in engineer_grades:
                message0 = url_engineer_grades[engineer_grades.index(self.grade)]
                if self.week < 17 and self.what_day == 'Monday' and if_tomorrow:
                    message0 = '可点击该链接查看课表:\n' + message0 + '?p=' + str(self.week + 3)
                else:
                    message0 = '可点击该链接查看课表:\n' + message0
                return message0
            else:
                raise Exception('不属于适用年级')

            # 对schedule_ls的final系列的初始化
            for i in range(5):
                schedule[i].final_class_fr_name = ''
                schedule[i].final_class_ch_name = ''
                schedule[i].final_teacher = ''
                schedule[i].final_classroom = ''

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

        except Exception as e:
            print(e)

        # def return_tomorrow_schedule(self):
        if self.grade in [2018, 2019, 2020]:
            try:
                message0 = '明天的课程表:' if self.if_tomorrow else '今天的课程表:'
                if self.replacement:
                    if self.if_tomorrow:
                        message0 = '明天补的是第' + str(self.week + 1) + '周' + self.what_day + '的课:'
                    else:
                        message0 = '今天补的是第' + str(self.week + 1) + '周' + self.what_day + '的课:'

                class_ls = [self.c0, self.c1, self.c2, self.c3, self.c4]
                for i in range(5):
                    if class_ls[i].final_class_ch_name != '':
                        if class_ls[i].final_classroom != '':
                            if class_ls[i].final_teacher != '':
                                message0 = message0 + '\n\n' + f'第{str(2 * (i + 1) - 1)},{str(2 * (i + 1))}节课是{class_ls[i].final_teacher}老师的{class_ls[i].final_class_ch_name}，地点:{class_ls[i].final_classroom}'
                            else:
                                message0 = message0 + '\n\n' + f'第{str(2 * (i + 1) - 1)},{str(2 * (i + 1))}节课是{class_ls[i].final_class_ch_name}，地点:{class_ls[i].final_classroom}'
                        else:
                            if class_ls[i].final_teacher != '':
                                message0 = message0 + '\n\n' + f'第{str(2 * (i + 1) - 1)},{str(2 * (i + 1))}节课是{class_ls[i].final_teacher}老师的{class_ls[i].final_class_ch_name}'
                            else:
                                message0 = message0 + '\n\n' + f'第{str(2 * (i + 1) - 1)},{str(2 * (i + 1))}节课是{class_ls[i].final_class_ch_name}'
                    elif i == 4:
                        pass  # 如果晚上没课，则不显示第五条
                    else:
                        message0 = message0 + '\n\n' + f'第{str(2 * (i + 1) - 1)},{str(2 * (i + 1))}节课没课'
                if len(self.c0.final_class_ch_name) + len(self.c1.final_class_ch_name) + len(
                        self.c2.final_class_ch_name) + len(self.c3.final_class_ch_name) + len(
                    self.c4.final_class_ch_name) == 0:
                    print('student tomorrow info send ----> None')
                    if if_tomorrow:
                        message0 = '明天全天没有课'
                    else:
                        message0 = '今天全天没有课'
                return message0

            except Exception as e:
                print(f'student tomorrow info send ----> fail\n{e}\n')
