import Adafruit_DHT
import time, math, LED

def heatStroke(temp, wet):
    return temp + wet * 0.1

def dewPoint(temp, wet):
    a = 17.271, b = 237.7
    d = (a * temp) / (b + temp) + math.log(wet / 100)
    return (b * temp) / (a - d)


if __name__ == '__main__':
    sensor = Adafruit_DHT.DHT11
    sensor_num = 14
    led1 = 20
    led2 = 21

    LED.setup(0, 'setup')
    LED.setup(led1, 'out')
    LED.setup(led2, 'out')


    while True:
        cur_time = time.ctime()
        wet, temp = Adafruit_DHT.read_retry(sensor, sensor_num)
        dew_point = dewPoint(temp, wet)
        heat_stroke = heatStroke(temp, wet)

        if wet and temp:
            print('{} >> wet = {}, temp = {}'.format(cur_time, wet, temp))
            print('heatStroke = {}, dewPoint = {}'.format(heat_stroke, dew_point))
        else:
            print('Fail to get reading!')
        time.sleep(5)
