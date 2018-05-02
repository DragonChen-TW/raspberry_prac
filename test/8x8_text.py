import RPi.GPIO as gpio
import time

def setupAll():
    gpio.setmode(gpio.BCM)
    global col_led, row_led
    for i in col_led + row_led:
        print(str(i) + 'is setting')
        try:
            gpio.setup(i, gpio.OUT)
        except:
            print(i)
col_led = [17, 27, 22, 5, 6, 13, 19, 26]
row_led = [14, 15, 18, 23, 12, 16, 20, 21]

if __name__ == '__main__':
    try:
        setupAll()

        for i in row_led:
            gpio.output(i, gpio.HIGH)

        time.sleep(10)
        for i in col_led:
            gpio.output(i, gpio.LOW)

        time.sleep(10)
        for i in col_led:
            gpio.output(i, gpio.HIGH)
    except:
        gpio.cleanup()
