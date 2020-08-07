import time
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.date import DateTrigger


def my_job():
    print('my_job, {}'.format(time.ctime()))


def do_at_sometime(func, run_date, task_name='my_job_id'):
    scheduler = BackgroundScheduler()
    intervalTrigger = DateTrigger(run_date=run_date)
    scheduler.add_job(func, intervalTrigger, id=task_name)
    scheduler.start()


if __name__ == "__main__":
    # scheduler = BackgroundScheduler()
    # intervalTrigger = DateTrigger(run_date='2020-08-07 17:13:00')
    # scheduler.add_job(my_job, intervalTrigger, id='my_job_id')
    # scheduler.start()
    # while True:
    #     time.sleep(1)
    do_at_sometime(my_job, '2020-08-07 17:17:10')
    while True:
        time.sleep(1)

# import time
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.date import DateTrigger
#
#
# def my_job():
#     print('my_job, {}'.format(time.ctime()))
#
#
# def do_at_sometime(func, send_time, task_name='my_job_id', **trigger_args):
#     """send_time = 2020-08-07 12:02:00"""
#     """format = '%Y-%m-%d %H:%M:%s'"""
#     scheduler = BackgroundScheduler()
#     intervalTrigger = DateTrigger(run_date=send_time)
#     scheduler.add_job(func, intervalTrigger, id=task_name, **trigger_args)
#     scheduler.start()


# if __name__ == "__main__":
#     scheduler = BlockingScheduler()
#     intervalTrigger = DateTrigger(run_date='2020-08-07 12:02:00')
#     scheduler.add_job(my_job, intervalTrigger, id='my_job_id')
#     scheduler.start()

# import time
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.interval import IntervalTrigger
#
#
# def my_job():
#     print('my_job, {}'.format(time.ctime()))
#
#
# if __name__ == "__main__":
#     scheduler = BackgroundScheduler()
#
#     # 间隔设置为1秒，还可以使用minutes、hours、days、weeks等
#     intervalTrigger = IntervalTrigger(seconds=1)
#
#     # 给作业设个id，方便作业的后续操作，暂停、取消等
#     scheduler.add_job(my_job, intervalTrigger, id='my_job_id')
#     scheduler.start()
#     print('=== end. ===')

'''
class Subject:
    def __init__(self, class_name, classroom, teacher):
        self.class_name = class_name
        self.classroom = classroom
        self.teacher = teacher


class Day:
    def __init__(self, c1, c2, c3, c4, c5):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5



第一周
高等数学/林洁/201,经典物理/秦哲/201,高等数学/林洁/201,经典物理/秦哲/201,高等数学/林洁/201\n
高等数学/林洁/201,经典物理/秦哲/201,高等数学/林洁/201,经典物理/秦哲/201,高等数学/林洁/201\n
高等数学/林洁/201,经典物理/秦哲/201,高等数学/林洁/201,经典物理/秦哲/201,高等数学/林洁/201\n
高等数学/林洁/201,经典物理/秦哲/201,高等数学/林洁/201,经典物理/秦哲/201,高等数学/林洁/201\n
,,毛概/李老师/220,,\n

第二周
...

'''
