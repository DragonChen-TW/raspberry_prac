from RPi import GPIO as gpio

# global
stats = 1
# 1 ==> stop
# 2 ==> play
# 3 ==> pause

def setup(lights, gpio_PIR):
    gpio.setmode(gpio.BCM)
    gpio.setup(gpio_PIR, gpio.IN)
    for i in lights:
        gpio.setup(lights[i], gpio.OUT)
    # for stop
    gpio.output(lights['yellow'], gpio.HIGH)

def turnON(gpio_num):
    gpio.output(gpio_num, gpio.HIGH)

def turnOFF(gpio_num):
    gpio.output(gpio_num, gpio.LOW)
