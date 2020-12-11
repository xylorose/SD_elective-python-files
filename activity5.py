
from microbit import *
from time import *


brightness= 0
brightnessControl= 0
positionControl= 0
position_X = 0
position_Y = 0
while True:

    brightnessControl = (display.read_light_level() // 10) * 10 
    brightness = display.read_light_level() - brightnessControl 
    positionControl = display.read_light_level() // 50
    position_Y = 4 - positionControl
    position_X = (display.read_light_level()-(positionControl*50))// 10


    for i in range(5):
        if(i > position_Y):
            for j in range(5):
                display.set_pixel(j,i,9)

        if(i < position_Y):
            for j in range(5):
                display.set_pixel(j,i,0)

        if i == position_Y:
            for j in range(5):
                if(j < position_X):
                    display.set_pixel(j,i,9)

                if(j > position_X):
                    display.set_pixel(j,i,0)




    if (position_Y < 0):
        display.set_pixel(4,0, 9)
    else:
        display.set_pixel(position_X, position_Y, brightness)