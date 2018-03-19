import RPi.GPIO as gpio
import time
from multiprocessing import Process

def setup():
    lights = [17, 22, 27,  16, 20, 21]
    gpio.setmode(gpio.BCM)
    for light in lights:
        gpio.setup(light, gpio.OUT)


def turnOnLED(light_num, light_name):
    gpio.output(light_num[light_name], gpio.HIGH)
def turnOffLED(light_num, light_name):
    gpio.output(light_num[light_name], gpio.LOW)


def light_round(light_num, start):
    # light_setting = [['red',15], ['green',8], ['yellow',5]]
    light_setting = [['green',3], ['yellow',3], ['red',5]]

    # setting that i to start light type
    i = 0
    while i < 3:
        if light_setting[i][0] == start:
            break
        i += 1

    # infinite light loop
    while True:
        light(light_num, light_setting[i])
        i += 1
        if i >= 3:
            i = 0

def light(light_num, light_sec):
    print(light_sec[0], light_sec[1])
    if light_sec[0] == 'yellow':
        for sec in range(light_sec[1]):     # light_sec[1] is the second
            turnOnLED(light_num, 'yellow')
            time.sleep(0.5)
            turnOffLED(light_num, 'yellow')
            time.sleep(0.5)
    else:
        turnOnLED(light_num, light_sec[0])
        time.sleep(light_sec[1])
        turnOffLED(light_num, light_sec[0])


if __name__ == '__main__':
    try:
        setup()

        th1 = Process(target=light_round, args=({'red':17, 'yellow':27, 'green':22}, 'green',))
        th2 = Process(target=light_round, args=({'red':16, 'yellow':20, 'green':21}, 'red',))
        th1.start()
        th2.start()
        th1.join()
        th2.join()
    finally:
        # run this after shut down program using ctrl+c
        print('finish')
        gpio.cleanup()
