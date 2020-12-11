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


nd = 0
color = 0
defference = 0

while True:

   nd = cp.light // 32 
   defference = nd * 32 


   color = (255*(cp.light - defference))// 32 
   
   for f in range(10):

      if f < nd: 
         cp.pixels[f] = (255,255,255)
      if f > nd:
         cp.pixels[f] = (0,0,0)


   
   if nd > 9:
      cp.pixels[nd - 1] = (255,255,255)
   else: 
      cp.pixels[nd] = (color,color,color)




  
   
   
   