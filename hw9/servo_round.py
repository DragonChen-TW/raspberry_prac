import RPi.GPIO as gpio
import time

def setup():
    gpio.setmode(gpio.BCM)
    gpio.setup(3, gpio.OUT)


    pwm = gpio.PWM(3, 50)
    pwm.start(0)
    gpio.output(3, gpio.HIGH)

def setAngle(angle):
    global pwm
    duty_cycle = 1/20 * angle + 3
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)
    pwm.ChangeDutyCycle(0)

if __name__ == '__main__':
    setup()


    setAngle(180)
    setAngle(0)
    setAngle(90)
    time.sleep(1)


    pwm.stop()
    gpio.cleanup()
