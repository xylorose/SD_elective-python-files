from microbit import *
from time import sleep
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        display.show(Image.YES)
        client.subscribe("roseMarryJoyStickControl")
def on_message(client, userdata, msg):
    # print(msg.topic+" "+msg.payload.decode())
    print(msg.payload.decode())
    if msg.payload.decode() == "C":
        display.show(Image.HAPPY)
        pass
    elif msg.payload.decode() == "N":
        display.show(Image.ARROW_N)
    elif msg.payload.decode() == "S":
        display.show(Image.ARROW_S)
    elif msg.payload.decode() == "E":
        display.show(Image.ARROW_E)
    elif msg.payload.decode() == "W":
        display.show(Image.ARROW_W)
    elif msg.payload.decode() == "SE":
        display.show(Image.ARROW_SE)
    elif msg.payload.decode() == "SW":
        display.show(Image.ARROW_SW)
    elif msg.payload.decode() == "NW":
        display.show(Image.ARROW_NW)
    elif msg.payload.decode() == "NE":
        display.show(Image.ARROW_NE)
    
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()