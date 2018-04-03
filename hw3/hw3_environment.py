import Adafruit_DHT
import time
import hw3hw3_light as light

if __name__ == '__main__':
    sensor = Adafruit_DHT.DHT11
    sensor_num = 14
    lights = {'red':20, 'yellow':16, 'green':21}

    while True:
        cur_time = time.ctime()
        wet, temp = Adafruit_DHT.read_retry(sensor, sensor_num)

        if wet and temp:
            print('{} >> wet = {}, temp = {}'.format(cur_time, wet, temp))
            light.turnOFFALL(lights)
            if temp >= 31:
                light.turnON(lights['red'])
            elif temp >= 27:
                light.turnON(lights['yellow'])
            else:
                light.turnON(lights['green'])
        else:
            print('Fail to get reading!')
        time.sleep(5)
