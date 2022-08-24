import os
import sys
from random import choice
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
    LightGreen = "#64dd17"
    Yellow = "#ffd600"
    Orange = "#ff6d00"
    Brown = "#3e2723"


def get_random_color() -> Color:
    # return "#%06x" % randint(0, 0xFFFFFF)
    return choice(list(Color))
