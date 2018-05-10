import RPi.GPIO as gpio
import LED, time

def motion(gpio_num):
    global count
    if gpio.input(gpio_num):
        if not gpio.input(23):
            count += 1
            LED.turnON(2)
            print('Motion detected {}.'.format(count))
            print('LDR is {}'.format(gpio.input(23)))
    else:
        LED.turnOFF(2)
        print('Motion not detected')

if __name__ == '__main__':
    try:
        gpio.setmode(gpio.BCM)
        LED.setup(2, 'out')
        gpio.setup(14, gpio.IN, pull_up_down=gpio.PUD_DOWN) #PIR
        gpio.setup(23, gpio.IN) # LDR

        count = 0
        gpio.add_event_detect(14, gpio.BOTH, callback=motion, bouncetime=150)
        while True:
            time.sleep(1)
    finally:
        gpio.cleanup()
