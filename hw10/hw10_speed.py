import RPi.GPIO as gpio
import Adafruit_DHT
import time

from pygame.mixer import init
from pygame.mixer import music

def setup():
    global gpio_tri, gpio_echo, gpio_temp, sensor
    gpio.setmode(gpio.BCM)
    gpio_tri = 7
    gpio_echo = 12
    gpio_temp = 4

    gpio.setup(gpio_tri, gpio.OUT)
    gpio.setup(gpio_echo, gpio.IN)
    sensor = Adafruit_DHT.DHT11

    init() # pygame init for sound
    music.load('mp3/police_car.mp3')

def send_trigger():
    global gpio_tri
    gpio.output(gpio_tri, gpio.HIGH)
    time.sleep(0.00001)
    gpio.output(gpio_tri, gpio.LOW)

def get_speed():
    global sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_temp)
    speed = 33100 + 26 * 60
    return speed

def get_distance():
    global gpio_echo
    send_trigger()

    while gpio.input(gpio_echo) == 0:
        start_t = time.time()
    while gpio.input(gpio_echo) == 1:
        stop_t = time.time()

    time_elapsed = stop_t - start_t
    speed = get_speed()
    distance = (time_elapsed * speed) / 2

    return distance

def get_velocity():
    global gpio_echo
    send_trigger()

    while gpio.input(gpio_echo) == 0:
        start_t = time.time()
    while gpio.input(gpio_echo) == 1:
        stop_t = time.time()

    time_elapsed = stop_t - start_t
    speed = get_speed()
    distance = (time_elapsed * speed) / 2

    if distance < 2 or distance > 400:
        dist_err = True
    else:
        dist_err = False

    global pre_dist, pre_time

    velocity = (distance - pre_dist) / (stop_t - pre_time)
    pre_dist = distance
    pre_time = stop_t

    return abs(velocity)

if __name__ == '__main__':
    try:
        setup()
        pre_dist = 30
        pre_time = 0

        while True:
            v = get_velocity()
            print('Measured Velocity = {} cm'.format(v))

            if v >= 30:
                music.play()
                for i in range(3):
                    gpio.output(13, gpio.HIGH)
                    time.sleep(0.5)
                    gpio.output(13, gpio.LOW)
                    time.sleep(0.5)
                music.stop()
            time.sleep(1)
    finally:
        gpio.cleanup()
