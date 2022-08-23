from WechatPush import *
from Api import API

if __name__ == '__main__':
    wechatPush = WeChatPush()
    api = API(wechatPush.get_config())
    wechatPush.put_send_data("love_message", api.get_love_message())
    wechatPush.put_send_data("dujitang", api.get_dujitang())
    wechatPush.put_send_data("city", api.get_city())
    wechatPush.put_send_data("weather", api.get_weather())
    wechatPush.run()
