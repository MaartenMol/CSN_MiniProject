#Inbraak Preventie Systeem gemaakt voor CSN project
#Gemaakt door Bastiaan Ebbenhorst, Joshua Offermans, Maarten Mol, Thomas Mocellin uit TICT-ICT-V1D

#Imports
import RPi.GPIO as gpio
from gpiozero import LED
from time import sleep
import telegram

#Telegram instellingen
channelID = str(-151964127)
bot = telegram.Bot('291634953:AAGkRRBensuLumtfz4LKZ3rE0ixUJCFKlo0')

#Zet modus GPIO's
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN)
gpio.setup(27, gpio.IN)
gpio.setup(19, gpio.IN)
gpio.setup(5, gpio.IN)
gpio.setup(6, gpio.IN)

#Defineer LEDjes
green = LED(4)
red = LED(26)
yellow = LED(22)
bolb = LED(13)

#Defineer standaard status systeem
armed = False
inbraak = False

#Systeem standby
print('Systeem staat standby!')
bot.sendMessage(chat_id=channelID, text='Het systeem staat klaar voor gebruik. Het systeem staat in standby mode.')
yellow.blink()

#Core funcionaliteit, code, detectie
def codeFunc():
    global armed
    global inbraak
    Code = '2431'
    Input = ''

    #Wachten op input
    while len(Input) < 4:
        input_knop1 = gpio.input(17)
        input_knop2 = gpio.input(27)
        input_knop3 = gpio.input(5)
        input_knop4 = gpio.input(6)

        #Input Toets 1
        if input_knop1 == True:
            Input += '1'
            print('Toets 1')
            bot.sendMessage(chat_id=channelID, text='De code word ingevoerd.')
            sleep(1)
            while input_knop1 == True:
                input_knop1 = gpio.input(17)

        #Input Toets 2
        elif input_knop2 == True:
            Input += '2'
            print('Toets 2')
            sleep(1)
            while input_knop2 == True:
                input_knop2 = gpio.input(17)

        #Input Toets 3
        elif input_knop3 == True:
            Input += '3'
            print('Toets 3')
            sleep(1)
            while input_knop3 == True:
                input_knop3 = gpio.input(17)

        #Input Toets 4
        elif input_knop4 == True:
            Input += '4'
            print('Toets 4')
            sleep(1)
            while input_knop4 == True:
                input_knop4 = gpio.input(17)

    #Check op 4 tekens voor code
    if len(Input) == 4:
        #Controleer correcte code
        if Input == Code:
            armed = False
            print('Systeem gedeactiveerd!')
            bot.sendMessage(chat_id=channelID, text='Het systeem is niet meer actief. Toegang toegestaan.')
            bolb.on()
            yellow.blink()
            green.off()

        #Alarm door foute code
        else:
            armed = False
            inbraak = True
            print('Inbraak gedetecteerd!')
            bot.sendMessage(chat_id=channelID, text='Het systeem heeft inbraak gedetecteerd. (Gebruik toets 4 om te resetten)')
            bolb.off()
            yellow.off()
            red.blink()
            green.off()

#Wacht op commands
while True:
    input_motion = gpio.input(19)
    knop1 = gpio.input(17)
    knop4 = gpio.input(6)

    #Systeem activeren
    if knop1 == True:
        print ('Systeem geactiveerd!')
        bot.sendMessage(chat_id=channelID, text='Het systeem is geactiveerd. Zodra er beweging is gedetecteerd moet de volgende toets volgorde gebruikt worden: toets 2 4 3 1')
        bolb.off()
        yellow.off()
        green.on()
        armed = True
        while knop1 == True:
            knop1 = gpio.input(17)

    #Systeem resetten
    if knop4 == True and inbraak == True:
        print ('Systeem bezig met resetten!')
        bot.sendMessage(chat_id=channelID, text='Het systeem is bezig met resetten.')
        red.off()
        yellow.on()
        green.on()
        red.on()
        sleep(5)
        print('Systeem gerest!')
        bot.sendMessage(chat_id=channelID, text='Het systeem is gereset. Het systeem staat nu in standby mode')
        yellow.blink()
        red.off()
        green.off()
        armed = False
        inbraak = False
        while knop1 == True:
            knop4 = gpio.input(17)

    #Sensor detectie
    if input_motion == True and armed == True:
        print('Mogelijke inbraak gedetecteerd!')
        bot.sendMessage(chat_id=channelID, text='Het systeem heeft mogelijke inbraak gedetecteerd. Voer de correcte volgorde van toetsen in.')
        green.off()
        yellow.on()
        codeFunc()
        sleep(1)
