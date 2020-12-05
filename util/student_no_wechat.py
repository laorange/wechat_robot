from schedule.schedule18 import schedule_18
from schedule.schedule19 import schedule_19
from schedule.schedule20 import schedule_20
from util.time_util import determine_when_exam

import traceback
from loguru import logger

url_17 = 'kb.solars.top/17/S1/'
url_16 = 'kb.solars.top/16/S3/'
url_15 = 'kb.solars.top/15/S5/'

url_schedule_18 = 'laorange.top/kb/18/18.png'
url_schedule_19 = 'laorange.top/kb/19/19.png'
url_schedule_20 = 'laorange.top/kb/20/20.jpg'
# url_schedule_preparatory_grades = [url_schedule_18, url_schedule_19, url_schedule_20]
# url_19_td1 = 'laorange.top/img/19td1.png'
# url_19_td2 = 'laorange.top/img/19td2.png'
# 手动改改吧...
url_19_td = 'laorange.top/kb/19/td.pdf'

preparatory_grades = [18, 19, 20]
engineer_grades = [17, 16, 15]
url_engineer_grades = [url_17, url_16, url_15]


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

        # TODO: 通知
        self.inform_msg = ''  # "\n\n※注:solars.top服务器类型是限制流量的，还请大家需时查看，请勿频繁刷新"

        self.schedule_grade = []
        if grade in preparatory_grades:
            try:
                exec('self.schedule_grade = schedule_' + str(grade))
            except Exception as e:
                logger.error(f'在读取{grade}级课表时出错' + str(e))
                traceback.print_exc()

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

    def get_schedule(self, situation: str, date: str, week: int, what_day: str, t_delay=0):
        message0 = ''
        real_week = week
        self.situation = situation
        self.what_day_real = what_day
        if week > 14:  # 本学期只有15周，特殊情况
            message0 = "如果没猜错的话，此时本学期的课程已结束"

        else:
            try:
                # TODO: 补充 周末补课的判断条件
                if self.grade == 20 and date == '2020-10-09':
                    week = 14
                    what_day = 'Friday'
                    self.replacement = True  # add @ 2020-10-08
                if week == 5 and what_day == 'Sunday':
                    week = 16
                    what_day = 'Thursday'
                    self.replacement = True
                elif week == 6 and what_day == 'Sunday' and self.grade == 20:
                    week = 15
                    what_day = 'Monday'
                    self.replacement = True
                elif week == 7 and what_day == 'Sunday' and self.grade == 20:
                    week = 15
                    what_day = 'Wednesday'
                    self.replacement = True
                elif week == 8 and what_day == 'Sunday' and self.grade == 20:
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
                elif date == '2020-10-04':
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
                # ------------补充 周末补课的判断条件-------------- #

                self.week = week
                self.what_day = what_day

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
                    what_day_num = 6
                else:
                    what_day_num = -1

                message0 = ''
                # TODO: 工程师阶段 返回课表链接
                if self.grade in engineer_grades:
                    message0 = url_engineer_grades[engineer_grades.index(self.grade)]
                    if self.situation != '今天':
                        message0 = '可点击该链接查看课表:\n' + message0 + '?p=' + str(real_week + 3)
                    else:
                        message0 = '可点击该链接查看课表:\n' + message0

                # TODO: 返回 待发送的课表信息
                elif self.grade in preparatory_grades:
                    # TODO: 预科阶段 获取总schedule
                    # 条件：正常情况 预科阶段周日没有课
                    if what_day_num not in [-1, 6]:
                        schedule = self.schedule_grade[what_day_num]

                        # TODO: 对schedule_ls的final系列的初始化
                        for i in range(5):
                            schedule[i].final_class_fr_name = ''
                            schedule[i].final_class_ch_name = ''
                            schedule[i].final_teacher = ''
                            schedule[i].final_classroom = ''

                        # TODO: ⭐根据用户信息 解析出课程表
                        for i in range(5):  # 第i节课
                            if not schedule[i].class_property:
                                # logger.info(f'{self.name}:{self.situation}第{(i + 1) * 2 - 1},{(i + 1) * 2}没课')
                                pass  # 没课 -> 无操作

                            else:
                                for final_index in range(len(schedule[i].class_property)):
                                    if schedule[i].class_property[final_index] == 'all':
                                        if week in schedule[i].correspond_week[final_index]:
                                            try:
                                                if len(schedule[i].class_fr_name_ls) > final_index:
                                                    schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[
                                                        final_index]
                                                if len(schedule[i].class_ch_name_ls) > final_index:
                                                    schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[
                                                        final_index]
                                                if len(schedule[i].teacher_ls) > final_index:
                                                    schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                                if len(schedule[i].classroom_ls) > final_index:
                                                    schedule[i].final_classroom = schedule[i].classroom_ls[final_index]
                                            except Exception as e:
                                                logger.error(f'在处理{self.name}的第({i})节课时出错,{e}')
                                    elif schedule[i].class_property[final_index] == 'AB':
                                        if self.a_or_b == schedule[i].correspond_class[final_index]:
                                            if week in schedule[i].correspond_week[final_index]:
                                                try:
                                                    if len(schedule[i].class_fr_name_ls) > final_index:
                                                        schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[
                                                            final_index]
                                                    if len(schedule[i].class_ch_name_ls) > final_index:
                                                        schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[
                                                            final_index]
                                                    if len(schedule[i].teacher_ls) > final_index:
                                                        schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                                    if len(schedule[i].classroom_ls) > final_index:
                                                        schedule[i].final_classroom = schedule[i].classroom_ls[
                                                            final_index]
                                                except Exception as e:
                                                    logger.error(f'在处理{self.name}的第({i})节课时出错,{e}')
                                    elif schedule[i].class_property[final_index] == 'P':
                                        if self.p_ab_cd == schedule[i].correspond_class[final_index]:
                                            if week in schedule[i].correspond_week[final_index]:
                                                try:
                                                    if len(schedule[i].class_fr_name_ls) > final_index:
                                                        schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[
                                                            final_index]
                                                    if len(schedule[i].class_ch_name_ls) > final_index:
                                                        schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[
                                                            final_index]
                                                    if len(schedule[i].teacher_ls) > final_index:
                                                        schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                                    if len(schedule[i].classroom_ls) > final_index:
                                                        schedule[i].final_classroom = schedule[i].classroom_ls[
                                                            final_index]
                                                except Exception as e:
                                                    logger.error(f'在处理{self.name}的第({i})节课时出错,{e}')
                                    elif schedule[i].class_property[final_index] == 'F':
                                        if self.f_ab_cd_e == schedule[i].correspond_class[final_index]:
                                            if week in schedule[i].correspond_week[final_index]:
                                                try:
                                                    if len(schedule[i].class_fr_name_ls) > final_index:
                                                        schedule[i].final_class_fr_name = schedule[i].class_fr_name_ls[
                                                            final_index]
                                                    if len(schedule[i].class_ch_name_ls) > final_index:
                                                        schedule[i].final_class_ch_name = schedule[i].class_ch_name_ls[
                                                            final_index]
                                                    if len(schedule[i].teacher_ls) > final_index:
                                                        schedule[i].final_teacher = schedule[i].teacher_ls[final_index]
                                                    if len(schedule[i].classroom_ls) > final_index:
                                                        schedule[i].final_classroom = schedule[i].classroom_ls[
                                                            final_index]
                                                except Exception as e:
                                                    logger.error(f'在处理{self.name}的第({i})节课时出错,{e}')
                                exec("self.c" + str(i) + ".final_class_fr_name = schedule[i].final_class_fr_name")
                                exec("self.c" + str(i) + ".final_class_ch_name = schedule[i].final_class_ch_name")
                                exec("self.c" + str(i) + ".final_teacher = schedule[i].final_teacher")
                                exec("self.c" + str(i) + ".final_classroom = schedule[i].final_classroom")

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
                            if len(self.c0.final_class_ch_name) + len(self.c1.final_class_ch_name) + \
                                    len(self.c2.final_class_ch_name) + len(self.c3.final_class_ch_name) + \
                                    len(self.c4.final_class_ch_name) == 0:
                                logger.info('student schedule info send ----> None')

                                message0 = f'{self.situation}全天没有课'

                            # 新增预科阶段的验证网站
                            message_url = ''
                            if self.grade == 18:
                                message_url = '\n\n※课表图片链接:\n' + url_schedule_18
                            elif self.grade == 19:
                                message_url = '\n\n※课表图片链接:\n' + url_schedule_19 + '\n※可点此查看td轮班表:\n' + url_19_td
                            elif self.grade == 20:
                                message_url = '\n\n※课表图片链接:\n' + url_schedule_20
                            message0 = message0 + message_url + self.inform_msg

                        except Exception as e:
                            logger.error(f'student tomorrow info send ----> fail\n{e}\n')
                            traceback.print_exc()
                    else:
                        message0 = f"{situation}全天没有课"

            except Exception as e:
                logger.error("课表获取出错" + str(e))
                traceback.print_exc()

        # TODO: 获取考试倒计时
        if self.grade in preparatory_grades:
            # 预科阶段 获取考试倒计时
            exams_count_down = determine_when_exam(self.grade, t_delay=t_delay, situation=situation)
            if exams_count_down != '':
                message0 += '\n\n----------\n\n' + exams_count_down

        elif self.grade in engineer_grades:
            # 工程师阶段 获取考试倒计时
            exams_count_down = determine_when_exam(self.grade, situation=situation, t_delay=t_delay)
            if exams_count_down != '':
                message0 = exams_count_down + '\n\n' + message0

        # TODO: 添加某天的公告
        message0 = message0 + self.inform_msg

        if self.grade == 20 and date == '2020-10-16':
            message0 = message0 + '\n\n提示：\n本周五有20人参加运动会开幕式，1.2节的课调到第14周周四7.8节。以上课表信息仅供参考。'

        if self.grade == 20 and week == 13 and what_day == 'Thursday':
            message0 = message0 + '\n\n提示：\n第7周周五有20人参加运动会开幕式，1.2节的课调到本周四7.8节。以上课表信息仅供参考。'

        if self.grade in preparatory_grades and date in ['2020-11-09', '2020-11-10']:
            message0 = '⭐11-09更新⭐\n①新增按日期查询功能，示例：\n"@11-11"\n"@2020-12-1"\n"@12月5日"\n"@2020年12月13号"' \
                       + '\n②可发送“@指令”来查看当前支持的所有指令\n----------\n\n' + message0

        if date == '2020-11-18' and self.situation in ['今天', '明天']:
            message0 = message0 \
                       + '\n\n⭐⭐⭐⭐⭐\n' \
                       + f'{self.situation}中午11:45，中欧合唱团将在中欧楼一楼大厅进行快闪表演，歌曲串烧，时长约八分钟。' \
                       + '欢迎大家前来捧场[跳跳] (错峰用餐~)\n\n点此链接可查看相关信息: laorange.top/kb/herf'

        if self.grade in preparatory_grades and date in ['2020-11-25', '2020-11-26']:
            message0 = message0 + '\n\n⭐⭐⭐⭐⭐\n11-25更新：\n新增功能 可发送"@考试"查看一个月的考试倒计时'

        if self.grade in preparatory_grades and date in ['2020-11-29', '2020-11-30', '2020-12-01']:
            message0 = message0 + '\n\n-------\n11-29调整：\n预科阶段的每日推送时间改为 17:10~18:59'

        if self.grade == 20 and date in ['2020-12-02', '2020-12-03']:
            message0 = message0 + '\n\n-------\n临近期末考试，本周三晚上的课调整到周四晚上，到晚上九点半下课。最后两组集中演讲'

        if self.grade in preparatory_grades and date in ['2020-12-06']:
            message0 = message0 + '''\n\n-------\n推荐一个干货公众号：Mayder
项目网站地址：http://maydertop.natapp1.cc/DataBase/
该项目由14级学长维护，或许这里的学习资料能有帮助；不过这里预科的资料偏少，下学期我们将会以课表推送项目为基础搭建网页，到时候还请大家多多支持'''

        if self.grade in engineer_grades and date in ['2020-12-05']:
            message0 = message0 + '''\n\n-------\n推荐一个干货公众号：Mayder
网站地址：http://maydertop.natapp1.cc/DataBase/
该项目由14级学长维护，或许这里的学习资料能有帮助'''

        return message0
