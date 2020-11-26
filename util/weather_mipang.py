from bs4 import BeautifulSoup as bs
import re
import requests
from util.time_util import determine_date


def get_weather():
    url = 'https://weather.mipang.com/tianqi-8284'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    wb_data = requests.get(url, headers=headers)
    soup = bs(wb_data.text, 'lxml')
    temp = soup.find_all('div', class_='row row1')
    temp = str(list(temp)[0])
    pattern = re.compile(r'<[^>]+>', re.S)
    temp = pattern.sub('', temp)
    return temp


def get_weather_plus():
    url = 'https://weather.mipang.com/tianqi-8284'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
    wb_data = requests.get(url, headers=headers)
    soup = bs(wb_data.text, 'lxml')
    temp = soup.find_all('div', class_='row row1')
    temp = str(list(temp)[0])
    pattern = re.compile(r'<[^>]+>', re.S)
    temp = pattern.sub('', temp)
    pmtemp = soup.find_all('div', class_='br br2')
    pmtemp = str(list(pmtemp)[0])
    pmtemp = pattern.sub('', pmtemp)
    pmtemp = re.sub(r'pm2.5\n*', r'空气质量:', pmtemp, count=1)
    pmtemp = re.split(r'\n', pmtemp)
    for each in pmtemp:
        if len(each) != 0:
            if each[:4] != '空气质量':
                temp = temp + '\n' + each
    return temp


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
    # print(get_weather())
    print(get_weather_plus())
    # print(today_weather.weather)
