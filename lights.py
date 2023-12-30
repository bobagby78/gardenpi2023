#imports
from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BOARD)

light = 35

GPIO.setup(light, GPIO.OUT)



time = datetime.now()

print('*** starting lights at ', time, '.***')

def runLights():

    GPIO.output(light, GPIO.LOW)
    print('light on')
    sleep(43200)
    GPIO.output(light, GPIO.HIGH)
    print('light off')

runLights()
