# """
# To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

# To learn more about the CLUE and CircuitPython, check this link out:
# https://learn.adafruit.com/adafruit-clue/circuitpython

# Find example code for CPX on:
# https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
# """

###########################################################################
# # Original sample
# from adafruit_clue import clue

# clue_data = clue.simple_text_display(title="Hello World", title_scale=3)

# while True:
#     clue_data.show()

###########################################################################
# # Second sample
# """Monitor customisable temperature and humidity ranges, with an optional audible alarm tone."""
# from adafruit_clue import clue

# # Set desired temperature range in degrees Celsius.
# min_temperature = 24
# max_temperature = 30

# # Set desired humidity range in percent.
# min_humidity = 20
# max_humidity = 65

# # Set to true to enable audible alarm tone.
# alarm_enable = False

# clue_display = clue.simple_text_display(text_scale=3, colors=(clue.WHITE,))

# clue_display[0].text = "Temperature &"
# clue_display[1].text = "Humidity"

# while True:
#     alarm = False

#     temperature = clue.temperature
#     humidity = clue.humidity

#     clue_display[3].text = "Temp: {:.1f} C".format(temperature)
#     clue_display[5].text = "Humi: {:.1f} %".format(humidity)

#     if temperature < min_temperature:
#         clue_display[3].color = clue.BLUE
#         alarm = True
#     elif temperature > max_temperature:
#         clue_display[3].color = clue.RED
#         alarm = True
#     else:
#         clue_display[3].color = clue.WHITE

#     if humidity < min_humidity:
#         clue_display[5].color = clue.BLUE
#         alarm = True
#     elif humidity > max_humidity:
#         clue_display[5].color = clue.RED
#         alarm = True
#     else:
#         clue_display[5].color = clue.WHITE
#     clue_display.show()

#     if alarm and alarm_enable:
#         clue.start_tone(2000)
#     else:
#         clue.stop_tone()

###########################################################################
# # Third sample
#SPDX-FileCopyrightText: 2019 Kattni Rembor, written for Adafruit Industries

# SPDX-License-Identifier: Unlicense

# from adafruit_clue import clue

# clue.sea_level_pressure = 1020

# clue_data = clue.simple_text_display(title="CLUE Sensor Data!", title_scale=2)

# while True:
#     clue_data[0].text = "Acceleration: {:.2f} {:.2f} {:.2f} m/s^2".format(
#         *clue.acceleration
#     )
#     clue_data[1].text = "Gyro: {:.2f} {:.2f} {:.2f} dps".format(*clue.gyro)
#     clue_data[2].text = "Magnetic: {:.3f} {:.3f} {:.3f} uTesla".format(*clue.magnetic)
#     clue_data[3].text = "Pressure: {:.3f} hPa".format(clue.pressure)
#     clue_data[4].text = "Altitude: {:.1f} m".format(clue.altitude)
#     clue_data[5].text = "Temperature: {:.1f} C".format(clue.temperature)
#     clue_data[6].text = "Humidity: {:.1f} %".format(clue.humidity)
#     clue_data[7].text = "Proximity: {}".format(clue.proximity)
#     clue_data[8].text = "Gesture: {}".format(clue.gesture)
#     clue_data[9].text = "Color: R: {} G: {} B: {} C: {}".format(*clue.color)
#     clue_data[10].text = "Button A: {}".format(clue.button_a)
#     clue_data[11].text = "Button B: {}".format(clue.button_b)
#     clue_data[12].text = "Touch 0: {}".format(clue.touch_0)
#     clue_data[13].text = "Touch 1: {}".format(clue.touch_1)
#     clue_data[14].text = "Touch 2: {}".format(clue.touch_2)
#     clue_data[15].text = "Sample"
#     clue_data.show()

###########################################################################
# # Fourth Sample with error
# SPDX-FileCopyrightText: 2019 Kattni Rembor, written for Adafruit Industries

# SPDX-License-Identifier: Unlicense
# """Display a series of bitmaps using the buttons to advance through the list. To use: place
# supported bitmap files on your CIRCUITPY drive, then press the buttons on your CLUE to advance
# through them.
# Requires the Adafruit CircuitPython Slideshow library!"""

# from adafruit_slideshow import SlideShow, PlayBackDirection
# from adafruit_clue import clue

# # error starts in this line of code
# slideshow = SlideShow(clue.display, auto_advance=False)

# while True:
#     if clue.button_b:
#         slideshow.direction = PlayBackDirection.FORWARD
#         slideshow.advance()
#         print('button b pressed')
#     if clue.button_a:
#         slideshow.direction = PlayBackDirection.BACKWARD
#         slideshow.advance()
#         print('button a pressed')

###########################################################################
# # Fifth sample
#
# SPDX-FileCopyrightText: 2019 Kattni Rembor, written for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
# """CLUE Spirit Level Demo"""

# import board
# import displayio
# from adafruit_display_shapes.circle import Circle
# from adafruit_clue import clue

# display = board.DISPLAY
# clue_group = displayio.Group(max_size=4)

# outer_circle = Circle(120, 120, 119, outline=clue.WHITE)
# middle_circle = Circle(120, 120, 75, outline=clue.YELLOW)
# inner_circle = Circle(120, 120, 35, outline=clue.GREEN)
# clue_group.append(outer_circle)
# clue_group.append(middle_circle)
# clue_group.append(inner_circle)

# x, y, _ = clue.acceleration
# bubble_group = displayio.Group(max_size=1)
# level_bubble = Circle(int(x + 120), int(y + 120), 20, fill=clue.RED, outline=clue.RED)
# bubble_group.append(level_bubble)

# clue_group.append(bubble_group)
# display.show(clue_group)

# while True:
#     x, y, _ = clue.acceleration
#     bubble_group.x = int(x * -10)
#     bubble_group.y = int(y * -10)

###########################################################################
# Sixth sample

# from adafruit_clue import clue
# from time import *

# # clue_display = clue.simple_text_display(text_scale=3, colors=(clue.WHITE,))
# clue_display = clue.simple_text_display(text_scale=2, colors=(clue.WHITE,))

# clue_display[0].text = "Temperature &"
# clue_display[1].text = "Humidity"

# while True:
#     t = localtime()
#     current_time = strftime("%H:%M:%S", t)
#     clue_display[3].text = "Temperature: {}".format(clue.temperature)
#     clue_display[4].text = "Humidity: {}".format(clue.humidity)
#     clue_display[5].text = "Time: {}".format(current_time)
#     clue_display.show()

###########################################################################