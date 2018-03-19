import RPi.GPIO as gpio
import time

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)

def turnOnLED(gpio_num):
    gpio.output(gpio_num, gpio.HIGH)
def turnOffLED(gpio_num):
    gpio.output(gpio_num, gpio.LOW)

def redGreen(now):
    if now == 0:
        turnOnLED(22)
    elif now == 15:
        turnOffLED(22)
        turnOnLED(27)
    elif now == 23:
        turnOffLED(27)
        turnOnLED(17)
    elif now == 28:
        turnOffLED(17)

if __name__ == '__main__':
    setup()

    for sec in range(0,30):
        print(sec)
        redGreen(sec)
        time.sleep(0.5)

    gpio.cleanup()
