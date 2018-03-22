import RPi.GPIO as gpio
import time

def setup(gpio_num, OUT_IN):
    if OUT_IN == 'IN':
        gpio.setup(gpio_num, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    elif OUT_IN == 'OUT':
        gpio.setup(gpio_num, gpio.OUT)

status = False
def motion(gpio_num):
    if gpio.input(gpio_num):
        global status
        status = True
    # else:
    #     print('Motion not detected.')

def LED_blink(gpio_num, times):
    for i in range(times):
        gpio.output(gpio_num, gpio.HIGH)
        time.sleep(0.5)
        gpio.output(gpio_num, gpio.LOW)
        time.sleep(0.5)

if __name__ == '__main__':
    try:
        gpio.setmode(gpio.BCM)
        # PIR
        setup(15, 'IN')
        # redGreen
        setup(20, 'OUT')
        setup(21, 'OUT')

        gpio.add_event_detect(15, gpio.RISING, callback=motion, bouncetime=300)

        global status
        while True:
            LED_blink(21, 1)
            if status == True:
                LED_blink(20,2)
                status = False
    finally:
        gpio.cleanup()
