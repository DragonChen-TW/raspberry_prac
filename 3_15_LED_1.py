import RPi.GPIO as gpio
import time

def setup(gpio_num, OUT_IN):
    gpio.setmode(gpio.BCM)

    if OUT_IN == 'IN':
        gpio.setup(gpio_num, gpio.IN)
    elif OUT_IN == 'OUT':
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
        gpio_num = 7
        setup(gpio_num, 'IN')
        print('The status of gpio {} is {}'.format(gpio_num,getStatus(gpio_num)))
        setup(gpio_num, 'OUT')

        while True:
            print('Turn it on')
            turnOnLED(gpio_num)
            time.sleep(1)
            print('Turn it off')
            turnOffLED(gpio_num)
            time.sleep(1)
    except KeyboardInterrupt:
        gpio.cleanup()
