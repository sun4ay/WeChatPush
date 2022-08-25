from WechatPush import *
from Api import API
from utils import Color

if __name__ == '__main__':
    wechatPush = WeChatPush()
    api = API(wechatPush.get_config())
    # 参数说明wechatPush.put_send_data(keys即模板的变量名集合, values即需要替换模板的内容,
    # color即为模板的颜色, 可不传参, 即只需指定put_send_data(keys=[], values=[])

    # wechatPush.put_send_data(keys=["city", "weather", "max_temp", "min_temp", "current_temp", "current_window",
    #                                "PM2_5", "air_quality", "sunrise", "sunset"],
    #                          values=api.get_weather_all(),
    #                          colors=[Color.LightBlue])
    # 注意: 这是使用模板一的配置
    wechatPush.put_send_data(keys=["date"], values=[api.get_date()], colors=[Color.Red])

    wechatPush.put_send_data(keys=["city", "weather"],
                             values=api.get_weather_simple(),
                             colors=[Color.Indigo, Color.Orange])

    wechatPush.put_send_data(keys=["love_message", "rainbow_pi", "dujitang"],
                             values=[api.get_love_message(), api.get_rainbow_pi(), api.get_dujitang()],
                             colors=[Color.Yellow, Color.Green, Color.Pink])

    wechatPush.put_send_data(keys=["meet_days"],
                             values=[api.get_meet_days()],
                             colors=[Color.Teal])

    wechatPush.put_send_data(keys=['birthdays', "video"],
                             values=[api.get_birthdays_message(), api.get_chasing_drama()],
                             colors=[Color.Grape, Color.Pink])

    wechatPush.put_send_data(keys=["note"],
                             values=[api.get_everyday_note()],
                             colors=[Color.Purple])

    wechatPush.run()
