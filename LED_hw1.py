import RPi.GPIO as gpio
import time

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)

def redGreen(now):
    if now == 0:
        gpio.output(22, gpio.HIGH)
    elif now == 15:
        gpio.output(22, gpio.LOW)


if __name__ == '__main__':
    setup()

    for sec in range(0,30):
        print(sec)
        redGreen(sec)
        time.sleep(1)

    gpio.cleanup()
