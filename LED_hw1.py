import RPi.GPIO as gpio
import time
from threading import Thread

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)


light_num = {'red':17, 'yellow':22, 'green':27}
def turnOnLED(light_name):
    global light_num
    gpio.output(light_num[light_name], gpio.HIGH)
def turnOffLED(light_name):
    gpio.output(light_num[light_name], gpio.LOW)


def light_round(start):
    light_setting = [['red',15], ['green',8], ['yellow',5]]
    i = 0
    while True:
        light(light_setting[i])
        i += 1
        if i >= 3:
            i = 0

def light(light_sec):
    if light_sec[0] == 'yellow':
        for sec in range(light_sec[1]):     # light_sec[1] is the second
            turnOnLED('yellow')
            time.sleep(0.5)
            turnOffLED('yellow')
            time.sleep(0.5)
    else:
        turnOnLED(light_sec[0])
        time.sleep(light_sec[1])
        turnOffLED(light_sec[0])


if __name__ == '__main__':
    # setting GPIO
    setup()

    light_round('red')

    gpio.cleanup()
