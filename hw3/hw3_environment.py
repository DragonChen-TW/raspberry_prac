import Adafruit_DHT
import time
import RPi.GPIO as gpio
import threading as th
import hw3_light as light
import hw3_beep as beep

if __name__ == '__main__':
    try:
        sensor = Adafruit_DHT.DHT11
        sensor_num = 14
        lights = {'red':20, 'yellow':16, 'green':21}

        light.setup(lights)

        while True:
            cur_time = time.ctime()
            wet, temp = Adafruit_DHT.read_retry(sensor, sensor_num)

            if wet and temp:
                print('{} >> wet = {}, temp = {}'.format(cur_time, wet, temp))
                light.turnOFFALL(lights)
                if temp >= 31:
                    light.turnON(lights['red'])
                    beep_th = beep_th.Thread(target=beep.bbeepTimes, args=(10,))
                    beep_th.start()
                elif temp >= 27:
                    light.turnON(lights['yellow'])
                else:
                    light.turnON(lights['green'])
            else:
                print('Fail to get reading!')
            beep_th.join()
            time.sleep(5)
    finally:
        light.end()
