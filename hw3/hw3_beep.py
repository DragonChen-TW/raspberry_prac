import RPi.GPIO as gpio
import time

if __name__ == '__main__':
    time.sleep(2)
    beep=gpio.PWM(12,800)
    pwm_buzzer.satrt(0)
    pwm_buzzer.ChangeDutyCycle(50)
    pwm_buzzer.stop()
