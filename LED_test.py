import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)

p = gpio.PWM(17, 0.5)
p.start(1)
input('Press return to stop:')   # use raw_input for Python 2
p.stop()
gpio.cleanup()
