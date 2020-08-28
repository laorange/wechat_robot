import time

t_refer_1_week = '2020-08-31'  # 本学期第一周周一的日期
t_refer_1_week = t_refer_1_week+' 00:00:00'
t_refer_strp = time.strptime(t_refer_1_week, '%Y-%m-%d %H:%M:%S')
t_refer = time.mktime(t_refer_strp)


def determine_week():
    t_now = time.time()
    week = int((t_now - t_refer) // 604800)
    return week


def determine_what_day():
    what_day = time.strftime('%A', time.localtime())
    return what_day


def determine_date():
    date = time.strftime('%Y-%m-%d', time.localtime())
    return date


if __name__ == "__main__":
    print(f't_refer:{t_refer}')
    print(f'week:{determine_week()}')
    print(f'what_day:{determine_what_day()}')
    print(f'date:{determine_date()}')
