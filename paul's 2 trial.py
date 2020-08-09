import xlrd
import re
from pprint import pprint
from baijiaxing import bai_jia_xing

data = xlrd.open_workbook(r'2020-2021（1）Annee2.xlsx')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
# print(nrows,ncols)
# (36,11)


class Class:
    def __init__(self):
        self.class_property = []
        self.class_fr_name_ls = []
        self.class_ch_name_ls = []
        self.teacher_ls = []
        self.classroom_ls = []
        self.correspond_week = []
        self.correspond_class = []


def get_today_schedule(what_day):
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

    pprint(info_dict)

    for i in range(5):
        total_split = 0
        for each_class in info_dict['c' + str(i)]:
            no_property_time = 0
            class_property = None
            for each_info in each_class:
                if re.search(r'^[A-Za-z]+', each_info):
                    today_schedule[i].class_fr_name_ls.append(each_info)
                elif re.search(r'^[\u4E00-\u9FA5]{4,20}', each_info):
                    today_schedule[i].class_ch_name_ls.append(each_info)

                each_info_ls = re.split(r'[ ,]', each_info)
                total_split += len(each_info_ls)

                for _ in each_info_ls:
                    if _:
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

                        prob_week = re.findall(r'.*\d周', _)
                        if prob_week:
                            for result_re in prob_week:
                                if result_re:
                                    prob_several_weeks = re.match(r'(\d{1,2})\-(\d{1,2})周', result_re)
                                    print(type(prob_several_weeks))
                                    if prob_several_weeks:
                                        print('prob_several_weeks.groups(1)', prob_several_weeks.group(1))  # ?
                                        print('prob_several_weeks.groups(2)', prob_several_weeks.group(2))  # ?
                                        try:
                                            today_schedule[i].correspond_week.append(range(int(prob_several_weeks.group(1)), int(prob_several_weeks.group(2))+1))
                                        except Exception as e:
                                            print('处理周数时出错', e)
                                    else:
                                        prob_certain_weeks = re.findall(r'\d', result_re)
                                        today_schedule[i].correspond_week.append(list(prob_certain_weeks))

            if no_property_time == total_split:
                class_property = 'all'
                today_schedule[i].correspond_class.append('all')

            today_schedule[i].class_property.append(class_property)

    return today_schedule

# raise Exception('TEST')


if __name__ == "__main__":
    today_schedule = get_today_schedule('Monday')
    for each_class in today_schedule:
        print(each_class.class_property, '\n',
              each_class.class_fr_name_ls, '\n',
              each_class.class_ch_name_ls, '\n',
              each_class.teacher_ls, '\n',
              each_class.classroom_ls, '\n',
              each_class.correspond_week, '\n',
              each_class.correspond_class)
