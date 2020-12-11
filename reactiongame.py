from adafruit_clue import clue
from time import time,sleep
from random import randint
clue_display = clue.simple_text_display(title="Reaction Game", title_color=(255,255 ,0 ), title_scale=2)

while True:
    clue_display[2].text = "Instructions:"
    clue_display[2].color = clue.GREEN
    clue_display[2].scale = 2
    
    clue_display[4].text = "Player A presses A"
    clue_display[4].color = clue.WHITE
    clue_display[4].scale = 2
    
    clue_display[6].text = "Player B presses B"
    clue_display[6].color = clue.WHITE
    clue_display[6].scale = 2
    
    clue_display[8].text = "Press if the number"
    clue_display[8].color = clue.SKY
    clue_display[8].scale = 2

    clue_display[10].text = "is divisible by 2"
    clue_display[10].color = clue.SKY
    clue_display[10].scale = 2
    
    clue_display[12].text = "Maximum score of 5"
    clue_display[12].color = clue.YELLOW
    clue_display[12].scale = 2

    for i in range(3, 0, -1): 
        clue_display[14].text = "STARTS IN " + str(i)
        clue_display[14].color = clue.RED
        clue_display[14].scale = 2
        sleep(2) 
       
        
        player_A = 0 
        player_B = 0 
        if i == 1:
            while True:
                random = randint(1, 100) 
                clue_display[2].text = "" 
                clue_display[4].text = "" 
                clue_display[6].text = "" 
                clue_display[8].text = "" 
                clue_display[10].text = ""
                clue_display[12].text = "Player A score: " + str(player_A)
                clue_display[12].color = clue.GREEN
                clue_display[14].text = "Player B score: " + str(player_B)
                clue_display[14].color = clue.SKY
                clue_display[4].text = "         " + str(random)

                time_1 = time()
                time_2 = time()
                counter = 1
                while counter > 0:
                    if time_2 - time_1 >= 1: 
                        counter = 0 
                    else: 
                        time_2 = time() 

                    if clue.button_a:
                        if random % 2 == 0:
                            player_A +=1
                        else: 
                            player_A -=1
                        break
                    if clue.button_b:
                        if random % 2 == 0:
                            player_B +=1 
                        else:
                            player_B -=1
                        break    

                if player_A == 5:
                    clue_display[12].text = "Player A score: " + str(player_A)
                    clue_display[2].text = "PLAYER A WINS!" 
                    clue_display[2].color = clue.RED 
                    break 
                    
                if player_B == 5:
                    clue_display[14].text = "Player B score: " + str(player_B)
                    clue_display[2].text = "PLAYER B WINS!" 
                    clue_display[2].color = clue.RED 
                    break 
            sleep(10) 
        clue_display.show()
