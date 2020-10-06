from random import randint

from wechat_func import send_msg_when
from util.weather import get_weather
from util.student_no_wechat import StudentNoWechat

preparatory_grades = [18, 19, 20]
engineer_grades = [17, 16, 15]


class Student(StudentNoWechat):
    def __init__(self, name, grade, a_or_b, p_ab_cd, f_ab_cd_e):
        super(Student, self).__init__(name, grade, a_or_b, p_ab_cd, f_ab_cd_e)
        # 为了避免达到发送阈值
        if randint(0, 1):
            self.send_hour = '5'
            self.send_min = str(randint(15, 59))
            self.send_sec_weather = str(randint(0, 29))
            self.send_sec_schedule = str(randint(30, 59))
        else:
            self.send_hour = '6'
            self.send_min = str(randint(0, 30))
            self.send_sec_weather = str(randint(0, 29))
            self.send_sec_schedule = str(randint(30, 59))

    def send_weather(self, week: int, date: str):
        try:
            # 发送天气
            print('-' * 9, '↓', self.name, '↓', '-' * 10)
            # 6:30通报全天有哪些课，以及第一节课的详细信息
            weather = get_weather()
            message_weather = ''
            if week == -1:
                message_weather = '今天是' + date + '，新学期即将开始\n' + weather
            else:
                if not self.replacement or self.grade in engineer_grades:
                    message_weather = '今天是' + date + '，这周是本学期的第' + str(week + 1) + '周\n' + weather
                else:
                    if self.grade in preparatory_grades:
                        message_weather = '今天是' + date + '，这周是本学期的第' + str(week + 1) + '周，今天补的是第' + str(
                            self.week + 1) + '周' + self.what_day + '的课\n' + weather
            print(message_weather)
            send_msg_when(self.name, message_weather,
                          date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec_weather)
        except Exception as e:
            print("发送天气时出错")
            print(e)

    def send_schedule_auto(self, date: str, week: int, what_day: str):
        message0 = self.get_schedule('今天', date, week, what_day)

        if_send = True
        # if self.what_day == 'Sunday':
        #     if_send = False
        #     print('周日不发送')
        # if date in ['2020-10-01', '2020-10-02', '2020-10-03']:
        #     if_send = False
        #     print('国庆假期')

        if self.grade in preparatory_grades and if_send:
            try:
                print(message0)
                send_msg_when(self.name, message0,
                              date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec_schedule)
                print('student info send ----> done\n')

            except Exception as e:
                print(f'student info send ----> fail\n{e}\n')

        if self.grade in engineer_grades and if_send:
            print(message0)
            send_msg_when(self.name, message0,
                          date + ' 0' + self.send_hour + ':' + self.send_min + ':' + self.send_sec_schedule)
            print('student info send ----> done\n')


if __name__ == "__main__":
    # student1 = Student('张三', 19, 'B', 'PC', 'PC')
    # # student1.get_schedule(14, 'Friday')
    # raise Exception('test')
    pass
