import os
import sys
from random import choice


def exit_with_error():
    os.system("pause")
    sys.exit(1)


def print_error(message: str):
    print("[**ERROR**]: ", message)


def print_info(title: str, message: str):
    print("[**INFO**]", title + ": " + message)


def get_random_color() -> str:
    # return "#%06x" % randint(0, 0xFFFFFF)
    # 颜色来源: 中国传统色
    # colors = ["#fff799", "#ffee6f", "#ecd452", "#b6a014",
    #           "#d5ebe1", "#b1d5c8", "#99bcac", "#80a492",
    #           "#8b7042", "#775039", "#5f4321", "#422517",
    #           "#f3a694", "#ee7959", "#ba5140", "#c12c1f"]
    colors = ["#80a492", "#beb1aa", "#9aa7b1", "#698e6a",
              "#f6bec8", "#d4e5ef", "#ffee6f", "#c3d94e",
              "#d6c560", "#2a6e3f", "#8a1874", "#f3a694",
              "#f091a0"]
    return choice(colors)
