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

temp_list = []
# for i in [8, 12, 20, 24, 30]:
#     temp_list.append(table.row_values(i, start_colx=1, end_colx=10))
# x = temp_list[4][2]

for i in [8, 12, 20, 24, 30]:
    temp_list.append(table.row_values(i, start_colx=1, end_colx=2))

for class_num in range(len(temp_list)):
    for info in temp_list[class_num]:
        info_ls = re.split(r'[\n]', info)

        info_ls = list(map(str.strip, info_ls))
        info_ls = list(filter(None, info_ls))

        for _ in info_ls:
            if '周' in _:
                print(_)
                print()

        print(info_ls)
    print('\n\n')





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

print(temp_list)




def get_info_from_excel(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num):
    if what_day == 'Monday':
        for i in [8, 12, 20, 24, 30]:
            temp_list.append(table.row_values(i, start_colx=1, end_colx=2))
    if what_day == 'Tuesday':
        for i in [8, 12, 20, 24, 30]:
            temp_list.append(table.row_values(i, start_colx=3, end_colx=4))
    if what_day == 'Wednesday':
        for i in [8, 12, 20, 24, 30]:
            temp_list.append(table.row_values(i, start_colx=5, end_colx=6))
    if what_day == 'Thursday':
        for i in [8, 12, 20, 24, 30]:
            temp_list.append(table.row_values(i, start_colx=7, end_colx=8))
    if what_day == 'Friday':
        for i in [8, 12, 20, 24, 30]:
            temp_list.append(table.row_values(i, start_colx=9, end_colx=10))
    if what_day == 'Saturday':
        # for i in [8, 12, 20, 24, 30]:
        #     temp_list.append(table.row_values(i, start_colx=11, end_colx=12))
        pass
    if what_day == 'Sunday':
        # for i in [8, 12, 20, 24, 30]:
        #     temp_list.append(table.row_values(i, start_colx=13, end_colx=14))
        pass





    dict_info = {}
    pass
    return dict_info


class ClassExcel:
    def __init__(self, grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num):
        self.property = get_info_from_excel(grade, a_or_b, p_ab_cd, f_ab_cd_e, week, what_day, class_num)['property']
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

    def get_info(self):
        info_dict = get_info_from_excel(self.grade, self.a_or_b, self.p_ab_cd, self.f_ab_cd_e,
                                        self.week, self.what_day, self.class_num)
        if self.property == 'AB' or 'none':
            pass
        if self.property == 'P':
            pass
        if self.property == 'F':
            pass

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