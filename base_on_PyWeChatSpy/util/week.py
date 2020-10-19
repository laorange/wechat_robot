import time
import traceback
from loguru import logger

t_refer_1_week = '2020-08-31'  # 本学期第一周周一的日期
t_refer_1_week = t_refer_1_week + ' 00:00:00'
t_refer_strp = time.strptime(t_refer_1_week, '%Y-%m-%d %H:%M:%S')
t_refer = time.mktime(t_refer_strp)


def get_time_time(t_delay: int or float = 0):
    return time.time() + t_delay


def determine_week(t_delay: int or float = 0):
    t_now = time.time() + t_delay
    week = int((t_now - t_refer) // 604800)
    return week


def determine_what_day(t_delay: int or float = 0):
    what_day = time.strftime('%A', time.localtime(time.time() + t_delay))
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


def determine_when_exam(grade):
    if grade != 17:
        return ''
    exam_dict = {
        "项目管理1": "2020-10-18 15:30",
        "最优化": "2020-11-05 08:00",
        "泛函分析": "2020-11-13 13:30",
        "经济学": "2020-11-17 15:30",
        "确定性信号处理": "2020-11-20 10:00",
        "金属结构材料": "2020-11-23 08:00",
        "概率论与数理统计": "2020-11-27 13:30",
        "电气工程": "2020-12-01 08:00",
        "线性静力学": "2020-12-07 08:00",
        "工程热力学": "2020-12-14 08:00",
        "基础流体力学和空气动力学": "2020-12-17 08:00"
    }
    exam_list = exam_dict.keys()
    time_today = time.mktime(time.strptime(determine_date(), '%Y-%m-%d'))
    exams_count_down = ''
    for exam in exam_list:
        if isinstance(exam, str):
            exam_time_str = exam_dict[exam]
            exam_time = time.mktime(time.strptime(exam_time_str, '%Y-%m-%d %H:%M'))
            count_down_days = int((exam_time - time_today) // 86400)
            if 0 <= count_down_days <= 30:
                count_down_str = '距离 ' + exam + ' 考试还有' + str(count_down_days) + '天;\n'
                if not count_down_str:
                    exams_count_down += count_down_str
                else:
                    exams_count_down = exams_count_down + count_down_str
    if exams_count_down.strip() != '':
        exams_count_down = "一个月内的考试：\n" + exams_count_down.strip()
    return exams_count_down


if __name__ == "__main__":
    # print(f't_refer:{t_refer}')
    # print(f"time:{get_time_time()}")
    # print(f'week:{determine_week()}')
    # print(f'what_day:{determine_what_day()}')
    # print(f'date:{determine_date(86400)}')
    # print(compute_week_num('2020-09-26'))

    # start_date = determine_date()
    # start_hms = '00:12:00'
    # start_time = start_date + ' ' + start_hms
    # t_start_strp = time.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    # t_start = time.mktime(t_start_strp)
    # time_for_sleep = t_start - time.time()
    # if time_for_sleep < 0:
    #     time_for_sleep = t_start - get_time_time(-86400)
    #     print('今日的自动推送已错过，自动生成明日的推送任务')
    #     if time_for_sleep < 0:
    #         raise Exception("main l24逻辑错误")
    #
    # print(time_for_sleep)

    print(determine_when_exam(17))
