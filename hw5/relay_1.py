import RPi.GPIO as gpio_num
import LED, time

if __name__ == '__main__':
    try:
        LED.setup(2, 'out')
        while True:
            LED.turnON(2)
            time.sleep(1)
            LED.turnOFF(2)
            time.sleep(1)
    finally:
        gpio.cleanup()
