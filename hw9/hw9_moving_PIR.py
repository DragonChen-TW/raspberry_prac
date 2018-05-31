import RPi.GPIO as gpio
import servo, time

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(3, gpio.OUT) # servo's gpio
    gpio.setup(21, gpio.OUT) # LED's gpio
    gpio.setup(14, gpio.IN, pull_up_down=gpio.PUD_DOWN) # PIR's gpio

    servo.setup()

def detect(gpio_num):
    global status
    if gpio.input(gpio_num):
        status = True
        print('PIR detected !')
        gpio.output(21, gpio.HIGH)

        time.sleep(1)
        status = False
        gpio.output(21, gpio.LOW)
    else:
        status = False


if __name__ == '__main__':
    try:
        setup()
        status = False

        gpio.add_event_detect(14, gpio.RISING, callback=detect, bouncetime=300)

        while True:
            for i in range(-180, 180, 5):
                print(abs(i))
                servo.setAngle(abs(i))
                while status:
                    time.sleep(0.1)
    finally:
        servo.cleanup()
