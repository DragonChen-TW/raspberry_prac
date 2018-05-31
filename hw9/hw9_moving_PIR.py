import RPi.GPIO as gpio
import servo

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(3, gpio.OUT) # servo's gpio
    gpio.setup(21, gpio.OUT) # LED's gpio
    gpio.setup(4, gpio.IN) # PIR's gpio

    servo.setup()

def detect(gpio_num):
    global status
    if gpio.input(gpio_num):
        print('PIR detected !')
        status = True
    else:
        status = False


if __name__ == '__main__':
    try:
        setup()

        gpio.add_event_detect(detect, gpio.RISING, callback=motion, bouncetime=300)

        while True:
            servo.setAngle(0)
            servo.setAngle(180)
    finally:
        servo.cleanup()
