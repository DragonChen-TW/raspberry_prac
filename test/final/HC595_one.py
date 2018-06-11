import RPi.GPIO as gpio
import time

def setup():
    # global variables
    global DS, SHCP, STCP
    # global CLK, MOSI, CE
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
        gpio.output(SHCP, gpio.LOW)
        gpio.output(DS, int(i))
        gpio.output(SHCP, gpio.HIGH)
        gpio.output(DS, 0)

def hc_out(data, delay=1):
    for each in data:
        gpio.output(STCP, gpio.LOW)
        shift(each)
        gpio.output(STCP, gpio.HIGH)
        time.sleep(delay)

    # clean
    for i in range(8):
        for j in range(8):
            gpio.output(DS, gpio.LOW)
        makeTick(SHCP)
    makeTick(STCP)

if __name__ =="__main__":
    try:
        setup()

        data = ['11110000', '10101010', '0000111100001111', '1100110011001100']
        data *= 3

        hc_out(data)
    finally:
        gpio.cleanup()
