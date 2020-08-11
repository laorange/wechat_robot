import xlrd
import re
import time
# from pprint import pprint
from baijiaxing import bai_jia_xing

time_today = time.strftime('%Y-%m-%d %H:%M', time.localtime())
print(time_today)


class Class:
    def __init__(self):
        self.class_property = []
        self.class_fr_name_ls = []
        self.class_ch_name_ls = []
        self.teacher_ls = []
        self.classroom_ls = []
        self.correspond_week = []
        self.correspond_class = []

        self.final_class_fr_name = ''
        self.final_class_ch_name = ''
        self.final_teacher = ''
        self.final_classroom = ''


def get_today_schedule(grade, what_day):
    path = ''
    if grade == 2017:
        path = '2017.xls'
    if grade == 2018:
        path = ''
    if grade == 2019:
        path = '2019.xlsx'
    if grade == 2020:
        path = ''

    data = xlrd.open_workbook(path)
    table = data.sheets()[0]

    start_colx = 0
    end_colx = 0
    # nrows = table.nrows
    # ncols = table.ncols
    # print(nrows,ncols)
    # (36,11)

    if what_day == 'Monday':
        start_colx = 1
        end_colx = 3
    if what_day == 'Tuesday':
        start_colx = 3
        end_colx = 5
    if what_day == 'Wednesday':
        start_colx = 5
        end_colx = 7
    if what_day == 'Thursday':
        start_colx = 7
        end_colx = 9
    if what_day == 'Friday':
        start_colx = 9
        end_colx = 11
    if what_day == 'Saturday':
        pass
    if what_day == 'Sunday':
        pass

    today_schedule = [Class(), Class(), Class(), Class(), Class()]

    info_dict = {}

    for class_num in range(5):
        i = [8, 12, 20, 24, 30][class_num]
        ls = table.row_values(i, start_colx=start_colx, end_colx=end_colx)
        for _ in range(len(ls)):
            ls[_] = re.split(r'[\n]', ls[_])
            ls[_] = list(map(str.strip, ls[_]))
            ls[_] = list(filter(None, ls[_]))
        ls = list(filter(None, ls))
        # re.split(r'[\n]',
        exec("info_dict['c" + str(class_num) + "']=ls")

    # pprint(info_dict)

    for i in range(5):
        class_fr_name = class_ch_name = ''

        for each_class in info_dict['c' + str(i)]:
            # total_split = 0
            # no_property_time = 0
            correspond_class = ''
            teacher = ''
            classroom = ''
            dan_shuang_zhou = 0  # 0无，1奇数周，2偶数周

            class_property = ''
            for each_info in each_class:
                each_info_ls = re.split(r'[ ,，]', each_info)
                # total_split += len(each_info_ls)

                if re.match(r'^[A-Za-z]+', each_info):
                    if len(each_info) > 4 and each_info[:2] not in ['PA', 'PB', 'PC', 'PD', 'PE']:
                        class_fr_name = each_info
                        today_schedule[i].class_fr_name_ls.append(class_fr_name)

                if re.search(r'^[\u4E00-\u9FA5]+', each_info):
                    if each_info[0] not in ['双', '单', '外', '教', '南']:
                        if len(each_info) > 3 or each_info[0] in ['数', '化', '物']:
                            if each_info[0] not in bai_jia_xing or each_info[:2] in ['高等']:
                                class_ch_name = each_info
                                today_schedule[i].class_ch_name_ls.append(class_ch_name)

                for _ in each_info_ls:
                    if _:
                        if _ == 'AB班':
                            class_property = 'all'
                            correspond_class = 'all'
                            today_schedule[i].correspond_class.append(correspond_class)

                        elif 'A班' == _:
                            class_property = 'AB'
                            correspond_class = 'A'
                            today_schedule[i].correspond_class.append(correspond_class)

                        elif 'B班' == _:
                            class_property = 'AB'
                            correspond_class = 'B'
                            today_schedule[i].correspond_class.append(correspond_class)

                        elif 'PA' == _:
                            class_property = 'P'
                            correspond_class = 'PA'
                            today_schedule[i].correspond_class.append(correspond_class)

                        elif 'PB' == _:
                            class_property = 'P'
                            correspond_class = 'PB'
                            today_schedule[i].correspond_class.append(correspond_class)

                        elif 'PC' == _:
                            class_property = 'P'
                            correspond_class = 'PC'
                            today_schedule[i].correspond_class.append(correspond_class)

                        elif 'PD' == _:
                            class_property = 'P'
                            correspond_class = 'PD'
                            today_schedule[i].correspond_class.append(correspond_class)

                        elif 'PE' == _:
                            class_property = 'F'
                            correspond_class = 'PE'
                            today_schedule[i].correspond_class.append(correspond_class)
                        # else:
                        #     no_property_time += 1

                        if _ == '单周':
                            dan_shuang_zhou = 1

                        elif _ == '双周':
                            dan_shuang_zhou = 2

                        if _[0] in bai_jia_xing and _[0] not in ['南', '单', '双'] and _[:2] != '高等' or _ in ['Joël'] or _[
                                                                                                                      :2] == '外教':
                            teacher = _
                            today_schedule[i].teacher_ls.append(teacher)

                        if re.search(r'^\d{3}', _) or re.search(r'\d{3}$', _) or _[0] == '南':
                            classroom = _
                            today_schedule[i].classroom_ls.append(classroom)

                        prob_week = re.match(r'(\d+)([-~])(\d+)周', _)
                        prob_weeks = re.match(r'.*(\d+)[,， ]*?(\d+).?周', _)
                        if prob_week:
                            # print('here1')
                            prob_week = prob_week.groups()
                            ls = list(range(int(prob_week[0]) - 1, int(prob_week[2])))
                            if dan_shuang_zhou == 1:
                                for _ in ls:
                                    if _ % 2 == 0:
                                        ls.remove(_)
                            elif dan_shuang_zhou == 2:
                                for _ in ls:
                                    if _ % 2 == 1:
                                        ls.remove(_)
                            today_schedule[i].correspond_week.append(ls)

                        elif prob_weeks:
                            # print('here2')
                            ls = list(re.findall(r'(\d{1,2})', _))
                            today_schedule[i].correspond_week.append(ls)

                max_len = max(len(today_schedule[i].correspond_class),
                              len(today_schedule[i].teacher_ls),
                              len(today_schedule[i].correspond_class),
                              len(today_schedule[i].class_property),
                              len(today_schedule[i].correspond_week))

                if classroom:
                    while len(today_schedule[i].classroom_ls) < max_len:
                        today_schedule[i].classroom_ls.append(classroom)
                if teacher:
                    while len(today_schedule[i].teacher_ls) < max_len:
                        today_schedule[i].teacher_ls.append(teacher)
                if correspond_class:
                    while len(today_schedule[i].correspond_class) < max_len:
                        today_schedule[i].correspond_class.append(correspond_class)
                if class_property:
                    while len(today_schedule[i].class_property) < max_len:
                        today_schedule[i].class_property.append(class_property)
                if len(ls):
                    while len(today_schedule[i].correspond_week) < max_len:
                        today_schedule[i].correspond_week.append(ls)

            if class_property == '':
                class_property = 'all'
                today_schedule[i].correspond_class.append('all')

            if class_property:
                while len(today_schedule[i].class_property) < len(today_schedule[i].correspond_class):
                    today_schedule[i].class_property.append(class_property)

            if class_ch_name:
                while len(today_schedule[i].class_ch_name_ls) < len(today_schedule[i].correspond_class):
                    today_schedule[i].class_ch_name_ls.append(class_ch_name)

            if class_fr_name:
                while len(today_schedule[i].class_fr_name_ls) < len(today_schedule[i].correspond_class):
                    today_schedule[i].class_fr_name_ls.append(class_fr_name)

    # raise Exception('TEST')
    return today_schedule, what_day


def write_today_schedule(grade, today_schedule, what_day):
    what_day_lower = what_day.lower()
    for class_num in range(5):
        cls = today_schedule[class_num]
        with open(f'schedule{grade}.py', 'at', encoding='UTF-8') as schedule_py:
            schedule_py.write(f'''\
# {what_day} 第{class_num}节课
{what_day_lower}{class_num} = Class()
{what_day_lower}{class_num}.class_property = {cls.class_property}
{what_day_lower}{class_num}.class_fr_name_ls = {cls.class_fr_name_ls}
{what_day_lower}{class_num}.class_ch_name_ls = {cls.class_ch_name_ls}
{what_day_lower}{class_num}.correspond_week = {cls.correspond_week}
{what_day_lower}{class_num}.correspond_class = {cls.correspond_class}
{what_day_lower}{class_num}.classroom_ls = {cls.classroom_ls}
{what_day_lower}{class_num}.teacher_ls = {cls.teacher_ls}

''')
    with open(f'schedule{grade}.py', 'at', encoding='UTF-8') as schedule_py:
        schedule_py.write(f'''\
{what_day_lower}_ls = ({what_day_lower}0, {what_day_lower}1, {what_day_lower}2, {what_day_lower}3, {what_day_lower}4) 

''')


def get_write_what_day(grade, what_day):
    today_schedule, what_day = get_today_schedule(grade, what_day)
    write_today_schedule(grade, today_schedule, what_day)


def write_class_info(grade):
    with open(f'schedule{grade}.py', 'wt', encoding='UTF-8') as schedule_py:
        schedule_py.write('''\
# coding: utf-8

# {}级课表 更新时间:{}
class Class:
    def __init__(self):
        self.class_property = []
        self.class_fr_name_ls = []
        self.class_ch_name_ls = []
        self.teacher_ls = []
        self.classroom_ls = []
        self.correspond_week = []
        self.correspond_class = []
        self.final_class_fr_name = ''
        self.final_class_ch_name = ''
        self.final_teacher = ''
        self.final_classroom = ''


'''.format(grade, time_today))


def grade_yi_tiao_long_fu_wu(grade):
    write_class_info(grade)
    what_day_ls = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    for i in range(len(what_day_ls)):
        what_day = what_day_ls[i]
        get_write_what_day(grade, what_day)


if __name__ == "__main__":
    grade_yi_tiao_long_fu_wu(2019)
    grade_yi_tiao_long_fu_wu(2017)
