from RPi import GPIO as gpio
import time

import hw2pro_light as light

def trigger(gpio_num):
    global status, lights, count
    print('trigger status={}'.format(status))
    # if status == 1:
    #     light.turnOFF(lights['yellow'])
    #     light.turnON(lights['green'])
    #     status = 2
    # elif status == 2:
    #     light.turnOFF(lights['green'])
    #     light.turnON(lights['yellow'])
    #     status = 1
    count += 1
    print(count)

if __name__ == '__main__':
    try:
        lights = {'red':16, 'yellow':20, 'green':21}
        gpio_PIR = 14
        light.setup(lights, gpio_PIR)
        gpio.add_event_detect(gpio_PIR, gpio.RISING, callback=trigger)
        
        status = 1
        count = 0
        # 1 ==> stop
        # 2 ==> play
        # 3 ==> pause

        while True:
            time.sleep(2)
    finally:
        gpio.cleanup()
