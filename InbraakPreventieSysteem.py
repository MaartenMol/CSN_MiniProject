#Inbraak Preventie Systeem gemaakt voor CSN project
#Gemaakt door Bastiaan Ebbenhorst, Joshua Offermans, Maarten Mol, Thomas Mocellin uit TICT-ICT-V1D


import RPi.GPIO as gpio
from gpiozero import LED
import time
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN)
gpio.setup(27, gpio.IN)
gpio.setup(19, gpio.IN)
gpio.setup(5, gpio.IN)
gpio.setup(6, gpio.IN)

green = LED(4)
red = LED(26)
yellow = LED(22)
bolb = LED(13)

Code = '2431'
Input = ''


while True:
        input_knop1 = gpio.input(17)
        input_knop2 = gpio.input(27)
        input_knop3 = gpio.input(5)
        input_knop4 = gpio.input(6)
        input_motion = gpio.input(19)
        if input_motion == True:
                print('Motion has been detected...')
                yellow.on()

        while len(Input) < 4:

            if input_knop1 == True:
                Input += '1'

            elif input_knop2 == True:
                Input += '2'

            elif input_knop3 == True:
                Input += '3'

            elif input_knop4 == True:
                Input += '4'




        if len(Input) == 4:
            if Input == Code:
                yellow.off()
                green.on()

            else:
                yellow.off()
                red.on()






