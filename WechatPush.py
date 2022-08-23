from utils import *

import requests


class WeChatPush:
    def __init__(self):
        self.config = None  # 配置文件
        self.send_message_url = None  # 推送消息的链接
        self.data = None  # 上传的数据
        self.__load_config()  # 加载配置文件
        self.__get_access_token()  # 获取令牌
        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }  # 请求头
        self.__send_data = {}

    # 加载配置
    def __load_config(self):
        try:
            with open("config.cfg", encoding="utf-8", mode='r') as f:
                self.config = dict(eval(f.read()))
            self.data = {"template_id": self.config['template_id'],
                         'url': "http://weixin.qq.com/download",
                         'topcolor': "#FF0000"}
        except FileNotFoundError:
            print_error("推送消息失败，请检查config.cfg文件是否与程序位于同一路径")
            exit_with_error()
        except SyntaxError:
            print_error("推送消息失败，请检查config.cfg配置文件格式是否正确")
            exit_with_error()

    # 获取配置信息
    def get_config(self):
        return self.config

    # 获取口令
    def __get_access_token(self):
        post_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}" \
            .format(self.config["app_id"], self.config["app_secret"])
        try:
            self.send_message_url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=" + \
                                    requests.get(post_url).json()['access_token']
        except KeyError:
            print("获取access_token失败，请检查app_id和app_secret是否正确")
            exit_with_error()

    # 发起推送
    def __send_message(self, user_id: str, send_data: dict):
        self.data["touser"] = user_id
        self.data["data"] = send_data
        response = requests.post(self.send_message_url, headers=self.headers, json=self.data).json()
        # 返回码说明: https://mp.weixin.qq.com/debug/cgi-bin/readtmpl?t=tmplmsg/faq_tmpl
        match response["errcode"]:
            case 40037:
                print_error("推送消息失败，请检查模板id是否正确")
            case 40036:
                print_error("推送消息失败，请检查模板id是否为空")
            case 40003:
                print_error("推送消息失败，请检查微信号是否正确")
            case 0:
                print("[**Success**]: 推送消息成功!")
            case _:
                print_error(response)

    # 放入数据
    def put_send_data(self, key: str, value: str, color: str = None):
        if color is None:
            color = get_random_color()
        self.__send_data[key] = {
            "value": value,
            "color": color
        }

    # 运行
    def run(self):
        if not self.__send_data:
            print_error("请先使用put_send_data(key, value)放入数据!!")
            exit_with_error()
        for user_id in self.config['users']:
            self.__send_message(user_id, self.__send_data)
