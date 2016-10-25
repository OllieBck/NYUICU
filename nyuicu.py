import paho.mqtt.client as mqtt
import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("button")

def on_message(client, userdata, msg):
    if msg.payload == "led on":
        GPIO.output(21, GPIO.HIGH)
    if msg.payload == "led off":
  	GPIO.output(21, GPIO.LOW)
    if msg.payload == "fan on":
	GPIO.output(12, GPIO.HIGH)
    if msg.payload == "fan off":
	GPIO.output(12, GPIO.LOW)
    if msg.payload == "emergency":
	os.system("omxplayer /home/pi/Desktop/AudioICU/Emergency.m4a")
    if msg.payload == "yes":
	os.system("omxplayer /home/pi/Desktop/AudioICU/Yes.m4a")
    if msg.payload == "no":
	os.system("omxplayer /home/pi/Desktop/AudioICU/No.m4a")
    if msg.payload == "thankyou":
	os.system("omxplayer /home/pi/Desktop/AudioICU/ThankYou.m4a")
    print(str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.7", 1883, 60)

client.loop_forever()
