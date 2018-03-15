import RPi.GPIO as gpio
import time

def setup(gpio_num, OUT_IN):
    gpio.setmode(gpio.BCM)

    if OUT_IN == 'IN':
        gpio.setup(gpio_num, gpio.IN)
    else OUT_IN == 'OUT':
        gpio.setup(gpio_num, gpio.OUT)

def turnOnLED(gpio_num):
    gpio.output(gpio_num, True)

def turnOffLED(gpio_num):
    gpio.output(gpio_num, False)

def getStatus(gpio_num):
    gpio_status = gpio.input(gpio_num)
    return gpio_status

if __name__ == '__main__':
    try:
        gpio_num = 5
        setup(gpio_num, 'IN')
        print(f'The status of gpio {gpio_num} is {getStatus(gpio_num)}')
        setup(gpio_num, 'OUT')

        while True:
            turnOnLED(gpio_num)
            time.sleep(1)
            turnOffLED(gpio_num)
            time.sleep(1)
    except KeyboardInterrupt:
        gpio.cleanup()
