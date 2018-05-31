import RPi.GPIO as gpio
import time

def setup():
    global pwm
    pwm = gpio.PWM(3, 50)
    pwm.start(0)
    gpio.output(3, gpio.HIGH)

def setAngle(angle):
    global pwm
    duty_cycle = 1/20 * angle + 3
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(0.2)
    pwm.ChangeDutyCycle(0)

def cleanup():
    global pwm
    pwm.stop()
    gpio.cleanup()


if __name__ == '__main__':
    setup()

    setAngle(180)

    cleanup()
