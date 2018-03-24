from RPi import GPIO as gpio
import time

import hw2pro_light as light

def trigger():
    print(status)

if __name__ == '__main__':
    try:
        lights = {'red':16, 'yellow':20, 'green':21}
        gpio_PIR = 14
        light.setup(lights, gpio_PIR)
        gpio.add_event_detect(gpio_PIR, gpio.RISING, callback=trigger, bouncetime=300)

        while True:
            time.sleep(1)
    finally:
        pass
