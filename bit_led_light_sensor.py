"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.
Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
from time import sleep



while True:
    light = display.read_light_level()
    if light < 10:
        display.show(Image("00000:00000:00000:00000:{}0000".format(light)))
        sleep(1)
    else:
        display.show(Image("00000:00000:00000:00000:90000"))
    if light < 20:
        display.show(Image("00000:00000:00000:00000:0{}000".format(light)))
        sleep(1)
    else:
        display.show(Image("00000:00000:00000:00000:09000"))