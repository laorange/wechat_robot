# coding: utf-8

# 2019级课表 更新时间:2020-08-14 15:29
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
monday0.class_property = ['AB', 'AB', 'AB', 'AB']
monday0.class_fr_name_ls = ['Cours Physique', 'Cours Physique', 'Cours Physique', 'Cours Physique']
monday0.class_ch_name_ls = ['普通物理（上）', '普通物理（上）', '普通物理（上）', '普通物理（上）']
monday0.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17]]
monday0.correspond_class = ['A', 'B', 'A', 'B']
monday0.classroom_ls = ['220', '210', '220', '210']
monday0.teacher_ls = ['胡雪兰', '胡艳敏', '李文', '徐舟']

# Monday 第1节课
monday1 = Class()
monday1.class_property = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
monday1.class_fr_name_ls = ['TD Mathématiques', 'TD Mathématiques', 'TD Mathématiques', 'TD Physiques', 'TD Physiques', 'TD Physiques', 'TD Physiques', 'TD Physiques', 'TD Physiques']
monday1.class_ch_name_ls = ['高等数学(3)习题课', '高等数学(3)习题课', '高等数学(3)习题课', '高等数学(3)习题课', '普通物理（上）习题课', '普通物理（上）习题课', '普通物理（上）习题课', '普通物理（上）习题课', '普通物理（上）习题课']
monday1.correspond_week = [[9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17]]
monday1.correspond_class = ['PB', 'PB', 'PD', 'PA', 'PA', 'PA', 'PA', 'PC', 'PC']
monday1.classroom_ls = ['207', '207', '208', '309', '309', '309', '309', '310', 'PC310']
monday1.teacher_ls = ['刘文然', '刘文然', '田俊改', '胡雪兰', '胡雪兰', '胡雪兰', '李文', 'Joël', '秦哲']

# Monday 第2节课
monday2 = Class()
monday2.class_property = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
monday2.class_fr_name_ls = ['TD Mathématiques', 'TD Mathématiques', 'TD Mathématiques', 'TD Physiques', 'TD Physiques', 'TD Physiques', 'TD Physiques', 'TD Physiques']
monday2.class_ch_name_ls = ['高等数学(3)习题课', '高等数学(3)习题课', '高等数学(3)习题课', '高等数学(3)习题课', '普通物理（上）习题课', '普通物理（上）习题课', '普通物理（上）习题课', '普通物理（上）习题课']
monday2.correspond_week = [[10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17]]
monday2.correspond_class = ['PA', 'PA', 'PC', 'PB', 'PB', 'PB', 'PD', 'PD']
monday2.classroom_ls = ['207', '207', '208', '309', '309', '309', '310', '310']
monday2.teacher_ls = ['刘文然', '刘文然', '关静', '胡艳敏', '胡艳敏', '胡艳敏', '胡雪兰', '李文']

# Monday 第3节课
monday3 = Class()
monday3.class_property = ['all', 'all']
monday3.class_fr_name_ls = ['Cours Sport', 'Cours Sport']
monday3.class_ch_name_ls = []
monday3.correspond_week = [[10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
monday3.correspond_class = ['all', 'all']
monday3.classroom_ls = []
monday3.teacher_ls = []

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
tuesday0.class_property = ['P', 'P', 'P', 'P', 'P']
tuesday0.class_fr_name_ls = ['Cours  Anglais', 'Cours  Anglais', 'Cours  Anglais', 'Cours  Anglais', 'Cours  Anglais']
tuesday0.class_ch_name_ls = ['大学英语（3 ）', '大学英语（3 ）', '大学英语（3 ）', '大学英语（3 ）', '大学英语（3 ）']
tuesday0.correspond_week = [[['Cours Politique', '毛泽东思想和中国特色社会', '主义理论体系概论（1）', '1-18周', 'AB班  郝锦花', '教室 220']], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
tuesday0.correspond_class = ['PA', 'PA', 'PB', 'PC', 'PD']
tuesday0.classroom_ls = ['107', '107', '108', '120', '122']
tuesday0.teacher_ls = ['刘成盼', '刘成盼', '刘东亮', '王坤', '罗旭']

# Tuesday 第1节课
tuesday1 = Class()
tuesday1.class_property = ['AB', 'AB', 'AB', 'AB', 'AB']
tuesday1.class_fr_name_ls = ['Cours Physique', 'Cours Physique', 'Cours Physique', 'Cours Physique', 'Cours Physique']
tuesday1.class_ch_name_ls = ['普通物理（上）', '普通物理（上）', '普通物理（上）', '普通物理（上）', '普通物理（上）']
tuesday1.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17]]
tuesday1.correspond_class = ['A', 'A', 'B', 'A', 'B']
tuesday1.classroom_ls = ['220', '220', '210', '220', '210']
tuesday1.teacher_ls = ['胡雪兰', '胡雪兰', '胡艳敏', '李文', '徐舟']

# Tuesday 第2节课
tuesday2 = Class()
tuesday2.class_property = ['all', 'all', 'all', 'all', 'all']
tuesday2.class_fr_name_ls = ['Cours Mathématiques', 'Cours Mathématiques', 'Cours chemie', 'Cours chemie', 'Cours chemie']
tuesday2.class_ch_name_ls = ['高等数学（3）', '高等数学（3）', '高等数学（3）', '化学1', '化学1']
tuesday2.correspond_week = [[9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 2, 4, 6, 8, 10, 12, 14, 16], [0, 2, 4, 6, 8, 10, 12, 14, 16], [0, 2, 4, 6, 8, 10, 12, 14, 16], ['11', '13']]
tuesday2.correspond_class = ['all', 'all', 'all', 'all', 'all']
tuesday2.classroom_ls = ['教室201', '教室201', '201', '201', '201']
tuesday2.teacher_ls = ['田俊改', '田俊改', '王亚如', '王亚如', '杜娟']

# Tuesday 第3节课
tuesday3 = Class()
tuesday3.class_property = ['P', 'P', 'P', 'P']
tuesday3.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français', 'Cours  Français']
tuesday3.class_ch_name_ls = ['中级法语1', '中级法语1', '中级法语1', '中级法语1']
tuesday3.correspond_week = [['11', '13'], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
tuesday3.correspond_class = ['PA', 'PB', 'PC', 'PD']
tuesday3.classroom_ls = ['107', '108', '120', '122']
tuesday3.teacher_ls = ['外教1', '外教2', '马锐', '王玥']

# Tuesday 第4节课
tuesday4 = Class()
tuesday4.class_property = ['all', 'all', 'all']
tuesday4.class_fr_name_ls = ['Cours Politique', 'Cours Politique', 'AB班  郝锦花']
tuesday4.class_ch_name_ls = ['主义理论体系概论（1）', '主义理论体系概论（1）', '主义理论体系概论（1）']
tuesday4.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
tuesday4.correspond_class = ['all', 'all', 'all']
tuesday4.classroom_ls = ['220', '220', '220']
tuesday4.teacher_ls = ['毛泽东思想和中国特色社会', '毛泽东思想和中国特色社会', '郝锦花']

tuesday_ls = (tuesday0, tuesday1, tuesday2, tuesday3, tuesday4) 

# Wednesday 第0节课
wednesday0 = Class()
wednesday0.class_property = ['all', 'all']
wednesday0.class_fr_name_ls = ['Cours chemie', 'Cours chemie']
wednesday0.class_ch_name_ls = ['化学1', '化学1']
wednesday0.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17]]
wednesday0.correspond_class = ['all', 'all']
wednesday0.classroom_ls = ['201', '201']
wednesday0.teacher_ls = ['王亚如', '杜娟']

# Wednesday 第1节课
wednesday1 = Class()
wednesday1.class_property = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
wednesday1.class_fr_name_ls = ['TD Mathématiques', 'TD Mathématiques', 'TD Mathématiques', 'TD Physiques', 'TD Physiques', 'TD Physiques', 'TD Physiques', 'TD Physiques']
wednesday1.class_ch_name_ls = ['高等数学(3)习题课', '高等数学(3)习题课', '高等数学(3)习题课', '高等数学(3)习题课', '普通物理（上）习题课', '普通物理（上）习题课', '普通物理（上）习题课', '普通物理（上）习题课']
wednesday1.correspond_week = [[10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17]]
wednesday1.correspond_class = ['PB', 'PB', 'PD', 'PB', 'PB', 'PB', 'PD', 'PD']
wednesday1.classroom_ls = ['210', '210', '208', '309', '309', '309', '310', '310']
wednesday1.teacher_ls = ['刘文然', '刘文然', '关静', '胡艳敏', '胡艳敏', '胡艳敏', '胡雪兰', '李文']

# Wednesday 第2节课
wednesday2 = Class()
wednesday2.class_property = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
wednesday2.class_fr_name_ls = ['TD Mathématiques', 'TD Mathématiques', 'TD Mathématiques', 'TD Physiques', 'TD Physiques', 'TD Physiques', 'TD Physiques', 'TD Physiques', 'TD Physiques']
wednesday2.class_ch_name_ls = ['高等数学(3)习题课', '高等数学(3)习题课', '高等数学(3)习题课', '高等数学(3)习题课', '普通物理（上）习题课', '普通物理（上）习题课', '普通物理（上）习题课', '普通物理（上）习题课', '普通物理（上）习题课']
wednesday2.correspond_week = [[10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17], [1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17]]
wednesday2.correspond_class = ['PA', 'PA', 'PC', 'PA', 'PA', 'PA', 'PA', 'PC', 'PC']
wednesday2.classroom_ls = ['207', '207', '122', '309', '309', '309', '309', '310', 'PC310']
wednesday2.teacher_ls = ['刘文然', '刘文然', '田俊改', '胡雪兰', '胡雪兰', '胡雪兰', '李文', 'Joël', '秦哲']

# Wednesday 第3节课
wednesday3 = Class()
wednesday3.class_property = ['P', 'P', 'P', 'P']
wednesday3.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français', 'Cours  Français']
wednesday3.class_ch_name_ls = ['中级法语1', '中级法语1', '中级法语1', '中级法语1']
wednesday3.correspond_week = [[10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
wednesday3.correspond_class = ['PA', 'PB', 'PC', 'PD']
wednesday3.classroom_ls = ['107', '108', '120', '122']
wednesday3.teacher_ls = ['外教1', '外教2', '马锐', '王玥']

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
thursday0.class_property = ['P', 'P', 'P']
thursday0.class_fr_name_ls = ['Cours  Français', 'Cours  Français', 'Cours  Français']
thursday0.class_ch_name_ls = ['中级法语1', '中级法语1', '中级法语1']
thursday0.correspond_week = [[['形势与政策2', '11-16周', '刘晓宇', 'AB班', '教室201']], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
thursday0.correspond_class = ['PC', 'PC', 'PD']
thursday0.classroom_ls = ['120', '120', '122']
thursday0.teacher_ls = ['马锐', '马锐', '李俊仙']

# Thursday 第1节课
thursday1 = Class()
thursday1.class_property = ['all']
thursday1.class_fr_name_ls = ['Cours Mathématiques', 'Cours Mathématiques']
thursday1.class_ch_name_ls = ['高等数学（3）', '高等数学（3）']
thursday1.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
thursday1.correspond_class = ['all']
thursday1.classroom_ls = ['教室201', '教室201']
thursday1.teacher_ls = ['田俊改', '田俊改']

# Thursday 第2节课
thursday2 = Class()
thursday2.class_property = ['AB', 'AB', 'AB', 'AB', 'all']
thursday2.class_fr_name_ls = ['Cours Physique', 'Cours Physique', 'Cours Physique', 'Cours Physique', 'travaux Pratiques', 'PhysiqueⅠ', 'PhysiqueⅠ', 'PhysiqueⅠ']
thursday2.class_ch_name_ls = ['普通物理（上）', '普通物理（上）', '普通物理（上）', '普通物理（上）', '普通物理（上）', '普通物理（上）', '物理实验Ⅰ', '物理实验Ⅰ']
thursday2.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], ['10'], ['10'], ['10'], ['10'], ['10'], [0, 1, 2, 3, 4, 5, 6, 7, 8]]
thursday2.correspond_class = ['A', 'B', 'A', 'B', 'all']
thursday2.classroom_ls = ['220', '210', '220', '210']
thursday2.teacher_ls = ['胡雪兰', '胡艳敏', '李文', '徐舟', '时间另通知', '时间另通知', '时间另通知', '时间另通知']

# Thursday 第3节课
thursday3 = Class()
thursday3.class_property = ['all']
thursday3.class_fr_name_ls = ['Travaux Pratiques', 'PhysiqueⅠ', 'PhysiqueⅠ']
thursday3.class_ch_name_ls = ['物理实验Ⅰ', '物理实验Ⅰ', '物理实验Ⅰ']
thursday3.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8]]
thursday3.correspond_class = ['all']
thursday3.classroom_ls = []
thursday3.teacher_ls = ['时间另通知', '时间另通知', '时间另通知']

# Thursday 第4节课
thursday4 = Class()
thursday4.class_property = ['all', 'all']
thursday4.class_fr_name_ls = []
thursday4.class_ch_name_ls = ['形势与政策2', '形势与政策2']
thursday4.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [10, 11, 12, 13, 14, 15]]
thursday4.correspond_class = ['all', 'all']
thursday4.classroom_ls = ['教室201', '教室201']
thursday4.teacher_ls = ['刘晓宇', '刘晓宇']

thursday_ls = (thursday0, thursday1, thursday2, thursday3, thursday4) 

# Friday 第0节课
friday0 = Class()
friday0.class_property = ['all']
friday0.class_fr_name_ls = ['Cours Mathématiques']
friday0.class_ch_name_ls = ['高等数学（3）']
friday0.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
friday0.correspond_class = ['all']
friday0.classroom_ls = ['教室201']
friday0.teacher_ls = ['田俊改']

# Friday 第1节课
friday1 = Class()
friday1.class_property = ['AB', 'AB', 'AB', 'AB', 'AB']
friday1.class_fr_name_ls = ['Cours Physique', 'Cours Physique', 'Cours Physique', 'Cours Physique', 'Cours Physique']
friday1.class_ch_name_ls = ['普通物理（上）', '普通物理（上）', '普通物理（上）', '普通物理（上）', '普通物理（上）']
friday1.correspond_week = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [9, 10, 11, 12, 13, 14, 15, 16, 17]]
friday1.correspond_class = ['A', 'A', 'B', 'A', 'B']
friday1.classroom_ls = ['220', '220', '210', '220', '210']
friday1.teacher_ls = ['胡雪兰', '胡雪兰', '胡艳敏', '李文', '徐舟']

# Friday 第2节课
friday2 = Class()
friday2.class_property = ['P', 'P']
friday2.class_fr_name_ls = ['Cours  Français', 'Cours  Français']
friday2.class_ch_name_ls = ['中级法语1', '中级法语1']
friday2.correspond_week = [[9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]]
friday2.correspond_class = ['PA', 'PB']
friday2.classroom_ls = ['107', '108']
friday2.teacher_ls = ['外教1', '外教2']

# Friday 第3节课
friday3 = Class()
friday3.class_property = []
friday3.class_fr_name_ls = []
friday3.class_ch_name_ls = []
friday3.correspond_week = []
friday3.correspond_class = []
friday3.classroom_ls = []
friday3.teacher_ls = []

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

schedule_2019 = [monday_ls, tuesday_ls, wednesday_ls, thursday_ls, friday_ls]
