import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

def setup(gpio_num):
    gpio.setup(gpio_num, gpio.IN)
def clean():
    gpio.cleanup()
