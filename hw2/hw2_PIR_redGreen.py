import RPi.GPIO as gpio
import time

def setup(gpio_num, OUT_IN):
    if OUT_IN == 'IN':
        gpio.setup(gpio_num, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    elif OUT_IN == 'OUT':
        gpio.setup(gpio_num, gpio.OUT)

def motion(gpio_num):
    global status
    if gpio.input(gpio_num) and status == False:
        print('PIR detected !')
        status = True

def LED_blink(gpio_num, times):
    for i in range(times):
        gpio.output(gpio_num, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(gpio_num, gpio.LOW)
        time.sleep(0.5)
def LED_on(gpio_num, secs):
    gpio.output(gpio_num, gpio.HIGH)
    time.sleep(secs)
    gpio.output(gpio_num, gpio.LOW)

if __name__ == '__main__':
    try:
        # global variable setting
        status = False
        gpio_PIR = 14
        gpio1 = 21
        gpio2 = 20

        gpio.setmode(gpio.BCM)
        # PIR
        setup(gpio_PIR, 'IN')
        # redGreen
        setup(gpio2, 'OUT')
        setup(gpio1, 'OUT')

        gpio.add_event_detect(gpio_PIR, gpio.RISING, callback=motion, bouncetime=300)

        while True:
            LED_blink(gpio1, 1)
            if status == True:
                LED_on(gpio1,2)
                LED_on(gpio2,4)
                status = False
    finally:
        gpio.cleanup()
