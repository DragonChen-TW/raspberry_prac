import RPi.GPIO as gpio
from pydub import AudioSegment
import numpy as np
import time

global p
def setup():
    global p
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    p = gpio.PWM(17, 100)  # why can I just setting freq=1
    p.start(0)

def changeLED(signal):
    # signal should be 0~100 !
    global p
    p.ChangeDutyCycle(signal)

if __name__ == '__main__':
    try:
        # setup
        setup()

        # variable setting
        SEC = 1000
        CHUNK = 200
        rms_list = []

        # get data from mp3
        song = AudioSegment.from_mp3('mp3/lonely.mp3')
        song = song[0:70 * SEC]

        for i in range(CHUNK,len(song[:30000]) + CHUNK, CHUNK):
            rms_list.append(song[i - CHUNK:i + CHUNK].rms)

        for i in range(len(rms_list)):
            signal = rms[i] / 6000 * 100
            print('{} seconds. rms = {} signal = {}'.format(i * CHUNK / SEC,rms_list[i], signal))
            changeLED(signal)
            time.sleep(CHUNK / SEC)
    finally:
        gpio.cleanup()
        pass
