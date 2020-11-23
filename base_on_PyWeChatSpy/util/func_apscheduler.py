import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.background import BlockingScheduler
from loguru import logger
from util.time_util import determine_standard_time


def my_job():
    print('it is my_job, {}'.format(time.ctime()))


def do_at_sometime(func, run_time, countdown=False, if_block=False, misfire_grace_time=1, args=None):
    """
    do_at_sometime
    :param if_block: 是否阻塞进程
    :param countdown: 倒计时模式
    :param misfire_grace_time: 容错时间间隔 默认：1s
    :param args: func的参数
    :param func: 将要执行的函数名
    :param run_time: 形如'2020-08-07 17:17:10' ‘%Y-%m-%d %H:%M’的时间
    :return: None
    """
    if countdown:
        run_time = determine_standard_time(run_time)
    run_time_strp = time.strptime(run_time, '%Y-%m-%d %H:%M:%S')
    t_delay = time.mktime(run_time_strp) - time.time()
    if t_delay > 3600:
        misfire_grace_time = int(t_delay // 3600)  # 允许1个小时产生1秒误差，不足1秒记作1秒

    if t_delay > -3:  # 三秒容错
        if if_block:
            scheduler = BlockingScheduler()
        else:
            scheduler = BackgroundScheduler()
        scheduler.add_job(func, 'date', run_date=run_time,
                          misfire_grace_time=misfire_grace_time, id=func.__name__, args=args)
        logger.info(f'future task {run_time}: "{func.__name__}"')
        scheduler.start()
    else:
        logger.error(f'run time miss: {run_time}: "{func.__name__}"')


def do_something_at_regular_intervals(func, interval, args=None, if_exe_right_now=True, if_block=False,
                                      misfire_grace_time=1):
    if if_block:
        scheduler = BlockingScheduler()
    else:
        scheduler = BackgroundScheduler()

    if interval > 3600:
        misfire_grace_time = int(interval // 3600)  # 允许1个小时产生1秒误差

    scheduler.add_job(func, 'interval', seconds=interval,
                      misfire_grace_time=misfire_grace_time, id=func.__name__, args=args)
    if if_exe_right_now:
        if isinstance(args, list):
            if args:
                func(args)
        else:
            func()
    logger.info(f'interval task ({interval}s): "{func.__name__}"')
    scheduler.start()


if __name__ == "__main__":
    # do_at_sometime(my_job, -2, countdown=True, if_block=True)
    # do_something_at_regular_intervals(my_job, interval=5, if_block=True)
    do_at_sometime(do_something_at_regular_intervals, run_time=10, countdown=True, args=[my_job, 3], if_block=True)
