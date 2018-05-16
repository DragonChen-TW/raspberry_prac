import PIR, time
import RPi.GPIO as gpio

if __name__ == '__main__':
    PIR.setup(14)
    while True:
        print(gpio.input(14))
        time.sleep(1)
