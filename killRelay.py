#imports
from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BOARD)

testChannel1 = 37
testChannel2 = 35
pump = 33

GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

GPIO.output(29, GPIO.HIGH)
GPIO.output(31, GPIO.HIGH)
