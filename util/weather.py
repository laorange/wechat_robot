from bs4 import BeautifulSoup as bs
import re
import requests
from util.time_util import determine_date


def get_weather_from_internet(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    wb_data = requests.get(url, headers=headers)
    soup = bs(wb_data.text, 'lxml')
    temp = soup.find_all('div', class_='real-mess')
    temp = str(list(temp)[0])
    pattern = re.compile(r'<[^>]+>', re.S)
    temp = pattern.sub('', temp)
    temp = temp.split()
    # print(temp)
    aqi = '污染指数:' + temp[4] + '(' + temp[3] + ')'
    weather = ''
    for i in range(5, 10):
        weather = weather + temp[i] + '，'
        if temp[i + 1][0] == '昨':
            break
    weather = weather + aqi
    return weather


def get_weather():
    url = 'http://tianqi.2345.com/dongli1d/60140.htm'
    url_bk = 'http://tianqi.2345.com/tianjin1d/54527.htm'
    weather = get_weather_from_internet(url)
    if weather[0] == '昨':
        weather = '天津-' + get_weather_from_internet(url_bk)
    else:
        weather = '东丽区-' + weather
    return weather


class Weather:
    def __init__(self):
        self.date = ''
        self.weather = ''

    def update_weather(self):
        self.weather = get_weather()
        self.date = determine_date()


if __name__ == "__main__":
    today_weather = Weather()
    today_weather.update_weather()
    print(get_weather())
    print(today_weather.weather)
