from random import randint

from util.func_apscheduler import do_at_sometime
from util.wechat_func import send
from util.weather_mipang import Weather
from util.student_no_wechat import StudentNoWechat
from util.time_util import determine_date, determine_week, determine_what_day, ensure_time_or_plus_24h

import traceback
from loguru import logger

preparatory_grades = [18, 19, 20]
engineer_grades = [17, 16, 15]

today_weather = Weather()
today_weather.update_weather()


class Student(StudentNoWechat):
    def __init__(self, name, grade, a_or_b, p_ab_cd, f_ab_cd_e):
        super(Student, self).__init__(name, grade, a_or_b, p_ab_cd, f_ab_cd_e)
        # 为了避免达到发送阈值 使发送时间随机
        if grade in preparatory_grades:
            if randint(0, 1):
                self.send_hour = '17'
                self.send_min = str(randint(10, 59))
                self.send_sec_weather = str(randint(0, 29))
                self.send_sec_schedule = str(randint(30, 59))
            else:
                self.send_hour = '18'
                self.send_min = str(randint(0, 59))
                self.send_sec_weather = str(randint(0, 29))
                self.send_sec_schedule = str(randint(30, 59))

            self.situation_in_send_msg = '明天'
            self.time_delay_when_send = 86400

        elif grade in engineer_grades:
            if randint(0, 1):
                self.send_hour = '05'
                self.send_min = str(randint(30, 59))
                self.send_sec_weather = str(randint(0, 29))
                self.send_sec_schedule = str(randint(30, 59))
            else:
                self.send_hour = '06'
                self.send_min = str(randint(0, 30))  #
                self.send_sec_weather = str(randint(0, 29))
                self.send_sec_schedule = str(randint(30, 59))

            self.situation_in_send_msg = '今天'
            self.time_delay_when_send = 0

    def send_weather_func(self):
        date = determine_date(self.time_delay_when_send)
        week = determine_week(self.time_delay_when_send)
        try:
            global today_weather
            # 发送天气
            if today_weather.date == date and today_weather.situation == self.situation_in_send_msg:
                weather = today_weather.weather
            else:
                today_weather.update_weather(situation=self.situation_in_send_msg)
                weather = today_weather.weather
            message_weather = ''
            if week == -1:
                message_weather = f'{self.situation_in_send_msg}是' + date + '，新学期即将开始\n' + weather
            else:
                if not self.replacement or self.grade in engineer_grades:
                    message_weather = f'{self.situation_in_send_msg}是' + date + \
                                      '，本学期的第' + str(week + 1) + '周\n' + weather
                else:
                    if self.grade in preparatory_grades:
                        message_weather = f'{self.situation_in_send_msg}是' + date + '，本学期的第' + str(week + 1) + \
                                          f'周，{self.situation_in_send_msg}补的是第' + str(self.week + 1) + '周' + \
                                          self.what_day + '的课\n' + weather
            send(self.name, message_weather)

            logger.info(f'{self.name} weather ----> done\n')
        except Exception as e:
            logger.error("发送天气时出错" + str(e))
            traceback.print_exc()

    def send_weather(self):
        send_date = determine_date()
        send_time = send_date + ' ' + self.send_hour + ':' + self.send_min + ':' + self.send_sec_weather
        do_at_sometime(self.send_weather, ensure_time_or_plus_24h(send_time))

    def send_schedule_auto_func(self):
        date = determine_date(self.time_delay_when_send)
        week = determine_week(self.time_delay_when_send)
        what_day = determine_what_day(self.time_delay_when_send)

        message0 = self.get_schedule(self.situation_in_send_msg, date, week, what_day)

        if_send = True
        # if self.what_day == 'Sunday':
        #     if_send = False
        #     print('周日不发送')
        # if date in ['2020-10-01', '2020-10-02', '2020-10-03']:
        #     if_send = False
        #     print('国庆假期')

        if self.grade in preparatory_grades and if_send:
            try:
                send(self.name, message0)
                logger.info(f'预科课表 {self.name} send ----> done\n')

            except Exception as e:
                logger.warning(f'预科课表 {self.name} send ----> fail\n{e}\n')
                traceback.print_exc()

        if self.grade in engineer_grades and if_send:
            try:
                send(self.name, message0)
                logger.info(f'工程师课表{self.name} send ----> done\n')

            except Exception as e:
                logger.warning(f'工程师课表 {self.name} send ----> fail\n{e}\n')
                traceback.print_exc()

    def send_schedule_auto(self):
        send_date = determine_date()
        send_time = send_date + ' ' + self.send_hour + ':' + self.send_min + ':' + self.send_sec_schedule
        do_at_sometime(self.send_schedule_auto, ensure_time_or_plus_24h(send_time))


if __name__ == "__main__":
    # student1 = Student('张三', 19, 'B', 'PC', 'PC')
    # # student1.get_schedule(14, 'Friday')
    # raise Exception('test')
    pass
