import RPi.GPIO as gpio
import time
def setup(gpio_num):
    gpio.setmode(gpio.BCM)
    gpio.setup(gpio_num, gpio.IN, pull_up_down=gpio.PUD_DOWN)

count = 0
def motion(gpio_num):
    global count

    if gpio.input(gpio_num):
        count += 1
        print('Motion detected {} times.'.format(count))
    else:
        print('Motion not detected.')


if __name__ == '__main__':
    try:
        setup(14)
        gpio.add_event_detect(14, gpio.BOTH, callback=motion, bouncetime=200)
        while True:
            time.sleep(1)
    finally:
        gpio.cleanup()
