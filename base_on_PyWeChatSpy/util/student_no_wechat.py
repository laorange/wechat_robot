from schedule.schedule18 import schedule_18
from schedule.schedule19 import schedule_19
from schedule.schedule20 import schedule_20

# from wechat_func import send_msg_when
from util.weather import get_weather

url_17 = 'kb.solars.top/17/S1/'
url_2016 = 'kb.solars.top/16/S3/'
url_2015 = 'kb.solars.top/15/S5/'

url_schedule_18 = 'laorange.top/img/18.png'
url_schedule_19 = 'laorange.top/img/19.png'
url_schedule_20 = 'laorange.top/img/20.jpg'
# url_schedule_preparatory_grades = [url_schedule_18, url_schedule_19, url_schedule_20]
url_19_td1 = 'laorange.top/img/19td1.png'
url_19_td2 = 'laorange.top/img/19td2.png'
# 手动改改吧...
url_19_td = url_19_td1 + '\n' + url_19_td2

preparatory_grades = [18, 19, 20]
engineer_grades = [17, 16, 15]
url_engineer_grades = [url_17, url_2016, url_2015]


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

        # 通知
        self.inform_msg = ''  # "\n\n※注:solars.top服务器类型是限制流量的，还请大家需时查看，请勿频繁刷新"

        self.schedule_grade = []
        if grade in preparatory_grades:
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

        self.situation = ''

        # 为了新增周末补课的补课判断条件
        self.week = -1
        self.what_day = 'Sunday'
        self.what_day_real = 'Sunday'
        self.replacement = False

    def get_schedule(self, situation: str, date: str, week: int, what_day: str):
        self.situation = situation
        self.what_day_real = what_day
        try:
            # if self.situation == '明天':
            #     valid_what_day_ls = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            #     total_what_day_ls = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
            #     if what_day in valid_what_day_ls:
            #         today_index = valid_what_day_ls.index(what_day)
            #         what_day = total_what_day_ls[today_index + 2]
            #     elif what_day == 'Sunday':
            #         week += 1
            #         what_day = 'Monday'
            #     elif what_day == 'Saturday':
            #         what_day = 'Sunday'
            #     else:
            #         raise Exception('what_day输入错误')

            # ------------对于周末补课的补课判断条件-------------- #
            if week == 5 and what_day == 'Sunday':
                week = 16
                what_day = 'Thursday'
                self.replacement = True
            elif week == 6 and what_day == 'Sunday':
                week = 15
                what_day = 'Monday'
                self.replacement = True
            elif week == 7 and what_day == 'Sunday':
                week = 15
                what_day = 'Wednesday'
                self.replacement = True
            elif week == 8 and what_day == 'Sunday':
                week = 15
                what_day = 'Thursday'
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
                self.replacement = True
            elif week == 13 and what_day == 'Sunday':
                week = 17
                what_day = 'Friday'
                self.replacement = True
            # elif week == 14 and what_day == 'Sunday':
            #     week = 17
            #     what_day = 'Saturday'
            #     self.replacement = True

            # if if_tomorrow:
            #     if date == '2020-10-03':
            #         week = 15
            #         what_day = 'Friday'
            #         self.replacement = True
            #     elif date == '2020-10-04':
            #         week = 16
            #         what_day = 'Friday'
            #         self.replacement = True
            #     elif date == '2020-10-05':
            #         week = 16
            #         what_day = 'Monday'
            #         self.replacement = True
            #     elif date == '2020-10-06':
            #         week = 16
            #         what_day = 'Tuesday'
            #         self.replacement = True
            #     elif date == '2020-10-07':
            #         week = 16
            #         what_day = 'Wednesday'
            #         self.replacement = True
            # else:

            if date == '2020-10-04':
                week = 15
                what_day = 'Friday'
                self.replacement = True
            elif date == '2020-10-05':
                week = 16
                what_day = 'Friday'
                self.replacement = True
            elif date == '2020-10-06':
                week = 16
                what_day = 'Monday'
                self.replacement = True
            elif date == '2020-10-07':
                week = 16
                what_day = 'Tuesday'
                self.replacement = True
            elif date == '2020-10-08':
                week = 16
                what_day = 'Wednesday'
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

            # 预科阶段
            if self.grade in preparatory_grades and what_day_num >= 0:
                schedule = self.schedule_grade[what_day_num]
            # 工程师阶段
            elif self.grade in engineer_grades:
                message0 = url_engineer_grades[engineer_grades.index(self.grade)]
                if self.week < 17 and self.situation != '今天':
                    message0 = '可点击该链接查看课表:\n' + message0 + '?p=' + str(week + 3)
                else:
                    message0 = '可点击该链接查看课表:\n' + message0
                message0 = message0 + self.inform_msg
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
                    print(f'{self.name}:{self.situation}第{(i + 1) * 2 - 1},{(i + 1) * 2}没课')

                else:
                    for final_index in range(len(schedule[i].class_property)):
                        if schedule[i].class_property[final_index] == 'all':
                            if week in schedule[i].correspond_week[final_index]:
                                try:
                                    if len(schedule[i].class_fr_name_ls) > final_index:
                                        schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                                    if len(schedule[i].class_ch_name_ls) > final_index:
                                        schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                                    if len(schedule[i].teacher_ls) > final_index:
                                        schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                    if len(schedule[i].classroom_ls) > final_index:
                                        schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
                                except Exception as e:
                                    print(f'在处理{self.name}的第({i})节课时出错,{e}')

                        elif schedule[i].class_property[final_index] == 'AB':
                            if self.a_or_b == schedule[i].correspond_class[final_index]:
                                if week in schedule[i].correspond_week[final_index]:
                                    try:
                                        if len(schedule[i].class_fr_name_ls) > final_index:
                                            schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                                        if len(schedule[i].class_ch_name_ls) > final_index:
                                            schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                                        if len(schedule[i].teacher_ls) > final_index:
                                            schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                        if len(schedule[i].classroom_ls) > final_index:
                                            schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
                                    except Exception as e:
                                        print(f'在处理{self.name}的第({i})节课时出错,{e}')

                        elif schedule[i].class_property[final_index] == 'P':
                            if self.p_ab_cd == schedule[i].correspond_class[final_index]:
                                if week in schedule[i].correspond_week[final_index]:
                                    try:
                                        if len(schedule[i].class_fr_name_ls) > final_index:
                                            schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                                        if len(schedule[i].class_ch_name_ls) > final_index:
                                            schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                                        if len(schedule[i].teacher_ls) > final_index:
                                            schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                        if len(schedule[i].classroom_ls) > final_index:
                                            schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
                                    except Exception as e:
                                        print(f'在处理{self.name}的第({i})节课时出错,{e}')

                        elif schedule[i].class_property[final_index] == 'F':
                            if self.f_ab_cd_e == schedule[i].correspond_class[final_index]:
                                if week in schedule[i].correspond_week[final_index]:
                                    try:
                                        if len(schedule[i].class_fr_name_ls) > final_index:
                                            schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[final_index]
                                        if len(schedule[i].class_ch_name_ls) > final_index:
                                            schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[final_index]
                                        if len(schedule[i].teacher_ls) > final_index:
                                            schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                        if len(schedule[i].classroom_ls) > final_index:
                                            schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
                                    except Exception as e:
                                        print(f'在处理{self.name}的第({i})节课时出错,{e}')

                    exec("self.c" + str(i) + ".final_class_fr_name = schedule[i].final_class_fr_name")
                    exec("self.c" + str(i) + ".final_class_ch_name = schedule[i].final_class_ch_name")
                    exec("self.c" + str(i) + ".final_teacher = schedule[i].final_teacher")
                    exec("self.c" + str(i) + ".final_classroom = schedule[i].final_classroom")

        except Exception as e:
            print("error272", e)

        # def return_tomorrow_schedule(self):
        if self.grade in preparatory_grades:
            try:
                message0 = f'{self.situation}的课程表:'
                if self.replacement:
                    message0 = f'{self.situation}补的是第' + str(self.week + 1) + '周' + self.what_day + '的课:'

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
                    print('student schedule info send ----> None')

                    message0 = f'{self.situation}全天没有课'

                # 新增预科阶段的验证网站
                message_url = ''
                if self.grade == 18:
                    message_url = '\n\n※课表图片链接:\n' + url_schedule_18
                elif self.grade == 19:
                    message_url = '\n\n※课表图片链接:\n' + url_schedule_19 + '\n※可点此查看td课信息:\n' + url_19_td
                elif self.grade == 20:
                    message_url = '\n\n※课表图片链接:\n' + url_schedule_20

                message0 = message0 + message_url + self.inform_msg

                return message0

            except Exception as e:
                print(f'student tomorrow info send ----> fail\n{e}\n')
