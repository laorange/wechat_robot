import xlrd
import re

data = xlrd.open_workbook('2020-2021（1）Annee2.xlsx')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
# print(nrows,ncols)
# (36,11)

temp_list = []
for i in [8, 12, 20, 24, 30]:
    temp_list.append(table.row_values(i, start_colx=1, end_colx=11))

# print(len(temp_list))
# 5
# print(len(temp_list[0]))
# 10
x = temp_list[4][2]
# print(x)
x = x.split()
# print(x)
z = temp_list[1][2]
z = z.split()


# print(z)
def getindex(x):
    pattern_z = re.compile(r'周')
    for i, j in enumerate(x):
        result = pattern_z.search(j)
        if result:
            indexofx = i
            print(indexofx)
            break
    return indexofx


# print(temp_index)
# 4
temp_index = 4


def getfname(x, y=temp_index):
    fname = ''
    pattern_f = re.compile(r'[a-zA-Z]+')
    for i in range(y):
        result = pattern_f.search(x[i])
        if result:
            fname = fname + x[i] + ' '
    print(fname)
    return fname


def getcname(x, y=temp_index):
    cname = ''
    pattern_c = re.compile(r'[\u4E00-\u9FA5]+')
    for i in range(y):
        result = pattern_c.search(x[i])
        if result:
            cname = cname + x[i]
    print(cname)
    return cname


# print(x[temp_index])

# 这个函数暂时不能解决好几个周字的问题
def getweek(x, y=temp_index):
    list_week = []
    pattern_w = re.compile(r'-')
    if pattern_w.search(x[y]):
        startweek, finalweek = tuple(re.findall(re.compile(r'\d+'), x[y]))
        list_week = range(int(startweek), int(finalweek) + 1)
        print(list_week)
    else:
        print(re.findall(re.compile(r'\d+'), x[y]))
        list_week = map(int, re.findall(re.compile(r'\d+'), x[y]))
        print(list_week)
        for each in list_week:
            print(each)


def isclass_a(x=x):
    if 'A班' or 'AB班' or 'PA' or '教室201' in x:
        print('yes for a')
        return True
    else:
        print('no for a')
        return False


def isclass_b(x):
    if 'A班' or 'AB班' or 'PB' or '教室201' in x:
        print('yes for b')
        return True
    else:
        print('no for b')
        return False


def isclass_c(x):
    if 'B班' or 'AB班' or 'PC' or '教室201' in x:
        print('yes for c')
        return True
    else:
        print('no for c')
        return False


def isclass_d(x):
    if 'B班' or 'AB班' or 'PD' or '教室201' in x:
        print('yes for d')
        return True
    else:
        print('no for d')
        return False


# print(x)
# print(temp_list[1][1])
# isclass_a(temp_list[1][1].split())
# getindex(x)
# getfname(x)
# getcname(x)
# getweek(x)
# isclass_a(x)

# exec('isclass_{cid}(x)'.format(cid='a'))
class cellclass:
    def __init__(self, value):
        self.zhouindex = getindex(value)
        self.fname = getfname(value, self.zhouindex)
        self.cname = getcname(value, self.zhouindex)
        self.week = getweek(value, self.zhouindex)

    pass


# cellclass(temp_list[2][3].split())

def mainfuc(row, col, week, cid):
    '''
    :param row: 第几节课
    :param col: 星期几
    :param week: 第几周
    :param cid: 哪班的
    :return: 哪屋哪老师啥课,或者没有课
    '''
    # 变成index
    row -= 1
    col -= 1
    col1 = col * 2
    col2 = col1 + 1
    firststep = temp_list[row][col1]
    firststep = firststep.split()
    if exec('isclass_{cid}(firststep)'.format(cid=str(cid))):
        pass


mainfuc(1, 1, 1, cid='a')
