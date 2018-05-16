import RPi.GPIO as gpio

def setup(gpio_num):
    gpio.setmode(gpio.BCM)
    gpio.setup(gpio_num, gpio.IN)
def clean():
    gpio.cleanup()
