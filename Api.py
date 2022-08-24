import requests
from zhdate import ZhDate

from utils import *
from datetime import date, datetime


class API:
    def __init__(self, config: dict):
        self.config = config

    # 毒鸡汤
    @staticmethod
    def get_dujitang() -> str:
        content = requests.get("https://api.btstu.cn/yan/api.php").text
        print_info("毒鸡汤", content)
        return content

    # 情话
    def get_love_message(self) -> str:
        content = requests.get("https://api.lovelive.tools/api/SweetNothings/Web/1").json()["returnObj"]['content']
        print_info("情话", content)
        return content

    # 天气
    def get_weather(self) -> list[str]:
        data = requests.get(f"https://v2.alapi.cn/api/tianqi?token={self.config['alapi_token']}"
                            f"&city={self.config['city']}&province={self.config['province']}").json().get('data', {})
        content = [self.config['city'], data['weather'], data['max_temp'], data['min_temp'],
                   data['temp'], data['wind'], data['air_pm25'], data['aqi']['air_level'],
                   data['sunrise'], data['sunset']]
        # content = f"{data['weather']}, 当前温度: {data['temp']}℃, 最高温度: {data['max_temp']}℃, 最低温度: {data['min_temp']}℃"
        print_info("天气", str(content))
        return content

    # 追剧模式
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

    # 彩虹屁
    def get_rainbow_pi(self) -> str:
        content = requests.get("http://api.tianapi.com/caihongpi/index"
                               f"?key={self.config['tianapi_token']}").json()["newslist"][0]['content']
        print_info("彩虹屁", content)
        return content

    # 相遇时间
    def get_meet_days(self):
        days = str((date.today() - datetime.strptime(self.config["meet_day"], "%Y-%m-%d").date()).days)
        print_info("认识天数", days)
        return days

    # 词霸每日一句
    @staticmethod
    def get_everyday_note():
        data = requests.get("http://open.iciba.com/dsapi/").json()
        # note: 汉语, content: 英语
        content = data['note'] + "\n" + data['content']
        print_info("词霸每日一句", content)
        return content

    @staticmethod
    def __get_birth_text(name: str, days: int):
        if days == 0:
            return f"今天是{name}的生日哦, 你备好礼物了吗?\n"
        if 0 < days <= 10:
            return f"还有{days}天就是{name}的生日了, 赶快准备礼物吧!\n"
        if days > 10:
            return f"距离{name}的生日还有{days}天\n"

    def get_birthdays_message(self):
        names = self.config['names']
        births = self.config['birthdays']
        if len(names) != len(births):
            print_error("请确定姓名个数和生日个数是否对应")
            exit_with_error()
        i = 0
        content = ''
        for birth in births:
            # 农历计算
            if birth.startswith("r"):
                dt = datetime.strptime(birth[1:], "%Y-%m-%d")
                next_birth_day = ZhDate(datetime.today().year, dt.month, dt.day)
                days = next_birth_day - ZhDate.from_datetime(datetime.today())
                if days < 0:
                    next_birth_day = ZhDate(datetime.today().year + 1, dt.month, dt.day)
                    days = next_birth_day - ZhDate.from_datetime(datetime.today())
            else:
                d = datetime.strptime(birth, "%Y-%m-%d").date()
                days = (date(date.today().year, d.month, d.day) - date.today()).days
                if days < 0:
                    days = (date(date.today().year + 1, d.month, d.day) - date.today()).days
            content += self.__get_birth_text(names[i], days)
            i += 1
        content = content[:-1]  # 去除最后一个换行符
        print_info("生日", content)
        return content
