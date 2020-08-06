import requests
from basic_functions import read_file2list

robot_info_ls = read_file2list("data/private_space/robot.txt")


# 以下是机器人小思部分！！！！↓
def get_answer(text):    # 获取思知机器人的回复信息
    headers = {
        'User-Agent': robot_info_ls[0],
        'Referer': 'https://robot.ownthink.com/',
    }

    def get_data(text_for_data):  # 请求思知机器人API所需要的一些信息
        pre_data = {
            "appid": robot_info_ls[1],
            "userid": robot_info_ls[2],
            "spoken": text_for_data,
        }
        return pre_data

    data = get_data(text)
    url = 'https://api.ownthink.com/bot'  # API接口
    response = requests.post(url=url, data=data, headers=headers)
    response.encoding = 'utf-8'
    result = response.json()
    answer = result['data']['info']['text']
    return answer


if __name__ == "__main__":
    print(get_answer("成都今天天气怎么样?"))
