import RPi.GPIO as gpio
from gpiozero import LED
from time import sleep
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

yellow.on()

while True:
        input_knop1 = gpio.input(17)
        input_knop2 = gpio.input(27)
        input_knop3 = gpio.input(5)
        input_knop4 = gpio.input(6)
        input_motion = gpio.input(19)
        if input_knop1 == True:
                print('The button 1 has been pressed...')
                green.on()
                sleep(1)
                green.off()
                while input_knop1 == True:
                        input_knop1 = gpio.input(17)
        elif input_knop2 == True:
                print('The button 2 has been pressed...')
                red.on()
                sleep(1)
                red.off()
                while input_knop2 == True:
                        input_knop2 = gpio.input(27)
        elif input_knop3 == True:
                print('The button 3 has been pressed...')
                red.on()
                sleep(1)
                red.off()
                while input_knop3 == True:
                        input_knop3 = gpio.input(5)
        elif input_knop4 == True:
                print('The button 4 has been pressed...')
                red.on()
                sleep(1)
                red.off()
                while input_knop4 == True:
                        input_knop4 = gpio.input(6)
        elif input_motion == True:
                print('Motion has been detected...')
                red.on()
                green.on()
                bolb.on()
                sleep(1)
                red.off()
