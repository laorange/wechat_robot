import time
from threading import Thread

from wechat_func import log_in, send_review_word_two_language
# from util.basic_functions import read_file2list
from util.student import Student
from util.func_apscheduler import do_at_sometime
from util.week import determine_week, determine_what_day, determine_date

from data.private_space.mysql_func import get_user_list

# from application.review_word.get_word import get_word

start_date = '2020-09-16'
start_hms = '04:01:00'
start_time = start_date + ' ' + start_hms

# 测试时期 ---------------------------------------------------------------------#
# start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 5))
# 测试时期 ---------------------------------------------------------------------#

t_start_strp = time.strptime(start_time, '%Y-%m-%d %H:%M:%S')
t_start = time.mktime(t_start_strp)
t_next = t_start

user_list_path = 'data/private_space/user_list.csv'


def student_send(before_term_begin=False):
    # user_list = read_file2list(user_list_path)
    user_list = get_user_list()

    student_ls = []
    for user in user_list:
        try:
            # user_info_ls = user.split(',')
            user_info_ls = list(user)
            student_ls.append(
                Student(user_info_ls[0], user_info_ls[1], user_info_ls[2], user_info_ls[3], user_info_ls[4]))
        except Exception as e:
            print('for user in user_list:main37:', e)

    for student in student_ls:
        if student.name:
            if not before_term_begin:
                student.send_schedule_auto(if_tomorrow=False, date=determine_date(),
                                           week=determine_week(), what_day=determine_what_day())

            if True:
                student.send_weather(determine_week(), determine_date())
            time.sleep(0.1)


def start():
    global t_next
    # 自用的单词复习
    try:
        review_en_word_num = 20  # 复习英语单词的数量
        review_fr_word_num = 20  # 复习法语单词的数量
        send_review_word_two_language(review_en_word_num, review_fr_word_num)
        # do_at_sometime(lambda: send_review_word_two_language(review_en_word_num, review_fr_word_num),
        #                time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t_next + 57600)))
    except Exception as e:
        print('自用的单词复习模块出错')
        print(e)

    # 课表推送
    try:
        # what_day_num = time.strftime('%w', time.localtime())
        if determine_week() in [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
            # if what_day_num in ['1', '2', '3', '4', '5', '6']:  # 周一到周五，%w是从周日开始计数
            #     if_weekday = True
            # else:
            #     if_weekday = False
            #     print('-' * 10, '星期天', '-' * 10)

            try:
                print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "start checking students' info")
                if determine_week() == -1:
                    student_send(before_term_begin=True)  # , if_weekday=if_weekday
                else:
                    student_send(before_term_begin=False)  # , if_weekday=if_weekday
            except Exception as e:
                print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), 'student_send', e)
                raise Exception(e)

        else:
            print('本学期尚未开始或本学期的18周的课程已全部结束')
    except Exception as e:
        print('课表推送模块出错')
        print(e)


def multiple_start():
    global t_next
    start()
    for day in range(130):
        t_next += 86400
        t_next_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t_next))
        do_at_sometime(start, t_next_str)


def task_start():
    do_at_sometime(multiple_start, start_time)


if __name__ == "__main__":
    t1 = Thread(target=log_in)
    t2 = Thread(target=task_start)
    t1.start()
    t2.start()
