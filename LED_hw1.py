import RPi.GPIO as gpio
import time

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(27, gpio.OUT)
    gpio.setup(22, gpio.OUT)



if __name__ == '__main__':
    setup()

    gpio.output(17, gpio.HIGH)
    gpio.output(27, gpio.HIGH)
    gpio.output(22, gpio.HIGH)

    time.sleep(5)

    gpio.cleanup()
