#imports
from time import sleep
import RPi.GPIO as GPIO
from datetime import datetime
#Tell the GPIO pin how to read
GPIO.setmode(GPIO.BOARD)

#assign lights to pins
growLight = 35 #grow light outlet num 2
mainLight = 31 #10galtank outlet num 4
auxLight = 29  #8 galtank outlet num 5

#create a light/pin array
pins = [growLight, mainLight, auxLight]

#set the pins as output, not input
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

time = datetime.now()

print('*** starting lights at ', time, '.***')

def runLights():
#turn on all the lights
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
        print('growLight on')
        print('tank lights on')

#wait 12 hours
    sleep(43200)

#kill aquarium lights
    GPIO.output(mainLight, GPIO.HIGH)
    GPIO.output(auxLight, GPIO.HIGH)
    print('tank lights off')

# wait 2 hours
    sleep(7200)

#kill grow light
    GPIO.output(growLight, GPIO.HIGH)
    print('growLight off')

#grow light runs for 14 hours a day

    sleep(50400)

#fire the function when the file is run by the crons
runLights()
