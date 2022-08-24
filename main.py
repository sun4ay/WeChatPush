from WechatPush import *
from Api import API
from utils import Color

if __name__ == '__main__':
    wechatPush = WeChatPush()
    api = API(wechatPush.get_config())
    # 参数说明wechatPush.put_send_data(keys即模板的变量名集合, values即需要替换模板的内容,
    # color即为模板的颜色, 可不传参, 即只需指定put_send_data(keys=[], values=[])
    wechatPush.put_send_data(keys=["city", "weather", "max_temp", "min_temp", "current_temp", "current_window",
                                   "PM2_5", "air_quality", "sunrise", "sunset"],
                             values=api.get_weather(),
                             color=Color.LightBlue)

    wechatPush.put_send_data(keys=["meet_days"],
                             values=[api.get_meet_days()],
                             color=Color.Teal)

    wechatPush.put_send_data(keys=['birthdays'],
                             values=[api.get_birthdays_message()],
                             color=Color.LightGreen)

    wechatPush.put_send_data(keys=["note"],
                             values=[api.get_everyday_note()],
                             color=Color.Purple)

    wechatPush.run()
