import time

t_refer_1_week = '2020-07-11'
t_refer_1_week = t_refer_1_week+' 00:00:00'
t_refer_strp = time.strptime(t_refer_1_week, '%Y-%m-%d %H:%M:%S')
t_refer = time.mktime(t_refer_strp)

t_now = time.time()
week = int((t_now - t_refer) // 604800)

what_day = time.strftime('%A', time.localtime())

date = time.strftime('%Y-%m-%d', time.localtime())

if __name__ == "__main__":
    print(f't_refer:{t_refer}')
    print(f'week:{week}')
    print(f'what_day:{what_day}')
    print(f'date:{date}')
