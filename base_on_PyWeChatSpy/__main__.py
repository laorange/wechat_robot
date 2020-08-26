import time
from threading import Thread

from wechat_func import log_in, send_review_word
from util.basic_functions import read_file2list
from util.student import Student
from util.func_apscheduler import do_at_sometime
from util.week import determine_week, determine_what_day, determine_date

# from application.review_word.get_word import get_word

start_date = '2020-08-27'
start_hms = '06:00:00'
start_time = start_date + ' ' + start_hms

# 测试时期 ---------------------------------------------------------------------#
# start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 10))
# 测试时期 ---------------------------------------------------------------------#

t_start_strp = time.strptime(start_time, '%Y-%m-%d %H:%M:%S')
t_start = time.mktime(t_start_strp)
t_next = t_start

user_list_path = 'data/private_space/user_list.csv'


def student_send():
    user_list = read_file2list(user_list_path)

    student_ls = []
    for user in user_list:
        user_info_ls = user.split(',')
        student_ls.append(Student(user_info_ls[0], user_info_ls[1], user_info_ls[2], user_info_ls[3], user_info_ls[4]))

    for student in student_ls:
        student.get_schedule_and_send(determine_week(), determine_what_day(), determine_date())


def start():
    global t_next
    # 自用的单词复习
    try:
        send_review_word(20)
        do_at_sometime(lambda: send_review_word(20), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t_next+50400)))
    except Exception as e:
        print('自用的单词复习模块出错')
        print(e)

    # 课表推送
    try:
        what_day_num = time.strftime('%w', time.localtime())
        if determine_week() in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
            if what_day_num in ['1', '2', '3', '4', '5']:  # 周一到周五，%w是从周日开始计数
                try:
                    print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), "start checking students' info")
                    student_send()
                except Exception as e:
                    print(time.strftime('%Y-%m-%d %H:%M:', time.localtime()), 'student_send', e)
            else:
                print('周末不推送', '-' * 10)
        else:
            print('本学期尚未开始或本学期的18周的课程已全部结束')
    except Exception as e:
        print('课表推送模块出错')
        print(e)

    t_next += 86400
    t_next_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t_next))
    do_at_sometime(start, t_next_str)


def task_start():
    do_at_sometime(start, start_time)


# def review_word():


if __name__ == "__main__":
    t1 = Thread(target=log_in)
    t2 = Thread(target=task_start)
    t1.start()
    t2.start()
