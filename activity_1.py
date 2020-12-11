"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Getting started with CPX and CircuitPython intro on:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library

Find example code for CPX on:
https://github.com/adafruit/Adafruit_CircuitPython_CircuitPlayground/tree/master/examples
"""
# import CPX library
from adafruit_circuitplayground import cp
from time import sleep

WHITE = (255, 255,255)
OFF = (0, 0, 0)
i = 9
while True:
   i = 0 if i > 9 else i
   i = 9 if i < 0 else i


   cp.pixels[i] = WHITE
   sleep(0.1)
   cp.pixels[i] = OFF

   i = i - 1 if not cp.switch else i + 1
# cp.pixels[0] = (255,0,0); cp.pixels[1] = (0, 255,0); 
# while True:
# cp.pixels[0] =(255,0,0)
# cp.pixels[9] = ( 0, 0,255)



   
   
   
   