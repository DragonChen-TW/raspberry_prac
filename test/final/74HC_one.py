import RPi.GPIO as gpio

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(16, gpio.OUT)


if __name__ =="__main__":
    try:
        setup()
        gpio.output(16, gpio.HIGH)
    finally:
        gpio.cleanup()
