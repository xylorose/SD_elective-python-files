from adafruit_clue import clue
from adafruit_clue import time
from random import randint
from time import sleep


clue_data = clue.simple_text_display(title="Reaction Game", title_color=(255,0 ,0 ), title_scale=2)

def makeNewDisplay():
    clue_data[10].text = ("Player A presses A")
    clue_data[10].color = clue.GREEN
    clue_data[12].text = ("Player B presses B")
    clue_data[12].color = clue.GREEN
    # clue_data.show()


while True:
    clue_data[1].text = ("Instruction:")
    clue_data[1].color = clue.GREEN
    clue_data[1].scale = 2
    
    clue_data[3].text = ("Player A presses A: ")
    clue_data[3].color = clue.WHITE
    clue_data[3].scale = 1
    clue_data[5].text = ("Player B presses B: ")
    clue_data[5].color = clue.WHITE
    clue_data[5].scale = 1
    clue_data[8].text = ("Pressed if the number is divisible by 2")
    clue_data[8].color = clue.SKY
    clue_data[8].scale = 1
    clue_data[10].text = ("Maximum Score of 5")
    clue_data[10].color = clue.YELLOW
    clue_data[10].scale = 1
    clue_data.show()
    
    for i in range (3, 0, -1):
        clue_data[12].text = "Starts in " + str(i)
        clue_data[12].color = clue.RED
        sleep(2)
        clue_data.show()
        
    while True:
        if str(i) == "1":
            makeNewDisplay()


    # while True:
    #     if clue.button_a:
    #         print("print A is pressed")
    #     else:
    #         print("false")
    