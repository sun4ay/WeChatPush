import os
import sys
from random import choice, choices
from enum import Enum


def exit_with_error():
    os.system("pause")
    sys.exit(1)


def print_error(message: str):
    print("[**ERROR**]: ", message)


def print_info(title: str, message: str):
    print("[**INFO**]", title + ": " + message)


class Color(Enum):
    Red = "#d50000"
    Purple = "#aa00ff"
    Indigo = "#304ffe"
    LightBlue = "#0091ea"
    Teal = "#00bfa5"
    Green = "#2ed573"
    Yellow = "#ffd600"
    Orange = "#ff6d00"
    Brown = "#3e2723"
    Pink = "#e64980"
    Grape = "#be4bdb"
    Violet = "#7950f2"
    Lime = "#82c91e"


def get_random_color() -> Color:
    # return "#%06x" % randint(0, 0xFFFFFF)
    return choice(list(Color))


# 返回随机颜色数组
def get_random_colors(length: int) -> list[Color]:
    return choices(list(Color), k=length)
