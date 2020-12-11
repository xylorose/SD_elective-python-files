from microbit import *
import time 

while True:
    display.show(Image("90000:09000:00900:00090:00009"))
    time.sleep (1)
    display.show(Image("09000:00900:00090:00009:00000"))
    time.sleep (1)
    display.show(Image("00900:00090:00009:00000:90000"))
    time.sleep (1)
    display.show(Image("00090:00009:00000:90000:09000"))
    time.sleep (1)
    display.show(Image("00009:90000:09000:00900:00090"))
    time.sleep (1)
    

#not passed, narealize ra ni nako pag 1:15 after lunch