import RPi.GPIO as gpio
import time

if __name__ == '__main__':
    beep_num = 12
    gpio.setmode(gpio.BCM)
    gpio.setup(beep_num, gpio.OUT)
    time.sleep(2)
    beep = gpio.PWM(beep_num,800)
    beep.satrt(0)
    beep.ChangeDutyCycle(50)
    beep.stop()

    gpio.cleanup()
