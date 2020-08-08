import xlrd
import re
data = xlrd.open_workbook(r'E:\2345Downloads\wechat_robot\2020-2021（1）Annee2.xlsx')
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
#print(nrows,ncols)
#(36,11)

temp_list=[]
for i in [8,12,20,24,30]:
    temp_list.append(table.row_values(i,start_colx=1,end_colx=10))
x=temp_list[4][2]
#print(x)
x=x.split()
#print(x)
pattern_z=re.compile(r'周')
for i,j in enumerate(x):
    result=pattern_z.search(j)
    if result:
        temp_index=i
        break

def getfname(x):
    fname=''
    pattern_f=re.compile(r'[a-zA-Z]+')
    for i in range(temp_index):
        result=pattern_f.search(x[i])
        if result:
            fname=fname+x[i]+' '
    print(fname)
    return fname

def getcname(x):
    cname=''
    pattern_c=re.compile(r'[\u4E00-\u9FA5]+')
    for i in range(temp_index):
        result = pattern_c.search(x[i])
        if result:
            cname = cname + x[i]
    print(cname)
    return cname
#print(result)

getfname(x)
getcname(x)

class kecheng:
    def __init__(self,value):
        temp=value.split()
