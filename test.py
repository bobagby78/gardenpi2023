# test to see if the cronjob is running
# set an LED to turn on/off 3 times in rapid succession
# run the cron once every second (or every 5???) 

#led on pin 12

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

led = 12

GPIO.setup(led, GPIO.OUT)

GPIO.output(led, GPIO.HIGH)
sleep(.1)
GPIO.output(led, GPIO.LOW)
sleep(.1)
GPIO.output(led, GPIO.HIGH)
sleep(.1)
GPIO.output(led, GPIO.LOW)
sleep(.1)
GPIO.output(led, GPIO.HIGH)
sleep(.1)
GPIO.output(led, GPIO.LOW)
sleep(.1)

