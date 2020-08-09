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

for class_num in range(5):
    i = [8, 12, 20, 24, 30][class_num]

    ls = table.row_values(i, start_colx=1, end_colx=3)
    for _ in range(len(ls)):
        ls[_] = re.split(r'[\n]', ls[_])
        ls[_] = list(map(str.strip, ls[_]))
        ls[_] = list(filter(None, ls[_]))
    ls = list(filter(None, ls))
    # re.split(r'[\n]',
    exec("info_dict['c" + str(class_num) + "']=ls")

pprint(info_dict)


class Class:
    def __init__(self):
        self.class_fr_name_ls = []
        self.class_ch_name_ls = []
        self.teacher_ls = []
        self.classroom_ls = []


today_schedule = [Class(), Class(), Class(), Class(), Class()]

for i in range(5):
    for each_class in info_dict['c'+str(i)]:
        for each_info in each_class:
            if re.search(r'^[A-Za-z]+', each_info):
                today_schedule[i].class_fr_name_ls.append(each_info)
            if re.search(r'^[\u4E00-\u9FA5]+', each_info):
                today_schedule[i].class_ch_name_ls.append(each_info)


