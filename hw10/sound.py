import RPi.GPIO as GPIO
import Adafruit_DHT
import time

def setup():
    global gpio_tri, gpio_temp, gpio_temp
    gpio.setmode(gpio.BCM)
    gpio_tri = 21
    gpio_echo = 20
    gpio_temp = 4

    gpio.setup(gpio_tri, gpio.OUT)
    gpio.setup(gpio_echo, gpio.OUT)
    # sensor = Adafruit_DHT.DHT11

def send_trigger():
    global gpio_tri
    gpio.output(gpio_tri, gpio.HIGH)
    time.sleep(0.00001)
    gpio.output(gpio_tri, gpio.LOW)

def get_speed():
    # humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_temp)
    speed = 33100 + 26 * 60
    return speed

def get_distance():
    send_trigger()

    while gpio.input(gpio_echo) == 0:
        start_t = time.time()
    while gpio.input(gpio_echo) == 1:
        stop_t = time.time()

    time_elapsed = stop_t - start_t
    distance = (time_elapsed * speed) / 2

    return distance

if __name__ == '__main__':
    try:
        setup()

        while True:
            speed = get_speed()
            dist = distance(speed)
            print('Measured Distance = %.lf cm'.format(dist))
            time.sleep(1)
    finally:
        gpio.cleanup()
