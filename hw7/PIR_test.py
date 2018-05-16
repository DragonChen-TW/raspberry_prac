import PIR, time
import RPi.GPIO as gpio

def test():
    PIR.setup(14)
    while True:
        print(gpio.input(14))
        time.sleep(1)

if __name__ == '__main__':
    try:
        test()
    finally:
        PIR.clean()
