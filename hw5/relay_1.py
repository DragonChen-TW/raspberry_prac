import RPi.GPIO as gpio
import LED, time

if __name__ == '__main__':
    try:
        gpio.setmode(gpio.BCM)
        LED.setup(2, 'out')
        while True:
            LED.turnON(2)
            time.sleep(1)
            LED.turnOFF(2)
            time.sleep(1)
    finally:
        gpio.cleanup()
