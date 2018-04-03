from RPi import GPIO as gpio

def setup(lights):
    gpio.setmode(gpio.BCM)
    for i in lights:
        gpio.setup(lights[i], gpio.OUT)
        gpio.output(lights[i], gpio.LOW)

def turnON(gpio_num):
    gpio.output(gpio_num, gpio.HIGH)

def turnOFFALL(lighs):
    for i in lights:
        gpio.output(lights[i], gpio.LOW)
