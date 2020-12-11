"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.
To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython
Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
import paho.mqtt.client as mqtt
import ast

def display_text(clue_Data):
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(*clue_Data["accelerometer"])
    clue_data[1].text = "Gyro: {} {} {} dps".format(*clue_Data["gyro"])
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(*clue_Data["magnetometer"])
    clue_data[3].text = "Pressure: {} hPa".format(clue_Data["pressure"])
    clue_data[4].text = "Altitude: {:.0f} m".format(clue.altitude)
    clue_data[5].text = "Temperature: {} C".format(clue_Data["temperature"])
    clue_data[6].text = "Humidity: {} %".format(clue_Data["humidity"])
    clue_data[7].text = "Proximity: {}".format(clue.proximity)
    clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(*clue_Data["color"])
    clue_data.show()

data ={
    'accelerometer':(0,0,0),
    'gyro':(0,0,0)
    'temperature': 0,
    'pressure':1013,
    'magnetometer':(0,0,0),
    'humidity':0,
    'proximity':0,
    'color':(0,0,0,0)
}


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("clue-slider")
        display_text(data)

def on_message(client, userdata, message):
    dataFromHtml = ast.literal_eval(message.payload.decode())
    data["accelerometer"] = (int(dataFromHtml["accelX"]),int(dataFromHtml["accelY"]),int(dataFromHtml["accelZ"]))
    data["gyro"] = (int(dataFromHtml["gyroX"]), int(dataFromHtml["gyroY"]),int(dataFromHtml[gyroZ]))
    data["temperature"] = int(dataFromHtml["temp"])
    data['pressure'] = int(dataFromHtml['pressure'])
    data["magnetometer"] = (int(dataFromHtml["magnetX"]), int(dataFromHtml["magnetY"]),int(dataFromHtml["magnetZ"]))
    data["humidity"] = int(dataFromHtml["humidity"])
    data["proximity"] = int(dataFromHtml["proximity"])
    data["color"] = (int(dataFromHtml["colorR"]), int(dataFromHtml["colorG"]), int(dataFromHtml["colorB"]),int(dataFromHtml["colorC"]))

    display_text(data)

# clue.sea_level_pressure = 1020


clue_data = clue.simple_text_display(text_scale=2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()