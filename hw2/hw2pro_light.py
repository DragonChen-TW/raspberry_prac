from RPi import GPIO as gpio

# global
stats = 1
# 1 ==> stop
# 2 ==> play
# 3 ==> pause

def setup(lights):
    gpio.setmode(gpio.BCM)
    for light in lights:
        gpio.setup(light, gpio.OUT)
    # for stop
    gpio.output(lights[1], gpio.HIGH)

def turnON(gpio_num):
    gpio.output(gpio_num, gpio.HIGH)

def turnOFF(gpio_num):
    gpio.output(gpio_num, gpio.LOW)
