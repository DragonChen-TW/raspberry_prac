from RPi import GPIO as gpio
import time, os

import hw2pro_light as light
import hw2pro_audio as audio

# ============ Status ============
# 1
def stop():
    global lights, status
    light.turnOFF(lights['green'])
    audio.stop()
    light.turnON(lights['yellow'])
    status = 1
# 2
def play():
    global lights, status
    light.turnOFF(lights['yellow'])
    audio.play()
    light.turnON(lights['green'])
    status = 2
def unpause():
    global lights, status
    light.turnOFF(lights['red'])
    audio.unpause()
    light.turnON(lights['green'])
    status = 2
# 3
def pause():
    global lights, status
    light.turnOFF(lights['green'])
    audio.pause()
    light.turnON(lights['red'])
    status = 3


# next song
def nextSong():
    global lights, status
    light.turnOFF(lights['green'])
    light.blink(lights, 3)
    audio.nextSong()
    light.turnON(lights['yellow'])
    status = 1

# ============ Status ============

def trigger(gpio_num):
    if gpio.input(gpio_num):
        global lights, status, count
        if status == 1:
            play()
            printStatus()
        elif status == 2:
            count += 1
            print('trigger')
        elif status == 3:
            unpause()
            printStatus()


def printStatus():
    global status, count
    os.system('clear')
    if status == 1:
        str_status = 'STOP'
    elif status == 2:
        str_status = 'PLAYING'
    elif status == 3:
        str_status = 'PAUSE'
    print('=========================')
    print('||       {:^7}       ||'.format(str_status))
    print('|| Status: {}  Count: {} ||'.format(status, count))
    print('=========================')

if __name__ == '__main__':
    try:
        lights = {'red':16, 'yellow':20, 'green':21}
        gpio_PIR = 14
        light.setup(lights, gpio_PIR)
        audio.setup()
        gpio.add_event_detect(gpio_PIR, gpio.RISING, callback=trigger, bouncetime=1)

        status = 1
        count = 0

        while True:
            printStatus()
            time.sleep(10)
            if status == 2:
                if count == 1:
                    pause()
                elif count == 2:
                    stop()
                elif count >= 3:
                    nextSong()
                count = 0
    finally:
        gpio.cleanup()
