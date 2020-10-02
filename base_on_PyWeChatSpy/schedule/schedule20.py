# coding: utf-8

# 20级课表 更新时间:2020-09-28 23:43
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
monday0.class_property = ['P', 'P', 'P', 'P']
monday0.class_fr_name_ls = ['Cours  Anglais', 'Cours  Anglais', 'Cours  Anglais', 'Cours  Anglais']
monday0.class_ch_name_ls = ['大学英语（1）', '大学英语（1）', '大学英语（1）', '大学英语（1）']
monday0.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
monday0.correspond_class = ['PA', 'PB', 'PC', 'PD']
monday0.classroom_ls = ['107', '108', '120', '122']
monday0.teacher_ls = ['刘东亮', '刘成盼', '外教Eric', '曹迪']

# Monday 第1节课
monday1 = Class()
monday1.class_property = ['AB', 'AB']
monday1.class_fr_name_ls = ['Cours Physique', 'Cours Physique']
monday1.class_ch_name_ls = ['基础物理（1）', '基础物理（1）']
monday1.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13],
                          [6, 7, 8, 9, 10, 11, 12, 13], ]
monday1.correspond_class = ['A', 'B']
monday1.classroom_ls = ['220', '210']
monday1.teacher_ls = ['张艳峰', '胡艳敏']

# Monday 第2节课
monday2 = Class()
monday2.class_property = ['F', 'F', 'F']
monday2.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
monday2.class_ch_name_ls = ['基础法语（1）', '基础法语（1）', '基础法语（1）']
monday2.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
monday2.correspond_class = ['PA', 'PB', 'PC']
monday2.classroom_ls = ['122', '120', '108']
monday2.teacher_ls = ['马锐', '李俊仙', '武婧岚']

# Monday 第3节课
monday3 = Class()
monday3.class_property = ['F', 'F', 'F']
monday3.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
monday3.class_ch_name_ls = ['基础法语（1）', '基础法语（1）', '基础法语（1）']
monday3.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], ]
monday3.correspond_class = ['PA', 'PB', 'PC']
monday3.classroom_ls = ['122', '120', '108']
monday3.teacher_ls = ['马锐', '李俊仙', '武婧岚']

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
tuesday0.class_property = ['AB', 'AB']
tuesday0.class_fr_name_ls = ['Cours Mathématiques', 'Cours Mathématiques']
tuesday0.class_ch_name_ls = ['高等数学（1）', '高等数学（1）']
tuesday0.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17], ]
tuesday0.correspond_class = ['A', 'B']
tuesday0.classroom_ls = ['208', '210']
tuesday0.teacher_ls = ['谷瑞娟', '关静']

# Tuesday 第1节课
tuesday1 = Class()
tuesday1.class_property = ['F', 'F', 'F']
tuesday1.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
tuesday1.class_ch_name_ls = ['基础法语（1）', '基础法语（1）', '基础法语（1）']
tuesday1.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17], ]
tuesday1.correspond_class = ['PA', 'PB', 'PC']
tuesday1.classroom_ls = ['122', '120', '108']
tuesday1.teacher_ls = ['马锐', '李俊仙', '武婧岚']

# Tuesday 第2节课
tuesday2 = Class()
tuesday2.class_property = ['F', 'F', 'F']
tuesday2.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
tuesday2.class_ch_name_ls = ['基础法语（1）', '基础法语（1）', '基础法语（1）']
tuesday2.correspond_week = [
    [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17],
    [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17],
    [6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17],
]
tuesday2.correspond_class = ['PA', 'PB', 'PC']
tuesday2.classroom_ls = ['122', '120', '108']
tuesday2.teacher_ls = ['马锐', '李俊仙', '武婧岚']

# Tuesday 第3节课
tuesday3 = Class()
tuesday3.class_property = ['all']
tuesday3.class_fr_name_ls = ['Cours Sport']
tuesday3.class_ch_name_ls = ['体育1']
tuesday3.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
tuesday3.correspond_class = ['all']
tuesday3.classroom_ls = []
tuesday3.teacher_ls = []

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
wednesday0.class_property = ['F', 'F', 'F']
wednesday0.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
wednesday0.class_ch_name_ls = ['基础法语（1）', '基础法语（1）', '基础法语（1）']
wednesday0.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
wednesday0.correspond_class = ['PA', 'PB', 'PC']
wednesday0.classroom_ls = ['122', '120', '108']
wednesday0.teacher_ls = ['马锐', '李俊仙', '武婧岚']

# Wednesday 第1节课
wednesday1 = Class()
wednesday1.class_property = ['F', 'F', 'F']
wednesday1.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
wednesday1.class_ch_name_ls = ['基础法语（1）', '基础法语（1）', '基础法语（1）']
wednesday1.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14], ]
wednesday1.correspond_class = ['PA', 'PB', 'PC']
wednesday1.classroom_ls = ['122', '120', '108']
wednesday1.teacher_ls = ['王萱', '陈佳音', '王玥']

# Wednesday 第2节课
wednesday2 = Class()
wednesday2.class_property = ['P', 'P', 'P', 'P']
wednesday2.class_fr_name_ls = ['TD Mathématiques', 'TD Mathématiques', 'TD Physiques', 'TD Physiques']
wednesday2.class_ch_name_ls = ['高等数学（1）习题课', '高等数学（1）习题课', '基础物理（上）习题课', '基础物理（上）习题课']
wednesday2.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [7, 9, 10, 11, 12, 13, 14],
                          [7, 9, 10, 11, 12, 13, 14], ]
wednesday2.correspond_class = ['PB', 'PD', 'PB', 'PD']
wednesday2.classroom_ls = ['212', '210', '220', '122']
wednesday2.teacher_ls = ['谷瑞娟', '关静', '张艳峰', '胡艳敏']

# Wednesday 第3节课
wednesday3 = Class()
wednesday3.class_property = ['P', 'P', 'P', 'P']
wednesday3.class_fr_name_ls = ['TD Mathématiques', 'TD Mathématiques', 'TD Physiques', 'TD Physiques']
wednesday3.class_ch_name_ls = ['高等数学（1）习题课', '高等数学（1）习题课', '基础物理（上）习题课', '基础物理（上）习题课']
wednesday3.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [9, 10, 11, 12, 13, 14],
                          [9, 10, 11, 12, 13, 14], ]
wednesday3.correspond_class = ['PA', 'PC', 'PA', 'PC']
wednesday3.classroom_ls = ['212', '210', '309', '310']
wednesday3.teacher_ls = ['谷瑞娟', '关静', '张艳峰', '胡雪兰']

# Wednesday 第4节课
wednesday4 = Class()
wednesday4.class_property = ['all']
wednesday4.class_fr_name_ls = ['Cours Politique']
wednesday4.class_ch_name_ls = ['中国近现代史纲要及实践']
wednesday4.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14], ]
wednesday4.correspond_class = ['all']
wednesday4.classroom_ls = ['教室201']
wednesday4.teacher_ls = ['刘世山']

wednesday_ls = (wednesday0, wednesday1, wednesday2, wednesday3, wednesday4)

# Thursday 第0节课
thursday0 = Class()
thursday0.class_property = ['AB', 'AB']
thursday0.class_fr_name_ls = ['Cours Mathématiques', 'Cours Mathématiques']
thursday0.class_ch_name_ls = ['高等数学（1）', '高等数学（1）']
thursday0.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday0.correspond_class = ['A', 'B']
thursday0.classroom_ls = ['220', '201']
thursday0.teacher_ls = ['谷瑞娟', '关静']

# Thursday 第1节课
thursday1 = Class()
thursday1.class_property = ['F', 'F', 'F', 'AB', 'AB']
thursday1.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français', 'Cours Physique', 'Cours Physique']
thursday1.class_ch_name_ls = ['基础法语（1）', '基础法语（1）', '基础法语（1）', '基础物理（1）', '基础物理（1）']
thursday1.correspond_week = [
                          [14, 15, 16, 17],
                          [14, 15, 16, 17],
                          [14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13],
                          [6, 7, 8, 9, 10, 11, 12, 13], ]
thursday1.correspond_class = ['A', 'B', 'B', 'B', 'B']
thursday1.classroom_ls = ['122', '120', '108', '220', '210']
thursday1.teacher_ls = ['王萱', '陈佳音', '王玥', '张艳峰', '胡艳敏']

# Thursday 第2节课
thursday2 = Class()
thursday2.class_property = ['F', 'F', 'F']
thursday2.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
thursday2.class_ch_name_ls = ['基础法语（1）', '基础法语（1）', '基础法语（1）']
thursday2.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday2.correspond_class = ['PA', 'PB', 'PC']
thursday2.classroom_ls = ['122', '120', '108']
thursday2.teacher_ls = ['王萱', '陈佳音', '王玥']

# Thursday 第3节课
thursday3 = Class()
thursday3.class_property = ['F', 'F', 'F']
thursday3.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
thursday3.class_ch_name_ls = ['基础法语（1）', '基础法语（1）', '基础法语（1）']
thursday3.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12],
                          [6, 7, 8, 9, 10, 11, 12],
                          [6, 7, 8, 9, 10, 11, 12], ]
thursday3.correspond_class = ['PA', 'PB', 'PC']
thursday3.classroom_ls = ['122', '207', '208']
thursday3.teacher_ls = ['王萱', '陈佳音', '王玥']

# Thursday 第4节课
thursday4 = Class()
thursday4.class_property = ['all']
thursday4.class_fr_name_ls = ['Cours Politique']
thursday4.class_ch_name_ls = ['中国近现代史纲要及实践']
thursday4.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14], ]
thursday4.correspond_class = ['all']
thursday4.classroom_ls = ['教室201']
thursday4.teacher_ls = ['刘世山']

thursday_ls = (thursday0, thursday1, thursday2, thursday3, thursday4)

# Friday 第0节课
friday0 = Class()
friday0.class_property = ['F', 'F', 'F']
friday0.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
friday0.class_ch_name_ls = ['基础法语（1）', '基础法语（1）', '基础法语（1）']
friday0.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
friday0.correspond_class = ['PA', 'PB', 'PC']
friday0.classroom_ls = ['122', '120', '108']
friday0.teacher_ls = ['王萱', '陈佳音', '王玥']

# Friday 第1节课
friday1 = Class()
friday1.class_property = ['F', 'F', 'F']
friday1.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
friday1.class_ch_name_ls = ['基础法语（1）', '基础法语（1）', '基础法语（1）']
friday1.correspond_week = [
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
                          [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
friday1.correspond_class = ['PA', 'PB', 'PC']
friday1.classroom_ls = ['122', '120', '108']
friday1.teacher_ls = ['王萱', '陈佳音', '王玥']

# Friday 第2节课
friday2 = Class()
friday2.class_property = ['AB', 'AB', 'P', 'P', 'P', 'P']
friday2.class_fr_name_ls = ['Cours Mathématiques', 'Cours Mathématiques', 'Cours  Anglais', 'Cours  Anglais', 'Cours  Anglais', 'Cours  Anglais']
friday2.class_ch_name_ls = ['高等数学（1）', '高等数学（1）', '大学英语（1）', '大学英语（1）', '大学英语（1）', '大学英语（1）']
friday2.correspond_week = [
                          [6],
                          [6],
                          [7, 8],
                          [7, 8],
                          [7, 8],
                          [7, 8], ]
friday2.correspond_class = ['A', 'B', 'PA', 'PB', 'PC', 'PD']
friday2.classroom_ls = ['201', '210', '107', '108', '120', '122']
friday2.teacher_ls = ['谷瑞娟', '关静', '刘东亮', '刘成盼', '外教Eric', '曹迪']

# Friday 第3节课
friday3 = Class()
friday3.class_property = ['all']
friday3.class_fr_name_ls = ['Cours Politique']
friday3.class_ch_name_ls = ['中国近现代史纲要及实践']
friday3.correspond_week = [
                          [6, 7, 8, 9], ]
friday3.correspond_class = ['all']
friday3.classroom_ls = ['教室201']
friday3.teacher_ls = ['刘世山']

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
saturday0.class_property = []
saturday0.class_fr_name_ls = []
saturday0.class_ch_name_ls = []
saturday0.correspond_week = []
saturday0.correspond_class = []
saturday0.classroom_ls = []
saturday0.teacher_ls = []

# Saturday 第1节课
saturday1 = Class()
saturday1.class_property = []
saturday1.class_fr_name_ls = []
saturday1.class_ch_name_ls = []
saturday1.correspond_week = []
saturday1.correspond_class = []
saturday1.classroom_ls = []
saturday1.teacher_ls = []

# Saturday 第2节课
saturday2 = Class()
saturday2.class_property = []
saturday2.class_fr_name_ls = []
saturday2.class_ch_name_ls = []
saturday2.correspond_week = []
saturday2.correspond_class = []
saturday2.classroom_ls = []
saturday2.teacher_ls = []

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

schedule_20 = [monday_ls, tuesday_ls, wednesday_ls, thursday_ls, friday_ls, saturday_ls]
