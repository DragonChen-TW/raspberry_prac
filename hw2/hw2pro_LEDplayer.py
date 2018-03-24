from RPi import GPIO as gpio
import time

import hw2pro_light as light

def trigger(gpio_num):
    print('trigger')
    global status, lights
    print(status)
    if status == 1:
        light.turnOFF(lights['yellow'])
        light.turnON(lights['green'])
        status = 2
    else:
        light.turnON(lights['green'])
        light.turnOFF(lights['yellow'])
        status = 1

if __name__ == '__main__':
    try:
        lights = {'red':16, 'yellow':20, 'green':21}
        gpio_PIR = 14
        light.setup(lights, gpio_PIR)
        gpio.add_event_detect(gpio_PIR, gpio.RISING, callback=trigger, bouncetime=300)
        status = 1
        # 1 ==> stop
        # 2 ==> play
        # 3 ==> pause

        while True:
            time.sleep(1)
    finally:
        gpio.cleanup()
