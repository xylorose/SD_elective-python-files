from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt
from time import sleep



def on_connect(client, userdata, flags, rc):
    # print ("connected with result code" + str(rc))
    if rc == 0 :
        cp.red_led = True 
        client.subscribe("cpx-switch")
    
            

def on_message(client, userdata, msg):
    # print ( msg.topic + "" + msg.payload.decode())
    # while True:

    for f in range(10):
        if msg.payload.decode() == "true": 
            cp.pixels[f] = (255,255,255)
           
        elif msg.payload.decode() == "false":
            cp.pixels[f] = (0,0,0)
           

    



cp.red_led = False 

client= mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect("mqtt.eclipse.org" , 1883, 60)

client.loop_forever()