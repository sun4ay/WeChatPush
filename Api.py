import requests
from utils import print_info
from datetime import date


class API:
    def __init__(self, config: dict):
        self.config = config
        self.alapi_token = config['alapi_token']

    @staticmethod
    def get_dujitang() -> str:
        content = requests.get("https://api.btstu.cn/yan/api.php").text
        print_info("毒鸡汤", content)
        return content

    def get_love_message(self) -> str:
        content = requests.get(
            f"http://api.tianapi.com/saylove/index?key={self.config['tianapi_token']}").json()["newslist"][0]['content']
        print_info("情话", content)
        return content

    def get_weather(self):
        data = requests.get(f"https://v2.alapi.cn/api/tianqi?token={self.alapi_token}"
                            f"&city={self.config['city']}&province={self.config['province']}").json().get('data', {})
        content = f"{data['weather']},当前温度: {data['temp']}, 最高温度: {data['max_temp']}, 最低温度: {data['min_temp']}"
        print_info("天气", content)
        return content

    def get_city(self):
        return self.config['city']

    def get_chasing_drama(self) -> str:
        videos = dict(self.config['videos'])
        weekday = date.today().weekday() + 1
        content = ""
        for k, v in videos.items():
            if weekday in v[0]:
                content += (k + ", 今日" + v[1] + "点更新")
        if content == "":
            content = "今日没有你追的剧哦"
        print_info("追剧提醒", content)
        return content

    def get_rainbow_pi(self):
        content = requests.get("http://api.tianapi.com/caihongpi/index"
                               f"?key={self.config['tianapi_token']}").json()["newslist"][0]['content']
        print_info("彩虹屁", content)
        return content
