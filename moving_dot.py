from microbit import *
import time 

while True:
    for y in range (5):
        for x in range(5):
            display.set_pixel(x,y,9)
            time.sleep (0.1)
            display.set_pixel(x,y,0)