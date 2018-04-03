import Adafruit_DHT
import time

if __name__ == '__main__':
    sensor = Adafruit_DHT.DHT11
    sensor_num = 14

    while True:
        cur_time = time.ctime()
        wet, temp = Adafruit_DHT.read_retry(sensor, sensor_num)

        if wet and temp:
            print('{} >> wet = {}, temp = {}'.format(cur_time, wet, temp))
        else:
            print('Fail to get reading!')
        time.sleep(5)
