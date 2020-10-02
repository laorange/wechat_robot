import time

t_refer_1_week = '2020-08-31'  # 本学期第一周周一的日期
t_refer_1_week = t_refer_1_week + ' 00:00:00'
t_refer_strp = time.strptime(t_refer_1_week, '%Y-%m-%d %H:%M:%S')
t_refer = time.mktime(t_refer_strp)


def get_time_time(t_delay: int or float = 0):
    return time.time() + t_delay


def determine_week():
    t_now = time.time()
    week = int((t_now - t_refer) // 604800)
    return week


def determine_what_day():
    what_day = time.strftime('%A', time.localtime())
    return what_day


def determine_date(t_delay: int or float = 0):
    date = time.strftime('%Y-%m-%d', time.localtime(time.time() + t_delay))
    return date


def compute_week_num(target_day: str):
    target_day_final_str = target_day + ' 00:00:00'
    t_target_strp = time.strptime(target_day_final_str, '%Y-%m-%d %H:%M:%S')
    t_target = time.mktime(t_target_strp)
    week = int((t_target - t_refer) // 604800)
    return week


if __name__ == "__main__":
    print(f't_refer:{t_refer}')
    print(f"time:{get_time_time()}")
    print(f'week:{determine_week()}')
    print(f'what_day:{determine_what_day()}')
    print(f'date:{determine_date(86400)}')
    print(compute_week_num('2020-09-26'))

    start_date = determine_date()
    start_hms = '00:12:00'
    start_time = start_date + ' ' + start_hms
    t_start_strp = time.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    t_start = time.mktime(t_start_strp)
    time_for_sleep = t_start - time.time()
    if time_for_sleep < 0:
        time_for_sleep = t_start - get_time_time(-86400)
        print('今日的自动推送已错过，自动生成明日的推送任务')
        if time_for_sleep < 0:
            raise Exception("main l24逻辑错误")

    print(time_for_sleep)
