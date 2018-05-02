import RPi.GPIO as gpio
import time

def setupAll():
    gpio.setmode(gpio.BCM)
    global col_led, row_led
    for i in col_led + row_led:
        try:
            gpio.setup(i, gpio.OUT)
        except:
            print(str(i) + "wasn't be setuped.")
col_led = [17, 27, 22, 5, 6, 13, 19, 26]
row_led = [15, 18, 23, 24, 12, 16, 20, 21]

if __name__ == '__main__':
    try:
        setupAll()


        for i in col_led[0:3]:
            gpio.output(i, gpio.LOW)
        for i in row_led[0:3]:
            gpio.output(i, gpio.HIGH)


        time.sleep(10)

    finally:
        gpio.cleanup()
