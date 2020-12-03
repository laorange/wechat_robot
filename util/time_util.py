import time
import traceback
from loguru import logger
from util.parser_what_day import parse_weekday

t_refer_1_week = '2020-08-31'  # 本学期第一周周一的日期
t_refer_1_week = t_refer_1_week + ' 00:00:00'
t_refer_strp = time.strptime(t_refer_1_week, '%Y-%m-%d %H:%M:%S')
t_refer = time.mktime(t_refer_strp)


def ensure_time_or_plus_24h(time_str: str):
    date_strp = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    t_delay = int(time.mktime(date_strp) - time.time())
    while t_delay < 0:
        time_str = determine_standard_time(t_delay + 86400)
        date_strp = time.strptime(time_str, '%Y-%m-%d %H:%M:%S')
        t_delay = int(time.mktime(date_strp) - time.time())
    return time_str


def parse_wd_delay(wd: str, if_date=False) -> float:
    if not if_date:
        date_after_parse = parse_weekday(wd)
    else:
        date_after_parse = wd
    date_str = str(date_after_parse) + ' 00:00:05'
    date_strp = time.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    t_delay = time.mktime(date_strp) - time.time()
    return t_delay


def parse_wd_ref_delay(wd: str, if_date=False) -> float:
    try:
        delay_today = parse_wd_delay('今天')
        delay_target = parse_wd_delay(wd, if_date)
        ref_delay = delay_target - delay_today
        return ref_delay
    except ValueError as e:
        logger.error(e)
        raise ValueError


def get_time_time(t_delay: int or float = 0):
    return time.time() + t_delay


def determine_week(t_delay: int or float = 0):
    t_now = time.time() + t_delay
    week = int((t_now - t_refer) // 604800)
    return week


def determine_what_day(t_delay: int or float = 0):
    what_day = time.strftime('%A', time.localtime(time.time() + t_delay))
    return what_day


def determine_standard_time(t_delay: int or float = 0):
    standard_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + t_delay))
    return standard_time


def determine_date(t_delay: int or float = 0):
    date = time.strftime('%Y-%m-%d', time.localtime(time.time() + t_delay))
    return date


def determine_year(t_delay: int or float = 0):
    year = determine_date(t_delay)[:4]
    return year


def compute_week_num(target_day: str):
    target_day_final_str = target_day + ' 00:00:00'
    t_target_strp = time.strptime(target_day_final_str, '%Y-%m-%d %H:%M:%S')
    t_target = time.mktime(t_target_strp)
    week = int((t_target - t_refer) // 604800)
    return week


def determine_when_exam(grade, t_delay=0, situation='今天'):
    exam_dict = {}
    if grade not in [16, 17, 18, 19, 20]:
        return ''
    exam_dict[20] = {
        "法语口试": "2020-12-14 08:00",
        "基础物理(上)": "2020-12-15 08:00",
        "基础法语1": "2020-12-16 08:00",
        "中国近代史纲要及实践": "2020-12-17 08:00",
        "高等数学1": "2020-12-18 08:00",
        "大学英语1": "2020-12-19 08:00"
    }
    exam_dict[19] = {
        "高等数学3": "2020-12-13 08:00",
        "大学英语3": "2020-12-14 08:00",
        "中级法语1": "2020-12-15 08:00",
        "普通物理(上)": "2020-12-17 08:00",
        "化学1": "2020-12-18 08:00",
        "法语口试": "2020-12-18 08:00",
        "毛泽东思想和中国特色社会主义理论体系概论1": "2020-12-20 08:00"
    }
    exam_dict[18] = {
        "计算机编程": "2020-12-02 08:00",
        "工程制图": "2020-12-13 08:00",
        "中级法语3": "2020-12-14 08:00",
        "综合英语1": "2020-12-15 08:00",
        "高等数学5": "2020-12-16 08:00",
        "经典物理(上)": "2020-12-17 08:00",
        "法语口试": "2020-12-17 08:00",
        "英语口试": "2020-12-20 08:00"
    }
    exam_dict[17] = {
        "项目管理1": "2020-10-18 15:30",
        "最优化": "2020-11-05 08:00",
        "泛函分析": "2020-11-13 13:30",
        "经济学": "2020-11-17 15:30",
        "确定性信号处理": "2020-11-20 10:00",
        "金属结构材料": "2020-11-23 08:00",
        "概率论与数理统计": "2020-11-27 13:30",
        "电气工程": "2020-12-01 08:00",
        "线性静力学": "2020-12-07 08:00",
        "工程英语1": "2020-12-11 08:00",
        "工程热力学": "2020-12-14 08:00",
        "基础流体力学和空气动力学": "2020-12-17 08:00"
    }
    exam_dict[16] = {
        "航空法导论": "2020-10-30 08:00",
        "数字电路": "2020-11-03 08:00",
        "高级流体力学": "2020-11-16 08:00",
        "复合及特殊材料": "2020-11-24 10:00",
        "偏微分方程数值分析": "2020-12-01 10:00",
        "动态系统建模与分析": "2020-12-04 10:00",
        "对流换热": "2020-12-07 13:30",
        "离散结构动力学": "2020-12-14 13:30",
        "控制设计与伺服回路系统": "2020-12-18 10:00",
        "初级民航英语": "2020-12-19 08:00",
    }
    exam_list = exam_dict[grade].keys()
    time_refer = time.mktime(time.strptime(determine_date(t_delay), '%Y-%m-%d'))
    exams_count_down = ''
    for exam in exam_list:
        if isinstance(exam, str):
            exam_time_str = exam_dict[grade][exam]
            exam_time = time.mktime(time.strptime(exam_time_str, '%Y-%m-%d %H:%M'))
            count_down_days = int((exam_time - time_refer) // 86400)
            if 1 <= count_down_days <= 30:
                count_down_str = '距离 ' + exam + ' 考试还有' + str(count_down_days) + '天;\n'
                if not count_down_str:
                    exams_count_down += count_down_str
                else:
                    exams_count_down = exams_count_down + count_down_str
            elif count_down_days == 0:
                exams_count_down += f'{situation}就要考' + exam + '了，加油[加油]' + ';\n'
    if exams_count_down.strip() != '':
        exams_count_down = f"（{situation}）近期考试倒计时：\n" + exams_count_down.strip()
    if grade in [18, 19, 20]:
        exams_count_down = exams_count_down + "\n图片链接: laorange.top/kb/exam"
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
    print(ensure_time_or_plus_24h('2020-11-29 16:40:00'))
    print(determine_when_exam(20))
