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

systemActivted = False



while True:
    input_knop1 = gpio.input(17)
    input_knop2 = gpio.input(27)
    input_knop3 = gpio.input(5)
    input_knop4 = gpio.input(6)
    input_motion = gpio.input(19)

    if input_knop1 == True:
        print('Systeem is geactiveerd!')
        green.blink()
        sleep(5)
        systemActivted = True
        green.off()
        green.on()

    if input_motion == True:
        print('Beweging gedecteerd...')
        if systemActivted == True:
            authKey = input('Voer uw toegangscode in: ')
            yellow.blink()
