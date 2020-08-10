import xlrd
import re
import time
from pprint import pprint

data = xlrd.open_workbook(r'2020-2021（1）Annee2.xlsx')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
# print(nrows,ncols)
# (36,11)

info_dict = {}

# for i in [8, 12, 20, 24, 30]:
#     temp_list.append(table.row_values(i, start_colx=1, end_colx=10))
# x = temp_list[4][2]

for class_num in range(5):
    i = [8, 12, 20, 24, 30][class_num]
    # temp_list = []
    exec("info_dict['c"+str(class_num+1)+"']=table.row_values(i, start_colx=1, end_colx=3)")

# temp_list = list(filter(None, temp_list))
# print(temp_list)
pprint(info_dict)
print('start')

# for class_num in range(len(temp_list)):
#
#     for info in temp_list[class_num]:
#         info_ls = re.split(r'[\n]', info)
#
#         info_ls = list(map(str.strip, info_ls))
#         info_ls = list(filter(None, info_ls))
#
#         # for _ in info_ls:
#         #     if '周' in _:
#         #         print(_)
#         #         print()
#
#         print(info_ls)
#     print('\n\n')





# elif code[:3] == 'EWK':
#         if code[3] == '1':
#             week_day = 'Monday'
#         elif code[3] == '2':
#             week_day = 'Tuesday'
#         elif code[3] == '3':
#             week_day = 'Wednesday'
#         elif code[3] == '4':
#             week_day = 'Thursday'
#         elif code[3] == '5':
#             week_day = 'Friday'
#         elif code[3] == '6':
#             week_day = 'Saturday'
#         elif code[3] == '7':
#             week_day = 'Sunday'






# def get_info_from_excel(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num):
#     if what_day == 'Monday':
#         for i in [8, 12, 20, 24, 30]:
#             temp_list.append(table.row_values(i, start_colx=1, end_colx=2))
#     if what_day == 'Tuesday':
#         for i in [8, 12, 20, 24, 30]:
#             temp_list.append(table.row_values(i, start_colx=3, end_colx=4))
#     if what_day == 'Wednesday':
#         for i in [8, 12, 20, 24, 30]:
#             temp_list.append(table.row_values(i, start_colx=5, end_colx=6))
#     if what_day == 'Thursday':
#         for i in [8, 12, 20, 24, 30]:
#             temp_list.append(table.row_values(i, start_colx=7, end_colx=8))
#     if what_day == 'Friday':
#         for i in [8, 12, 20, 24, 30]:
#             temp_list.append(table.row_values(i, start_colx=9, end_colx=10))
#     if what_day == 'Saturday':
#         # for i in [8, 12, 20, 24, 30]:
#         #     temp_list.append(table.row_values(i, start_colx=11, end_colx=12))
#         pass
#     if what_day == 'Sunday':
#         # for i in [8, 12, 20, 24, 30]:
#         #     temp_list.append(table.row_values(i, start_colx=13, end_colx=14))
#         pass
#
#     dict_info = {}
#     pass
#     return dict_info


class ClassExcel:
    def __init__(self, grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num):
        # self.property = get_info_from_excel(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num)['property']
        self.grade = grade  # 年级
        self.a_or_b = a_or_b  # 大AB班
        self.p_ab_cd = p_ab_cd  # td班
        self.f_ab_cd_e = f_ab_cd_e  # 法语班
        self.week = week
        self.what_day = what_day
        self.class_num = class_num
        self.class_name = self.teacher = self.classroom = ''

    # self.class_name = get_info_from_excel(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num)['class_name']
    # self.teacher = get_info_from_excel(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num)['teacher']
    # self.classroom = get_info_from_excel(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num)['classroom']

    # def get_info(self):
        # info_dict = get_info_from_excel(self.grade, self.a_or_b, self.p_ab_cd, self.f_ab_cd_e,
        #                                 self.week, self.what_day, self.class_num)
        # if self.property == 'AB' or 'none':
        #     pass
        # if self.property == 'P':
        #     pass
        # if self.property == 'F':
        #     pass

    def make_class_ls(self):
        return [self.class_name, self.teacher, self.classroom]


class Class:
    def __init__(self, grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num):
        self.class_name = ClassExcel(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num).make_class_ls()[0]
        self.teacher = ClassExcel(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num).make_class_ls()[1]
        self.classroom = ClassExcel(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num).make_class_ls()[2]

    def __call__(self):
        pass  # sent()


class OneDaySchedule:
    def __init__(self, grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day):
        self.c1 = Class(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, 0)
        self.c2 = Class(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, 1)
        self.c3 = Class(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, 2)
        self.c4 = Class(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, 3)
        self.c5 = Class(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, 4)

    def __call__(self, class_num):
        code = 'self.c' + str(class_num + 1) + '()'
        exec(code)


class Student:
    def __init__(self, grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num):
        self.grade = grade  # 年级
        self.a_or_b = a_or_b  # 大AB班
        self.p_ab_cd = p_ab_cd  # td班
        self.f_ab_cd_e = f_ab_cd_e  # 法语班
        self.schedule = OneDaySchedule(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day)

    def __call__(self, class_num):
        self.schedule(class_num)
    #     return get_class(self.grade, self.a_or_b, self.p_ab_cd, self.f_ab_cd_e, week, what_day, class_num)


if __name__ == "__main__":
    pass

'''
if no_property_time == total_split:
    class_property = 'all'
    today_schedule[i].correspond_class.append('all')

while len(today_schedule[i].class_property) < len(today_schedule[i].correspond_class):
    today_schedule[i].class_property.append(class_property)

while len(today_schedule[i].correspond_week) < len(today_schedule[i].correspond_class):
    today_schedule[i].correspond_week.append(ls)

while len(today_schedule[i].correspond_week) < len(today_schedule[i].correspond_class):
    today_schedule[i].correspond_week.append(ls)

while len(today_schedule[i].class_ch_name_ls) < len(today_schedule[i].correspond_class):
    today_schedule[i].class_ch_name_ls.append(class_ch_name)

while len(today_schedule[i].class_fr_name_ls) < len(today_schedule[i].correspond_class):
    today_schedule[i].class_fr_name_ls.append(class_fr_name)'''






'''
import xlrd
import re
from pprint import pprint
from baijiaxing import bai_jia_xing


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

    def determine_finally(self, grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num):
        if len(self.class_property) == 0:
            print('len(self.class_property) == 0')

        elif self.class_property[0] == 'all':
            for final_index in range(len(self.correspond_week)):
                if week in self.correspond_week[final_index]:
                    self.final_class_fr_name = self.class_fr_name_ls[final_index]
                    self.final_class_ch_name = self.class_ch_name_ls[final_index]
                    self.final_teacher = self.teacher_ls[final_index]
                    self.final_classroom = self.classroom_ls[final_index]

        elif self.class_property[0] == 'AB':
            for final_index in range(len(self.correspond_week)):
                if week in self.correspond_week[final_index] and a_or_b == self.correspond_class[final_index]:
                    self.final_class_fr_name = self.class_fr_name_ls[final_index]
                    self.final_class_ch_name = self.class_ch_name_ls[final_index]
                    self.final_teacher = self.teacher_ls[final_index]
                    self.final_classroom = self.classroom_ls[final_index]

        elif self.class_property[0] == 'P':
            for final_index in range(len(self.correspond_week)):
                if week in self.correspond_week[final_index] and p_ab_cd == self.correspond_class[final_index]:
                    self.final_class_fr_name = self.class_fr_name_ls[final_index]
                    self.final_class_ch_name = self.class_ch_name_ls[final_index]
                    self.final_teacher = self.teacher_ls[final_index]
                    self.final_classroom = self.classroom_ls[final_index]

        elif self.class_property[0] == 'F':
            for final_index in range(len(self.correspond_class)):
                if week in self.correspond_week[final_index] and f_ab_cd_e == self.correspond_class[final_index]:
                    self.final_class_fr_name = self.class_fr_name_ls[final_index]
                    self.final_class_ch_name = self.class_ch_name_ls[final_index]
                    self.final_teacher = self.teacher_ls[final_index]
                    self.final_classroom = self.classroom_ls[final_index]


def get_today_schedule(grade, what_day):
    path = ''
    if grade == 2017:
        path = ''
    if grade == 2018:
        path = ''
    if grade == 2019:
        path = '2020-2021（1）Annee2.xlsx'
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
        for each_class in info_dict['c' + str(i)]:
            total_split = 0
            no_property_time = 0

            class_property = None
            for each_info in each_class:

                each_info_ls = re.split(r'[ ,，]', each_info)
                total_split += len(each_info_ls)

                for _ in each_info_ls:
                    if _:
                        if re.search(r'^[A-Za-z]+', _):
                            if len(_) > 4:
                                class_fr_name = _
                                today_schedule[i].class_fr_name_ls.append(class_fr_name)
                        elif re.search(r'^[\u4E00-\u9FA5]+', _):
                            if _[0] not in ['双', '单', '外', '教', '南']:
                                if len(_) > 3 or _[0] in ['数', '化', '物']:
                                    class_ch_name = _
                                    today_schedule[i].class_ch_name_ls.append(class_ch_name)

                        if 'AB班' == _:
                            class_property = 'all'
                            today_schedule[i].correspond_class.append('all')

                        elif 'A班' == _:
                            class_property = 'AB'
                            today_schedule[i].correspond_class.append('A')

                        elif 'B班' == _:
                            class_property = 'AB'
                            today_schedule[i].correspond_class.append('B')

                        elif 'PA' == _:
                            class_property = 'P'
                            today_schedule[i].correspond_class.append('PA')

                        elif 'PB' == _:
                            class_property = 'P'
                            today_schedule[i].correspond_class.append('PB')

                        elif 'PC' == _:
                            class_property = 'P'
                            today_schedule[i].correspond_class.append('PC')

                        elif 'PD' == _:
                            class_property = 'P'
                            today_schedule[i].correspond_class.append('PD')

                        elif 'PE' == _:
                            class_property = 'F'
                            today_schedule[i].correspond_class.append('PE')
                        else:
                            no_property_time += 1

                        if _[0] in bai_jia_xing and _[0] != '南' and _[:2] != '高等':
                            today_schedule[i].teacher_ls.append(_)
                        if re.search(r'^\d{3}$', _) or _[0] == '南':
                            today_schedule[i].classroom_ls.append(_)

                        prob_week = re.match(r'.*(\d{1,2})([-~])(\d{1,2}).?周', _)
                        prob_weeks = re.match(r'.*(\d{1,2})[,， ]*?(\d{1,2}).?周', _)
                        if prob_week:
                            print('here1')
                            prob_week = prob_week.groups()
                            ls = list(range(int(prob_week[0])-1, int(prob_week[2])))
                            today_schedule[i].correspond_week.append(ls)

                        elif prob_weeks:
                            print('here2')
                            ls = list(re.findall(r'(\d{1,2})', _))
                            today_schedule[i].correspond_week.append(ls)

                if no_property_time == total_split:
                    class_property = 'all'
                    today_schedule[i].correspond_class.append('all')

                while len(today_schedule[i].class_property) < len(today_schedule[i].correspond_class):
                    today_schedule[i].class_property.append(class_property)
                
                while len(today_schedule[i].correspond_week) < len(today_schedule[i].correspond_class):
                    today_schedule[i].correspond_week.append(ls)

                while len(today_schedule[i].correspond_week) < len(today_schedule[i].correspond_class):
                    today_schedule[i].correspond_week.append(ls)
                    
                while len(today_schedule[i].cla) < len(today_schedule[i].correspond_class):
                    today_schedule[i].correspond_week.append(ls)

                

            today_schedule[i].class_property.append(class_property)

    return today_schedule


class Student:
    def __init__(self, grade, a_or_b, p_ab_cd, f_ab_cd_e):
        self.grade = grade  # 年级
        self.a_or_b = a_or_b  # 大AB班
        self.p_ab_cd = p_ab_cd  # td班
        self.f_ab_cd_e = f_ab_cd_e  # 法语班

    def __call__(self, week, what_day, class_num):
        schedule = get_today_schedule(self.grade, what_day)
        print(schedule)
        target_class = schedule[class_num]
        target_class.determine_finally(self.grade, self.a_or_b, self.p_ab_cd, self.f_ab_cd_e, week, what_day, class_num)

        if target_class.class_property is None:
            print('这节没课哟')
            return '', '', ''
        else:
            print('这节课是{}的{},地点在:{}'.format(target_class.final_teacher,
                                            target_class.final_class_ch_name,
                                            target_class.final_classroom))
            return target_class.final_teacher, target_class.final_class_ch_name, target_class.final_classroom

    # return get_class(self.grade, self.a_or_b, self.p_ab_cd, self.f_ab_cd_e, week, what_day, class_num)


if __name__ == "__main__":
    # today_schedule = get_today_schedule('Monday')
    # for each_class in today_schedule:
    #     print(each_class.class_property, '\n',
    #           each_class.class_fr_name_ls, '\n',
    #           each_class.class_ch_name_ls, '\n',
    #           each_class.teacher_ls, '\n',
    #           each_class.classroom_ls, '\n',
    #           each_class.correspond_week, '\n',
    #           each_class.correspond_class)
    student = Student(2019, 'B', 'PC', 'PC')
    student(5, 'Tuesday', 1)

    raise Exception('TEST')

'''