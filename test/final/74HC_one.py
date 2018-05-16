import RPi.GPIO as gpio
import time

def setup():
    # global variables
    global DS, SHCP, STCP
    DS = 17
    SHCP = 27
    STCP = 22

    gpio.setmode(gpio.BCM)
    gpio.setup(DS, gpio.OUT)
    gpio.setup(SHCP, gpio.OUT)
    gpio.setup(STCP, gpio.OUT)

def makeTick(gpio_num):
    gpio.output(gpio_num, gpio.HIGH)
    gpio.output(gpio_num, gpio.LOW)

def shift(shift_data):
    for i in shift_data:
        print(i)
        gpio.output(DS, i)
        makeTick(SHCP)

def hc_out(data):
    for each in data:
        makeTick(SHCP)
        shift(each)
        makeTick(STCP)
        time.sleep(5)

if __name__ =="__main__":
    try:
        setup()
        hc_out([1, 1, 1, 1, 0, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0])
    finally:
        makeTick(STCP)
        gpio.cleanup()
