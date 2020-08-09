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
            for final_index in range(len(self.correspond_week)):
                if week in self.correspond_week[final_index] and f_ab_cd_e == self.correspond_class[final_index]:
                    self.final_class_fr_name = self.class_fr_name_ls[final_index]
                    self.final_class_ch_name = self.class_ch_name_ls[final_index]
                    self.final_teacher = self.teacher_ls[final_index]
                    self.final_classroom = self.classroom_ls[final_index]


def get_today_schedule(grade, what_day):
    if grade == 2019:
        path = '2020-2021（1）Annee2.xlsx'

    data = xlrd.open_workbook(path)
    table = data.sheets()[0]

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

                        prob_week = re.findall(r'.*\d.*?周', _)
                        if prob_week:
                            for result_re in prob_week:
                                if result_re:
                                    prob_several_weeks = re.match(r'(\d{1,2})\-(\d{1,2}).*?周', result_re)
                                    print(type(prob_several_weeks))
                                    if prob_several_weeks:
                                        print('prob_several_weeks.groups(1)', prob_several_weeks.group(1))  # ?
                                        print('prob_several_weeks.groups(2)', prob_several_weeks.group(2))  # ?
                                        try:
                                            today_schedule[i].correspond_week.append(
                                                range(int(prob_several_weeks.group(1)),
                                                      int(prob_several_weeks.group(2)) + 1))
                                        except Exception as e:
                                            print('处理周数时出错', e)
                                    else:
                                        prob_certain_weeks = re.findall(r'\d', result_re)
                                        today_schedule[i].correspond_week.append(list(prob_certain_weeks))

            if no_property_time == total_split:
                class_property = 'all'
                today_schedule[i].correspond_class.append('all')

            today_schedule[i].class_property.append(class_property)

    raise Exception('TEST')
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


