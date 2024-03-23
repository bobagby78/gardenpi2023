#imports
from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BOARD)

relay1 = 37
relay2 = 35
relay3 = 33
relay4 = 31
relay5 = 29
relay6 = 15
relay7 = 13
relay8 = 11

relays = [relay1, relay2, relay3, relay4, relay5, relay6, relay7, relay8]

for relay in relays:
    GPIO.setup(relay, GPIO.OUT)

    GPIO.output(relay, GPIO.HIGH)
