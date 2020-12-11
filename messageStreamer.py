from adafruit_clue import clue
from adafruit_clue import time

clue_data = clue.simple_text_display(title="Message Streamer", title_color=(255,0 ,0 ), title_scale=3)
message = "This Message moves from right to left"
message1 = "This Message moves from left to right "
while True:
    clue_data[2].text = message
    clue_data[2].color = clue.YELLOW
    clue_data[2].scale = 2
   
    clue_data[5].text = message1
    clue_data[5].color = clue.WHITE
    clue_data[5].scale = 2
    
    clue_data[8].text = "This message blinks "
    clue_data[8].color = clue.SKY
    clue_data[8].scale = 2
    clue_data.show()
    clue_data[8].color = clue.BLACK
    time.sleep (0.05)

    temp = message[:1]
    message = message[1:] + temp

    temp1 = message1[:-1]
    message1 = message1[-1:]+temp1

   