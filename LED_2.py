import RPi.GPIO as gpio
import time

global g_gpio_num

def setup(gpio_num, freq):
    global g_gpio_num
    gpio.setmode(gpio.BCM)
    g_gpio_num = gpio_num
    gpio.setup(g_gpio_num, gpio.OUT)

    g_gpio_num = gpio.PWM(g_gpio_num, freq)
    g_gpio_num.start(0)

if __name__ == '__main__':
    try:
        gpio_num = int(input('Please input the BCM number of LED.'))
        setup(gpio_num, 100)

        step = 1
        while True:
            for i in range(0, 101, step):
                g_gpio_num.ChangeDutyCycle(i)
                time.sleep(0.1)
            for i in range(100, -1, -step):
                g_gpio_num.ChangeDutyCycle(i)
                time.sleep(0.1)
    except KeyboardInterrupt:
        gpio.cleanup()
