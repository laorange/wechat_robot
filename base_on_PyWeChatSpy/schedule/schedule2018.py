# coding: utf-8

# 2018级课表 更新时间:2020-08-29 16:41
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
monday0.class_property = ['all', 'all', 'all', 'all']
monday0.class_fr_name_ls = ['Physique', 'Physique', 'Physique', 'Physique']
monday0.class_ch_name_ls = []
monday0.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
monday0.correspond_class = ['all', 'all', 'all', 'all']
monday0.classroom_ls = ['201', '201', '201', '201']
monday0.teacher_ls = ['经典物理（上）', '张艳峰/', 'Joël', '王亚如']

# Monday 第1节课
monday1 = Class()
monday1.class_property = ['all', 'all']
monday1.class_fr_name_ls = ['Cours  Français', 'Cours  Français']
monday1.class_ch_name_ls = []
monday1.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
monday1.correspond_class = ['all', 'all']
monday1.classroom_ls = ['教室201', '教室201']
monday1.teacher_ls = ['高级写作', '马锐']

# Monday 第2节课
monday2 = Class()
monday2.class_property = ['P', 'P', 'P', 'P', 'P', 'P']
monday2.class_fr_name_ls = ['TD physique', 'TD physique', 'TD physique', 'Cours  Anglais', 'Eric，PC 107', 'Adil，PD 210']
monday2.class_ch_name_ls = ['综合英语（1）', '综合英语（1）', '综合英语（1）', '综合英语（1）', '综合英语（1）', '综合英语（1）']
monday2.correspond_week = [
                          [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
                          [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
                          [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], ]
monday2.correspond_class = ['PA', 'PB', 'PB', 'PC', 'PD', 'PD']
monday2.classroom_ls = ['212', '220', '220', '107', '210', '210']
monday2.teacher_ls = ['经典物理（上）习题课', '王亚如', '秦哲']

# Monday 第3节课
monday3 = Class()
monday3.class_property = ['P', 'P', 'P', 'P', 'P', 'P']
monday3.class_fr_name_ls = ['TD physique', 'TD physique', 'TD physique', 'Cours  Anglais', 'Eric，PA  107', 'Adil，PB  108']
monday3.class_ch_name_ls = ['综合英语（1）', '综合英语（1）', '综合英语（1）', '综合英语（1）', '综合英语（1）', '综合英语（1）']
monday3.correspond_week = [
                          [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
                          [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
                          [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], ]
monday3.correspond_class = ['PC', 'PD', 'PD', 'PA', 'PB', 'PB']
monday3.classroom_ls = ['212', '210', '210', '107', '108', '108']
monday3.teacher_ls = ['经典物理（上）习题课', '张艳峰', '秦哲/王亚如']

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
                          ['1', '18'], ]
tuesday0.correspond_class = ['all']
tuesday0.classroom_ls = ['220']
tuesday0.teacher_ls = ['徐登明']

# Tuesday 第1节课
tuesday1 = Class()
tuesday1.class_property = ['all', 'all', 'all', 'all']
tuesday1.class_fr_name_ls = ['Physique', 'Physique', 'Physique', 'Physique']
tuesday1.class_ch_name_ls = []
tuesday1.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
tuesday1.correspond_class = ['all', 'all', 'all', 'all']
tuesday1.classroom_ls = ['201', '201', '201', '201']
tuesday1.teacher_ls = ['经典物理（上）', '张艳峰/', 'Joël', '王亚如']

# Tuesday 第2节课
tuesday2 = Class()
tuesday2.class_property = ['all', 'all']
tuesday2.class_fr_name_ls = ['Cours  Français', 'Julien  FA     212', 'Caroline  FB   208', 'TD Mathématiques']
tuesday2.class_ch_name_ls = ['中级法语3', '中级法语3', '中级法语3', '高等数学（5）习题课']
tuesday2.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
tuesday2.correspond_class = ['all', 'all']
tuesday2.classroom_ls = ['212', '208', '208', '309']
tuesday2.teacher_ls = ['林洁', '林洁', '林洁', '林洁']

# Tuesday 第3节课
tuesday3 = Class()
tuesday3.class_property = ['all', 'all']
tuesday3.class_fr_name_ls = ['Cours  Français', 'Thomas   FC   212', 'TD Mathématiques']
tuesday3.class_ch_name_ls = ['中级法语3', '中级法语3', '高等数学（5）习题课']
tuesday3.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
tuesday3.correspond_class = ['all', 'all']
tuesday3.classroom_ls = ['212', '212', '309', '310']
tuesday3.teacher_ls = ['林洁', '徐登明', '徐登明']

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
                          ['1', '18'], ]
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
wednesday2.class_property = ['all']
wednesday2.class_fr_name_ls = ['Cours  Français', 'Julien FA   107', 'Caroline    FB   108', 'Thomas   FC   120']
wednesday2.class_ch_name_ls = ['中级法语1', '中级法语1', '中级法语1', '中级法语1']
wednesday2.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
wednesday2.correspond_class = ['all']
wednesday2.classroom_ls = ['107', '108', '120', '120']
wednesday2.teacher_ls = []

# Wednesday 第3节课
wednesday3 = Class()
wednesday3.class_property = ['all', 'all']
wednesday3.class_fr_name_ls = []
wednesday3.class_ch_name_ls = []
wednesday3.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ]
wednesday3.correspond_class = ['all', 'all']
wednesday3.classroom_ls = ['教室220', '教室220']
wednesday3.teacher_ls = ['计算机编程', '马龙']

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
thursday0.class_property = ['P', 'P', 'P', 'P', 'P']
thursday0.class_fr_name_ls = ['Cours  Anglais', 'Eric，PA  309', 'Adil，PB  310', 'TD physique', 'TD physique']
thursday0.class_ch_name_ls = ['综合英语（1）   1-18周', '综合英语（1）   1-18周', '综合英语（1）   1-18周', '综合英语（1）   1-18周', '综合英语（1）   1-18周']
thursday0.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday0.correspond_class = ['PA', 'PB', 'PB', 'PC', 'PD']
thursday0.classroom_ls = ['309', '310', '310', '208', '212']
thursday0.teacher_ls = ['经典物理（上）习题课', '张艳峰', '秦哲/', '王亚如', '王亚如']

# Thursday 第1节课
thursday1 = Class()
thursday1.class_property = ['P', 'P', 'P', 'P', 'P']
thursday1.class_fr_name_ls = ['Cours  Anglais', 'Eric，PC  309', 'Adil，PD  310', 'TD physique', 'TD physique']
thursday1.class_ch_name_ls = ['综合英语（1）   1-18周', '综合英语（1）   1-18周', '综合英语（1）   1-18周', '综合英语（1）   1-18周', '综合英语（1）   1-18周']
thursday1.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday1.correspond_class = ['PC', 'PD', 'PD', 'PA', 'PB']
thursday1.classroom_ls = ['309', '310', '310', '208', '210']
thursday1.teacher_ls = ['经典物理（上）习题课', '王亚如', '秦哲', '秦哲', '秦哲']

# Thursday 第2节课
thursday2 = Class()
thursday2.class_property = ['all', 'all']
thursday2.class_fr_name_ls = ['TD Mathématiques', 'Cours  Français', 'Julien FA 107', 'Caroline FB 207']
thursday2.class_ch_name_ls = ['高等数学（5）习题课', '中级法语1', '中级法语1', '中级法语1']
thursday2.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday2.correspond_class = ['all', 'all']
thursday2.classroom_ls = ['309', '107', '207', '207']
thursday2.teacher_ls = ['林洁']

# Thursday 第3节课
thursday3 = Class()
thursday3.class_property = ['all']
thursday3.class_fr_name_ls = ['TD Mathématiques', 'TD Mathématiques']
thursday3.class_ch_name_ls = ['高等数学（5）习题课', '高等数学（5）习题课']
thursday3.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday3.correspond_class = ['all']
thursday3.classroom_ls = ['309', '310']
thursday3.teacher_ls = ['林洁', '徐登明']

# Thursday 第4节课
thursday4 = Class()
thursday4.class_property = ['all']
thursday4.class_fr_name_ls = ['Cours  Français', 'Thomas', 'FC   120']
thursday4.class_ch_name_ls = ['中级法语3', '中级法语3', '中级法语3']
thursday4.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
thursday4.correspond_class = ['all']
thursday4.classroom_ls = ['120', '120', '120']
thursday4.teacher_ls = []

thursday_ls = (thursday0, thursday1, thursday2, thursday3, thursday4) 

# Friday 第0节课
friday0 = Class()
friday0.class_property = ['all', 'all', 'all', 'all']
friday0.class_fr_name_ls = ['Physique', 'Physique', 'Physique', 'Physique']
friday0.class_ch_name_ls = []
friday0.correspond_week = [
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 
                          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ]
friday0.correspond_class = ['all', 'all', 'all', 'all']
friday0.classroom_ls = ['220', '220', '220', '220']
friday0.teacher_ls = ['经典物理（上）', '张艳峰/', 'Joël', '王亚如']

# Friday 第1节课
friday1 = Class()
friday1.class_property = ['all']
friday1.class_fr_name_ls = ['Mathématiques']
friday1.class_ch_name_ls = ['高等数学（5）']
friday1.correspond_week = [
                          ['1', '18'], ]
friday1.correspond_class = ['all']
friday1.classroom_ls = ['201']
friday1.teacher_ls = ['徐登明']

# Friday 第2节课
friday2 = Class()
friday2.class_property = ['all', 'all', 'AB', 'AB']
friday2.class_fr_name_ls = []
friday2.class_ch_name_ls = []
friday2.correspond_week = [
                          [2, 3, 4, 5, 6, 7, 8], 
                          [2, 3, 4, 5, 6, 7, 8], 
                          [3, 4, 5, 6, 7, 8, 9], 
                          ['11'], ]
friday2.correspond_class = ['all', 'all', 'B', 'B']
friday2.classroom_ls = ['教室220', '教室220', '教室125', '教室125']
friday2.teacher_ls = ['计算机编程', '马龙', '计算机编程', '马龙、孙犇渊']

# Friday 第3节课
friday3 = Class()
friday3.class_property = ['AB', 'AB']
friday3.class_fr_name_ls = []
friday3.class_ch_name_ls = []
friday3.correspond_week = [
                          [3, 4, 5, 6, 7, 8, 9], 
                          ['11'], ]
friday3.correspond_class = ['A', 'A']
friday3.classroom_ls = ['教室125', '教室125']
friday3.teacher_ls = ['计算机编程', '马龙、孙犇渊']

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

schedule_2018 = [monday_ls, tuesday_ls, wednesday_ls, thursday_ls, friday_ls]
