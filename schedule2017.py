# coding: utf-8

# 2017级课表 更新时间:2020-08-12 12:00
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
monday0.class_property = []
monday0.class_fr_name_ls = []
monday0.class_ch_name_ls = []
monday0.correspond_week = []
monday0.correspond_class = []
monday0.classroom_ls = []
monday0.teacher_ls = []

# Monday 第1节课
monday1 = Class()
monday1.class_property = ['all']
monday1.class_fr_name_ls = ['Mathématiques']
monday1.class_ch_name_ls = ['高等数学（6）']
monday1.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
monday1.correspond_class = ['all']
monday1.classroom_ls = ['220']
monday1.teacher_ls = ['林洁']

# Monday 第2节课
monday2 = Class()
monday2.class_property = ['P', 'P', 'P', 'P']
monday2.class_fr_name_ls = ['TD Mathématiques', 'Physique TD', 'Physique TD', 'Physique TD']
monday2.class_ch_name_ls = ['数学指导课', '物理指导课 TD', '物理指导课 TD', '物理指导课 TD']
monday2.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
monday2.correspond_class = ['PA', 'PC', 'PC', 'PD']
monday2.classroom_ls = ['309', '210', '210', '208']
monday2.teacher_ls = ['徐登明', 'Joël', '王亚如', '秦哲']

# Monday 第3节课
monday3 = Class()
monday3.class_property = ['P', 'P', 'P', 'P', 'P']
monday3.class_fr_name_ls = ['TD Mathématiques', 'TD Mathématiques', 'Physique TD', 'Physique TD', 'Physique TD']
monday3.class_ch_name_ls = ['数学指导课', '数学指导课', '物理指导课 TD', '物理指导课 TD', '物理指导课 TD']
monday3.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17]]
monday3.correspond_class = ['PC', 'PD', 'PA', 'PB', 'PB']
monday3.classroom_ls = ['309', '310', '210', '208', '208']
monday3.teacher_ls = ['徐登明', '林洁', '王亚如', '秦哲', '胡艳敏']

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
tuesday0.class_ch_name_ls = ['高等数学（6）']
tuesday0.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
tuesday0.correspond_class = ['all']
tuesday0.classroom_ls = ['220']
tuesday0.teacher_ls = ['林洁']

# Tuesday 第1节课
tuesday1 = Class()
tuesday1.class_property = ['all']
tuesday1.class_fr_name_ls = ['Physique']
tuesday1.class_ch_name_ls = []
tuesday1.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
tuesday1.correspond_class = ['all']
tuesday1.classroom_ls = ['220', '220', '220']
tuesday1.teacher_ls = ['经典物理（下）', 'Joël', '秦哲']

# Tuesday 第2节课
tuesday2 = Class()
tuesday2.class_property = ['P', 'P', 'P', 'P', 'P']
tuesday2.class_fr_name_ls = ['Cours  Anglais', 'Adil，PA  208', 'Eric，PB   212', 'Adil，PC 208', 'Eric，PD  212']
tuesday2.class_ch_name_ls = ['综合英语2', '综合英语2', '综合英语2', '综合英语2', '综合英语2']
tuesday2.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [1, 3, 5, 7, 9, 11, 13, 15, 17], [1, 3, 5, 7, 9, 11, 13, 15, 17], [1, 3, 5, 7, 9, 11, 13, 15, 17]]
tuesday2.correspond_class = ['PA', 'PB', 'PB', 'PC', 'PD']
tuesday2.classroom_ls = ['208', '212', '212', '208', '212']
tuesday2.teacher_ls = []

# Tuesday 第3节课
tuesday3 = Class()
tuesday3.class_property = ['P', 'P', 'P', 'P', 'P']
tuesday3.class_fr_name_ls = ['Cours  Français', 'Thomas PA    107', 'Caroline PC 120', 'Caroline PC 120', 'Caroline PC 120']
tuesday3.class_ch_name_ls = ['中级法语4', '中级法语4', '中级法语4', '中级法语4', '中级法语4']
tuesday3.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [10, 11, 12, 13, 14, 15, 16, 17], [10, 11, 12, 13, 14, 15, 16, 17], [10, 11, 12, 13, 14, 15, 16, 17], [10, 11, 12, 13, 14, 15, 16, 17]]
tuesday3.correspond_class = ['PA', 'PA', 'PB', 'PC', 'PD']
tuesday3.classroom_ls = ['107', '107', '108', '120', '122']
tuesday3.teacher_ls = ['武婧岚', '武婧岚', '武婧岚', '武婧岚', '陈佳音']

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
wednesday0.class_fr_name_ls = ['Physique']
wednesday0.class_ch_name_ls = []
wednesday0.correspond_week = [[0, 1, 2, 3], [0, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
wednesday0.correspond_class = ['all']
wednesday0.classroom_ls = ['220', '220', '220']
wednesday0.teacher_ls = ['经典物理（下）', 'Joël', '秦哲']

# Wednesday 第1节课
wednesday1 = Class()
wednesday1.class_property = ['all']
wednesday1.class_fr_name_ls = ['Cours Chimie']
wednesday1.class_ch_name_ls = ['化学3']
wednesday1.correspond_week = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
wednesday1.correspond_class = ['all']
wednesday1.classroom_ls = ['220', '220']
wednesday1.teacher_ls = ['王亚如', '牛一凡']

# Wednesday 第2节课
wednesday2 = Class()
wednesday2.class_property = ['all', 'P', 'P']
wednesday2.class_fr_name_ls = ['Cours  Français', 'Caroline/武婧岚 B 108', 'Cours  Anglais', 'Adil，PC 120', 'Eric，PD  122']
wednesday2.class_ch_name_ls = ['中级法语3   1-17周', '综合英语2', '综合英语2']
wednesday2.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
wednesday2.correspond_class = ['all', 'PC', 'PD']
wednesday2.classroom_ls = ['107', '108', '120', '122']
wednesday2.teacher_ls = ['马锐/Thomas']

# Wednesday 第3节课
wednesday3 = Class()
wednesday3.class_property = ['all', 'P', 'P']
wednesday3.class_fr_name_ls = ['Cours  Français', 'Cours  Anglais', 'Adil，PA 120', 'Eric，PB  122']
wednesday3.class_ch_name_ls = ['中级法语3   1-17周', '综合英语2', '综合英语2']
wednesday3.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
wednesday3.correspond_class = ['all', 'PA', 'PB']
wednesday3.classroom_ls = ['107', '108', '120', '122']
wednesday3.teacher_ls = ['王萱/Caroline', '陈佳音/Thomas']

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
thursday0.class_fr_name_ls = ['Cours  Français', 'Caroline  PB   108', 'Thomas  PD 122', 'Thomas  PD 122']
thursday0.class_ch_name_ls = ['中级法语4', '中级法语4', '中级法语4', '中级法语4']
thursday0.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
thursday0.correspond_class = ['PA', 'PB', 'PC', 'PD']
thursday0.classroom_ls = ['107', '108', '120', '122']
thursday0.teacher_ls = ['马锐', '马锐', '王萱', '王萱']

# Thursday 第1节课
thursday1 = Class()
thursday1.class_property = ['P', 'P', 'P', 'P']
thursday1.class_fr_name_ls = ['TD Mathématiques', 'Physique TD', 'Physique TD', 'Physique TD']
thursday1.class_ch_name_ls = ['数学指导课', '物理指导课 TD', '物理指导课 TD', '物理指导课 TD']
thursday1.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ['5', '10', '14'], ['5', '10', '14'], ['10', '14']]
thursday1.correspond_class = ['PA', 'PC', 'PD', 'PD']
thursday1.classroom_ls = ['309', '309', '207', '207']
thursday1.teacher_ls = ['徐登明', '王亚如', '秦哲', '胡艳敏']

# Thursday 第2节课
thursday2 = Class()
thursday2.class_property = ['P', 'P', 'P', 'P', 'P']
thursday2.class_fr_name_ls = ['TD Mathématiques', 'TD Mathématiques', 'Physique TD', 'Physique TD', 'Physique TD']
thursday2.class_ch_name_ls = ['数学指导课', '数学指导课', '物理指导课 TD', '物理指导课 TD', '物理指导课 TD']
thursday2.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ['10', '14'], ['10', '14'], ['5', '10', '14']]
thursday2.correspond_class = ['PC', 'PD', 'PA', 'PA', 'PB']
thursday2.classroom_ls = ['309', '310', '208', '208', '207']
thursday2.teacher_ls = ['徐登明', '林洁', 'Joël', '王亚如', '秦哲']

# Thursday 第3节课
thursday3 = Class()
thursday3.class_property = ['P', 'P', 'P', 'P', 'P']
thursday3.class_fr_name_ls = ['Méthodologies II', 'Julien  PC  120', 'Julien  PA  107', 'CarolinePB   108', 'CarolinePB   108']
thursday3.class_ch_name_ls = ['化学实验', '化学实验', '化学实验', '化学实验', '化学实验']
thursday3.correspond_week = [['5', '10', '14'], ['5', '10', '14'], ['5', '10', '14'], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
thursday3.correspond_class = ['PC', 'PA', 'PD', 'PA', 'PB']
thursday3.classroom_ls = ['120', '107', '108', '122']
thursday3.teacher_ls = ['高级写作', '高级写作', '马锐']

# Thursday 第4节课
thursday4 = Class()
thursday4.class_property = []
thursday4.class_fr_name_ls = []
thursday4.class_ch_name_ls = []
thursday4.correspond_week = []
thursday4.correspond_class = []
thursday4.classroom_ls = []
thursday4.teacher_ls = []

thursday_ls = (thursday0, thursday1, thursday2, thursday3, thursday4) 

# Friday 第0节课
friday0 = Class()
friday0.class_property = ['all']
friday0.class_fr_name_ls = ['Mathématiques']
friday0.class_ch_name_ls = ['高等数学（6）']
friday0.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
friday0.correspond_class = ['all']
friday0.classroom_ls = ['220']
friday0.teacher_ls = ['林洁']

# Friday 第1节课
friday1 = Class()
friday1.class_property = ['all', 'all']
friday1.class_fr_name_ls = ['Physique', 'Physique']
friday1.class_ch_name_ls = ['复变函数', '复变函数']
friday1.correspond_week = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
friday1.correspond_class = ['all', 'all']
friday1.classroom_ls = ['教室220', '220', '220']
friday1.teacher_ls = ['赵纬经', '经典物理（下）', '秦哲']

# Friday 第2节课
friday2 = Class()
friday2.class_property = ['AB', 'AB', 'AB', 'P', 'P']
friday2.class_fr_name_ls = []
friday2.class_ch_name_ls = ['复变函数', '复变函数', '复变函数', '化学实验', '化学实验']
friday2.correspond_week = [[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]]
friday2.correspond_class = ['A', 'A', 'A', 'PC', 'PD']
friday2.classroom_ls = ['教室210', '教室210', '教室210']
friday2.teacher_ls = ['习题课', '习题课', '赵纬经']

# Friday 第3节课
friday3 = Class()
friday3.class_property = ['AB', 'AB', 'AB']
friday3.class_fr_name_ls = []
friday3.class_ch_name_ls = ['复变函数', '复变函数', '复变函数']
friday3.correspond_week = [[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
friday3.correspond_class = ['B', 'B', 'B']
friday3.classroom_ls = ['教室210', '教室210', '教室210']
friday3.teacher_ls = ['习题课', '习题课', '赵纬经']

# Friday 第4节课
friday4 = Class()
friday4.class_property = ['all']
friday4.class_fr_name_ls = ['Movie']
friday4.class_ch_name_ls = []
friday4.correspond_week = []
friday4.correspond_class = ['all']
friday4.classroom_ls = ['220']
friday4.teacher_ls = []

friday_ls = (friday0, friday1, friday2, friday3, friday4) 

schedule_2017 = [monday_ls, tuesday_ls, wednesday_ls, thursday_ls, friday_ls]
