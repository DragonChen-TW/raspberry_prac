import RPi.GPIO as gpio
import Adafruit_DHT
import time

def setup():
    global gpio_tri, gpio_echo, gpio_temp, sensor
    gpio.setmode(gpio.BCM)
    gpio_tri = 7
    gpio_echo = 12
    gpio_temp = 4

    gpio.setup(gpio_tri, gpio.OUT)
    gpio.setup(gpio_echo, gpio.OUT)
    sensor = Adafruit_DHT.DHT11

def send_trigger():
    global gpio_tri
    gpio.output(gpio_tri, gpio.HIGH)
    time.sleep(0.00001)
    gpio.output(gpio_tri, gpio.LOW)

def get_speed():
    global sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_temp)
    print('>>', humidity, temperature)
    speed = 33100 + 26 * 60
    return speed

def get_distance(speed):
    global gpio_echo
    send_trigger()

    print('start')

    while gpio.input(gpio_echo) == 0:
        start_t = time.time()
    print('mid')
    while gpio.input(gpio_echo) == 1:
        stop_t = time.time()

    print('end')

    time_elapsed = stop_t - start_t
    distance = (time_elapsed * speed) / 2

    print(distance)

    return distance

if __name__ == '__main__':
    try:
        setup()

        while True:
            speed = get_speed()
            dist = get_distance(speed)
            print('output:')
            print('Measured Distance = %.lf cm'.format(dist))
            time.sleep(1)
    finally:
        gpio.cleanup()
