import RPi.GPIO as gpio
import servo

gpio.setmode(gpio.BCM)
gpio.setup(3, gpio.OUT)
