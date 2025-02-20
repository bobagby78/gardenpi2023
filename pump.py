
#imports
from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BOARD)

testChannel1 = 37

pump = 33

GPIO.setup(pump, GPIO.OUT)
GPIO.setup(testChannel1, GPIO.OUT)



time = datetime.now()

print('*** starting pump at ', time, '.***')

def runPump():

    for _ in range(59):

        GPIO.output(pump, GPIO.LOW)
        GPIO.output(testChannel1, GPIO.LOW)
        print('pump on')
        sleep(45)
        GPIO.output(pump, GPIO.HIGH)
        GPIO.output(testChannel1, GPIO.HIGH)
        print('pump off')
        sleep(15)

runPump()
