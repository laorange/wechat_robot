# coding: utf-8

# 2018级课表 更新时间:2020-08-29 20:03
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


# Monday 第0节课
monday0 = Class()
monday0.class_property = ['all']
monday0.class_fr_name_ls = ['Physique']
monday0.class_ch_name_ls = ['经典物理（上）']
monday0.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
monday0.correspond_class = ['all']
monday0.classroom_ls = ['教室201']
monday0.teacher_ls = ['张艳峰/Joël/王亚如']

# Monday 第1节课
monday1 = Class()
monday1.class_property = ['all']
monday1.class_fr_name_ls = ['Cours  Français']
monday1.class_ch_name_ls = ['法语高级写作']
monday1.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
monday1.correspond_class = ['all']
monday1.classroom_ls = ['教室201']
monday1.teacher_ls = ['马锐']

# Monday 第2节课
monday2 = Class()
monday2.class_property = ['P', 'P', 'P', 'P']
monday2.class_fr_name_ls = ['TD physique', 'TD physique', 'Cours  Anglais', 'Cours  Anglais']
monday2.class_ch_name_ls = ['经典物理（上）习题课', '经典物理（上）习题课', '综合英语（1）', '综合英语（1）']
monday2.correspond_week = [
                          [3, 5, 7, 9, 11, 13, 15],
                          [3, 5, 7, 9, 11, 13, 15],
                          [0, 2, 4, 6, 8, 10, 12, 14, 16],
                          [0, 2, 4, 6, 8, 10, 12, 14, 16], ]
monday2.correspond_class = ['PA', 'PB', 'PC', 'PD']
monday2.classroom_ls = ['212', '220', '107', '210']
monday2.teacher_ls = ['王亚如', '秦哲', '外教Eric', '外教Adil']

# Monday 第3节课
monday3 = Class()
monday3.class_property = ['P', 'P', 'P', 'P']
monday3.class_fr_name_ls = ['TD physique', 'TD physique', 'Cours  Anglais', 'Cours  Anglais']
monday3.class_ch_name_ls = ['经典物理（上）习题课', '经典物理（上）习题课', '综合英语（1）', '综合英语（1）']
monday3.correspond_week = [
                          [3, 5, 7, 9, 11, 13, 15],
                          [3, 5, 7, 9, 11, 13, 15],
                          [0, 2, 4, 6, 8, 10, 12, 14, 16],
                          [0, 2, 4, 6, 8, 10, 12, 14, 16], ]
monday3.correspond_class = ['PC', 'PD', 'PA', 'PB']
monday3.classroom_ls = ['212', '210', '107', '108']
monday3.teacher_ls = ['张艳峰', '秦哲/王亚如', '外教Eric', '外教Adil']

# Monday 第4节课
monday4 = Class()
monday4.class_property = []
monday4.class_fr_name_ls = []
monday4.class_ch_name_ls = []
monday4.correspond_week = []
monday4.correspond_class = []
monday4.classroom_ls = []
monday4.teacher_ls = []

monday_ls = (monday0, monday1, monday2, monday3, monday4)

# Tuesday 第0节课
tuesday0 = Class()
tuesday0.class_property = ['all']
tuesday0.class_fr_name_ls = ['Mathématiques']
tuesday0.class_ch_name_ls = ['高等数学（5）']
tuesday0.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
tuesday0.correspond_class = ['all']
tuesday0.classroom_ls = ['220']
tuesday0.teacher_ls = ['徐登明']

# Tuesday 第1节课
tuesday1 = Class()
tuesday1.class_property = ['all']
tuesday1.class_fr_name_ls = ['Physique']
tuesday1.class_ch_name_ls = ['经典物理（上）']
tuesday1.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
tuesday1.correspond_class = ['all']
tuesday1.classroom_ls = ['201']
tuesday1.teacher_ls = ['张艳峰/Joël/王亚如']

# Tuesday 第2节课
tuesday2 = Class()
tuesday2.class_property = ['F', 'F', 'F']
tuesday2.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'TD Mathématiques']
tuesday2.class_ch_name_ls = ['中级法语3', '中级法语3', '高等数学（5）习题课']
tuesday2.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
tuesday2.correspond_class = ['PA', 'PB', 'PC']
tuesday2.classroom_ls = ['212', '208', '309']
tuesday2.teacher_ls = ['外教Julien', '外教Caroline', '林洁']

# Tuesday 第3节课
tuesday3 = Class()
tuesday3.class_property = ['F', 'F', 'F']
tuesday3.class_fr_name_ls = ['Cours  Français', 'TD Mathématiques', 'TD Mathématiques']
tuesday3.class_ch_name_ls = ['中级法语3', '高等数学（5）习题课', '高等数学（5）习题课']
tuesday3.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
tuesday3.correspond_class = ['PC', 'PA', 'PB']
tuesday3.classroom_ls = ['212', '309', '310']
tuesday3.teacher_ls = ['外教Thomas', '林洁', '徐登明']

# Tuesday 第4节课
tuesday4 = Class()
tuesday4.class_property = []
tuesday4.class_fr_name_ls = []
tuesday4.class_ch_name_ls = []
tuesday4.correspond_week = []
tuesday4.correspond_class = []
tuesday4.classroom_ls = []
tuesday4.teacher_ls = []

tuesday_ls = (tuesday0, tuesday1, tuesday2, tuesday3, tuesday4)

# Wednesday 第0节课
wednesday0 = Class()
wednesday0.class_property = ['all']
wednesday0.class_fr_name_ls = ['Mathématiques']
wednesday0.class_ch_name_ls = ['高等数学（5）']
wednesday0.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
wednesday0.correspond_class = ['all']
wednesday0.classroom_ls = ['201']
wednesday0.teacher_ls = ['徐登明']

# Wednesday 第1节课
wednesday1 = Class()
wednesday1.class_property = ['all']
wednesday1.class_fr_name_ls = []
wednesday1.class_ch_name_ls = ['工程制图']
wednesday1.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], ]
wednesday1.correspond_class = ['all']
wednesday1.classroom_ls = ['教室201']
wednesday1.teacher_ls = ['丁宁']

# Wednesday 第2节课
wednesday2 = Class()
wednesday2.class_property = ['F', 'F', 'F']
wednesday2.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
wednesday2.class_ch_name_ls = ['中级法语1', '中级法语1', '中级法语1']
wednesday2.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
wednesday2.correspond_class = ['PA', 'PB', 'PC']
wednesday2.classroom_ls = ['107', '108', '120']
wednesday2.teacher_ls = ['外教Julien', '外教Caroline', '外教Thomas']

# Wednesday 第3节课
wednesday3 = Class()
wednesday3.class_property = ['all']
wednesday3.class_fr_name_ls = []
wednesday3.class_ch_name_ls = ['计算机编程']
wednesday3.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ]
wednesday3.correspond_class = ['all']
wednesday3.classroom_ls = ['220']
wednesday3.teacher_ls = ['马龙']

# Wednesday 第4节课
wednesday4 = Class()
wednesday4.class_property = []
wednesday4.class_fr_name_ls = []
wednesday4.class_ch_name_ls = []
wednesday4.correspond_week = []
wednesday4.correspond_class = []
wednesday4.classroom_ls = []
wednesday4.teacher_ls = []

wednesday_ls = (wednesday0, wednesday1, wednesday2, wednesday3, wednesday4)

# Thursday 第0节课
thursday0 = Class()
thursday0.class_property = ['P', 'P', 'P', 'P']
thursday0.class_fr_name_ls = ['Cours  Anglais', 'Cours  Anglais', 'TD physique', 'TD physique']
thursday0.class_ch_name_ls = ['综合英语（1）', '综合英语（1）', '经典物理（上）习题课', '经典物理（上）习题课']
thursday0.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday0.correspond_class = ['PA', 'PB', 'PC', 'PD']
thursday0.classroom_ls = ['309', '310', '208', '212']
thursday0.teacher_ls = ['外教Eric', '外教Adil', '张艳峰', '秦哲/王亚如']

# Thursday 第1节课
thursday1 = Class()
thursday1.class_property = ['P', 'P', 'P', 'P']
thursday1.class_fr_name_ls = ['Cours  Anglais', 'Cours  Anglais', 'TD physique', 'TD physique']
thursday1.class_ch_name_ls = ['综合英语（1）', '综合英语（1）', '经典物理（上）习题课', '经典物理（上）习题课']
thursday1.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday1.correspond_class = ['PC', 'PD', 'PA', 'PB']
thursday1.classroom_ls = ['309', '310', '208', '210']
thursday1.teacher_ls = ['外教Eric', '外教Adil', '王亚如', '秦哲']

# Thursday 第2节课
thursday2 = Class()
thursday2.class_property = ['F', 'F', 'F']
thursday2.class_fr_name_ls = ['TD Mathématiques', 'Cours  Français', 'Cours  Français']
thursday2.class_ch_name_ls = ['高等数学（5）习题课', '中级法语1', '中级法语1']
thursday2.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday2.correspond_class = ['PC', 'PA', 'PB']
thursday2.classroom_ls = ['309', '107', '207']
thursday2.teacher_ls = ['林洁', '外教Julien', '外教Caroline']

# Thursday 第3节课
thursday3 = Class()
thursday3.class_property = ['F', 'F']
thursday3.class_fr_name_ls = ['TD Mathématiques', 'TD Mathématiques']
thursday3.class_ch_name_ls = ['高等数学（5）习题课', '高等数学（5）习题课']
thursday3.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday3.correspond_class = ['PA', 'PB']
thursday3.classroom_ls = ['309', '310']
thursday3.teacher_ls = ['林洁', '徐登明']

# Thursday 第4节课
thursday4 = Class()
thursday4.class_property = ['F']
thursday4.class_fr_name_ls = ['Cours  Français']
thursday4.class_ch_name_ls = ['中级法语3']
thursday4.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday4.correspond_class = ['PC']
thursday4.classroom_ls = ['120']
thursday4.teacher_ls = ['外教Thomas']

thursday_ls = (thursday0, thursday1, thursday2, thursday3, thursday4)

# Friday 第0节课
friday0 = Class()
friday0.class_property = ['all']
friday0.class_fr_name_ls = ['Physique']
friday0.class_ch_name_ls = ['经典物理（上）']
friday0.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
friday0.correspond_class = ['all']
friday0.classroom_ls = ['220']
friday0.teacher_ls = ['张艳峰/Joël/王亚如']

# Friday 第1节课
friday1 = Class()
friday1.class_property = ['all']
friday1.class_fr_name_ls = ['Mathématiques']
friday1.class_ch_name_ls = ['高等数学（5）']
friday1.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
friday1.correspond_class = ['all']
friday1.classroom_ls = ['201']
friday1.teacher_ls = ['徐登明']

# Friday 第2节课
friday2 = Class()
friday2.class_property = ['all', 'AB']
friday2.class_fr_name_ls = []
friday2.class_ch_name_ls = ['计算机编程', '计算机编程上机课']
friday2.correspond_week = [
                          [2, 4, 6, 8],
                          [3, 5, 7, 9, 10], ]
friday2.correspond_class = ['all', 'B']
friday2.classroom_ls = ['220', '125']
friday2.teacher_ls = ['马龙', '马龙/孙犇渊']

# Friday 第3节课
friday3 = Class()
friday3.class_property = ['AB']
friday3.class_fr_name_ls = []
friday3.class_ch_name_ls = ['计算机编程上机课']
friday3.correspond_week = [
                          [3, 5, 7, 9, 10], ]
friday3.correspond_class = ['A']
friday3.classroom_ls = ['125']
friday3.teacher_ls = ['马龙、孙犇渊']

# Friday 第4节课
friday4 = Class()
friday4.class_property = []
friday4.class_fr_name_ls = []
friday4.class_ch_name_ls = []
friday4.correspond_week = []
friday4.correspond_class = []
friday4.classroom_ls = []
friday4.teacher_ls = []

friday_ls = (friday0, friday1, friday2, friday3, friday4)

# Saturday 第0节课
saturday0 = Class()
saturday0.class_property = ['all']
saturday0.class_fr_name_ls = []
saturday0.class_ch_name_ls = ['工程制图']
saturday0.correspond_week = [
                          [0, 2, 4, 6, 8, 10, 12], ]
saturday0.correspond_class = ['all']
saturday0.classroom_ls = ['教室220']
saturday0.teacher_ls = ['丁宁']

# Saturday 第1节课
saturday1 = Class()
saturday1.class_property = ['AB']
saturday1.class_fr_name_ls = []
saturday1.class_ch_name_ls = ['工程制图 习题课']
saturday1.correspond_week = [
                          [0, 2, 4, 6, 8, 10, 12, 13], ]
saturday1.correspond_class = ['A']
saturday1.classroom_ls = ['教室220']
saturday1.teacher_ls = ['丁宁']

# Saturday 第2节课
saturday2 = Class()
saturday2.class_property = ['AB']
saturday2.class_fr_name_ls = []
saturday2.class_ch_name_ls = ['工程制图 习题课']
saturday2.correspond_week = [
                          [0, 2, 4, 6, 8, 10, 12, 13], ]
saturday2.correspond_class = ['B']
saturday2.classroom_ls = ['教室220']
saturday2.teacher_ls = ['丁宁']

# Saturday 第3节课
saturday3 = Class()
saturday3.class_property = []
saturday3.class_fr_name_ls = []
saturday3.class_ch_name_ls = []
saturday3.correspond_week = []
saturday3.correspond_class = []
saturday3.classroom_ls = []
saturday3.teacher_ls = []

# Saturday 第4节课
saturday4 = Class()
saturday4.class_property = []
saturday4.class_fr_name_ls = []
saturday4.class_ch_name_ls = []
saturday4.correspond_week = []
saturday4.correspond_class = []
saturday4.classroom_ls = []
saturday4.teacher_ls = []

saturday_ls = (saturday0, saturday1, saturday2, saturday3, saturday4)

schedule_2018 = [monday_ls, tuesday_ls, wednesday_ls, thursday_ls, friday_ls, saturday_ls]
