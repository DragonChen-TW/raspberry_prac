import RPi.GPIO as gpio
import time, LED

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(2, gpio.IN)
    gpio.setup(16, gpio.OUT)

def turnOnOff(gpio_num, LDR):
    if LDR == 1:
        LED.turnON(gpio_num)
    else:
        LED.turnOFF(gpio_num)

if __name__ == '__main__':
    setup()
    while True:
        turnOnOff(16, gpio.input(2))
        print(gpio.input(2))
        time.sleep(1)
