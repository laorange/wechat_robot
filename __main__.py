import time
from threading import Thread

from util.basic_wxpy import bot_register
from util.basic_functions import read_file2list
from util.student import Student
from util.func_apscheduler import do_at_sometime

start_date = '2020-08-14'
start_time = '14:38:00'
start_time = start_date + ' ' + start_time

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
        student.get_schedule()
        student.send()


def start():
    global t_next
    student_send()
    t_next += 86400
    t_next_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t_next))
    do_at_sometime(start, t_next_str)


def task_start():
    do_at_sometime(start, start_time)


if __name__ == "__main__":
    t1 = Thread(target=task_start)
    t2 = Thread(target=bot_register)
    t1.start()
    t2.start()
