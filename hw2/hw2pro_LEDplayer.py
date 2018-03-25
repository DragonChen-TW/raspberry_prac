from RPi import GPIO as gpio
import time

import hw2pro_light as light
import hw2pro_audio as audio

def trigger(gpio_num):
    global lights, status, count
    print('trigger status={}'.format(status))

    if status == 1:
        play()
    elif status == 2:
        count += 1
    elif status == 3:
        unpause()

if __name__ == '__main__':
    try:
        lights = {'red':16, 'yellow':20, 'green':21}
        gpio_PIR = 14
        light.setup(lights, gpio_PIR)
        audio.setup()
        gpio.add_event_detect(gpio_PIR, gpio.RISING, callback=trigger, bouncetime=1)

        status = 1
        count = 0
        i = 0

        while True:
            time.sleep(10)
            print('{} times, count is {}'.format(i,count))
            i += 1
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
    status = 2

# ============ Status ============
