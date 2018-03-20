import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)

try:
    p = gpio.PWM(17, 1)  # why can I just setting freq=1
    p.start(100)

    while True:
        for i in range(0, 101, 5):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)
        # time.sleep(1)
        for i in range(100, -1, -5):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)
finally:
    gpio.cleanup()
