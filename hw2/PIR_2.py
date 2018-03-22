import RPi.GPIO as gpio
import time

def setup(gpio_num, OUT_IN):
    gpio.setmode(gpio.BCM)
    if OUT_IN == 'IN':
        gpio.setup(gpio_num, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    elif OUT_IN == 'OUT':
        gpio.setup(gpio_num, gpio.OUT)

count = 0
def motion(gpio_num):
    global count

    if gpio.input(gpio_num):
        count += 1
        print('Motion detected {} times.'.format(count))
        LED_blink(12, 3)
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
        setup(15, 'IN')
        setup(12, 'OUT')
        gpio.add_event_detect(15, gpio.RISING, callback=motion, bouncetime=300)
        while True:
            time.sleep(1)
    finally:
        gpio.cleanup()
