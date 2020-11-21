from datetime import date
from dateutil.relativedelta import relativedelta
import time

weekday = ''
tbs_what_day = ['今天', '明天', '后天', '大后天', '大大后天', '早上', '中午', '晚上', '傍晚',
                '今日', '第一天', '明日', '第二天', '两天后', '第三天', '两天后',
                '第三天', '三天后', '第四天', '四天后', '第五天',
                '周一', '周二', '周三', '周四', '周五', '周六', '周日', '周天',
                '本周一', '本周二', '本周三', '本周四', '本周五', '本周六', '本周日', '本周天',
                '星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日', '星期天',
                '下周一', '下周二', '下周三', '下周四', '下周五', '下周六', '下周日', '下周天',
                '下星期一', '下星期二', '下星期三', '下星期四', '下星期五', '下星期六', '下星期日', '下星期天',
                '周1', '周2', '周3', '周4', '周5', '周6', '周7']


# TODO: 解析中文的周几
def parse_weekday(x: str) -> date:
    global weekday
    TODAY = date.today()
    if x in ['今天', '今日', '第一天']:
        return TODAY
    if x in ['明天', '明日', '第二天', '一天后']:
        return TODAY + relativedelta(days=+1)
    if x in ['后天', '后日', '第三天', '二天后', '两天后']:
        return TODAY + relativedelta(days=+2)
    if x in ['大后天', '大后日', '第四天', '三天后']:
        return TODAY + relativedelta(days=+3)
    if x in ['大大后天', '大大后日', '第五天', '四天后']:
        return TODAY + relativedelta(days=+4)
    if x in ['大大大后天', '大大大后日', '第六天', '五天后']:
        return TODAY + relativedelta(days=+5)
    TIME = {
        1: ['1', '一'],
        2: ['2', '二'],
        3: ['3', '三'],
        4: ['4', '四'],
        5: ['5', '五'],
        6: ['6', '六'],
        7: ['7', '七', '日', '天']
    }
    weeks = None
    if x[0] == '上' or x[0] == '前':
        weeks = -1
    if x[0] == '下' or x[0] == '后' or x[0] == '明':
        weeks = 0

    count = 0
    for k, v in TIME.items():
        for i in v:
            if i in x:
                count += 1
                weekday = k

    if count != 1:
        return TODAY
    elif weeks == 0 or weeks == -1:
        if weeks == 0 and TODAY.isoweekday() <= weekday:
            return TODAY + relativedelta(weekday=weekday - 1, weeks=1)
        return TODAY + relativedelta(weekday=weekday - 1, weeks=weeks)
    else:
        if TODAY.isoweekday() >= weekday:
            return TODAY + relativedelta(days=+1, weekday=weekday - 1, weeks=-1)
        else:
            return TODAY + relativedelta(days=+1, weekday=weekday - 1)


def parse_wd_delay(wd: str) -> float:
    date_after_parse = parse_weekday(wd)
    date_str = str(date_after_parse) + ' 00:00:05'
    date_strp = time.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    t_delay = time.mktime(date_strp) - time.time()
    return t_delay


def parse_wd_ref_delay(wd: str) -> float:
    delay_today = parse_wd_delay('今天')
    delay_target = parse_wd_delay(wd)
    ref_delay = delay_target - delay_today
    return ref_delay


if __name__ == '__main__':
    print('<p>')
    for x in tbs_what_day:
        print(x, parse_weekday(x=x), parse_wd_ref_delay(x))
    #     print("@"+x+'<br>')
    # print('<p>')
