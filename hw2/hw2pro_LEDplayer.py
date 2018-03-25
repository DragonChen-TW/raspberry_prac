from RPi import GPIO as gpio
import time

import hw2pro_light as light

def trigger(gpio_num):
    global status, lights, count
    print('trigger status={}'.format(status))

    light.turnON(lights['red'])
    if status == 1:
        # turn to play
        light.turnOFF(lights['yellow'])
        light.turnON(lights['green'])
        status = 2
    elif status == 2:
        count += 1
    elif status == 3:
        # continue play
        light.turnOFF(lights['red'])
        light.turnON(lights['green'])
        status = 2
    count += 1
    print(count)

    light.turnOFF(lights['red'])

if __name__ == '__main__':
    try:
        lights = {'red':16, 'yellow':20, 'green':21}
        gpio_PIR = 14
        light.setup(lights, gpio_PIR)
        gpio.add_event_detect(gpio_PIR, gpio.RISING, callback=trigger, bouncetime=1)

        status = 1
        count = 0
        # 1 ==> stop
        # 2 ==> play
        # 3 ==> pause

        while True:
            time.sleep(10)
            if status == 2:
                if count == 1:
                    # pause
                    light.turnOFF(lights['green'])
                    light.turnON(lights['red'])
                    status = 3
                elif count == 2:
                    # pause
                    light.turnOFF(lights['green'])
                    light.turnON(lights['yellow'])
                    status = 3
                elif count >= 3:
                    # pause
                    light.turnOFF(lights['green'])
                    light.blink(lights, 3)
                    status = 3
                count = 0

    finally:
        gpio.cleanup()
