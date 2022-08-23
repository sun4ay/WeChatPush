from WechatPush import *
from Api import API
from utils import colors

if __name__ == '__main__':
    wechatPush = WeChatPush()
    api = API(wechatPush.get_config())
    wechatPush.put_send_data("love_message", api.get_love_message(), color=colors[0])
    wechatPush.put_send_data("dujitang", api.get_dujitang(), color=colors[2])
    wechatPush.put_send_data("city", api.get_city(), color=colors[4])
    wechatPush.put_send_data("weather", api.get_weather(), color=colors[8])
    wechatPush.put_send_data('video', api.get_chasing_drama(), color=colors[10])
    wechatPush.put_send_data("rainbow_pi", api.get_rainbow_pi(), color=colors[12])
    wechatPush.run()
