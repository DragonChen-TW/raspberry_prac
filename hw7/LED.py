import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

def setup(gpio_num, ctr):
    if ctr == 'in':
        gpio.setup(gpio_num, gpio.IN)
    elif ctr == 'out':
        gpio.setup(gpio_num, gpio.OUT)

def turnON(gpio_num):
    gpio.output(gpio_num, gpio.HIGH)
def turnOFF(gpio_num):
    gpio.output(gpio_num, gpio.LOW)
