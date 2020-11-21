import time
from threading import Thread

from wechat_func import log_in, send_review_word_two_language, personalisation
# from util.basic_functions import read_file2list
from util.student import Student
from util.func_apscheduler import do_at_sometime
from util.week import *

from util.mysql_func import get_user_list_all_data

# from application.review_word.get_word import get_word

import traceback
from loguru import logger

logger.add('C:\\wamp64\\www\\log\\runtime{time}.log', rotation='00:00',
           retention='10 days', enqueue=True, encoding='UTF-8')  # 生成日志的路径

start_date = determine_date()
start_hms = '05:10:00'
start_time = start_date + ' ' + start_hms
t_start_strp = time.strptime(start_time, '%Y-%m-%d %H:%M:%S')
t_start = time.mktime(t_start_strp)
time_for_sleep = t_start - time.time()
if time_for_sleep < 0:
    time_for_sleep = t_start - get_time_time(-86400)
    logger.info('今日的自动推送已错过，自动生成明日的推送任务')
    if time_for_sleep < 0:
        raise Exception("main l24逻辑错误")
logger.info(f"time_for_sleep:{time_for_sleep}")


def student_send(before_term_begin=False):
    user_list = get_user_list_all_data()

    student_ls = []
    for user in user_list:
        try:
            user_info_ls = list(user)
            student_ls.append(
                Student(user_info_ls[0], user_info_ls[2], user_info_ls[3], user_info_ls[4], user_info_ls[5]))
        except Exception as e:
            logger.info(str(e))
            traceback.print_exc()

    for student in student_ls:
        if student.name:
            if not before_term_begin:
                student.send_schedule_auto(date=determine_date(),
                                           week=determine_week(),
                                           what_day=determine_what_day())

            if True:
                student.send_weather(determine_week(), determine_date())
            time.sleep(0.1)


def start():
    # ①对特定要求的定制发送任务
    # personalisation()

    # ②自用的单词复习
    # try:
    #     review_en_word_num = 20  # 复习英语单词的数量
    #     review_fr_word_num = 20  # 复习法语单词的数量
    #     send_review_word_two_language(review_en_word_num, review_fr_word_num)
    # except Exception as e:
    #     logger.error('自用的单词复习模块出错'+str(e))
    #     traceback.print_exc()

    # ⭐③课表推送
    try:
        if determine_week() in [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:  # 本学期只有15周
            try:
                logger.info("start checking students' info")
                if determine_week() == -1:
                    student_send(before_term_begin=True)  # , if_weekday=if_weekday
                else:
                    student_send(before_term_begin=False)  # , if_weekday=if_weekday
            except Exception as e:
                logger.error(e)
                traceback.print_exc()
                raise Exception(e)
        else:
            logger.warning('本学期尚未开始或本学期的18周的课程已全部结束')
    except Exception as e:
        logger.error('课表推送模块出错' + str(e))
        traceback.print_exc()
    next_time = determine_standard_time(86400)
    do_at_sometime(start, next_time)


def auto_send():
    time.sleep(time_for_sleep)
    start()


if __name__ == "__main__":
    t1 = Thread(target=log_in)
    t2 = Thread(target=auto_send())
    t1.start()
    t2.start()
