import RPi.GPIO as gpio
from pydub import AudioSegment
from threading import Thread
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
        CHUNK = 100
        rms = []

        # get data from mp3
        song = AudioSegment.from_mp3('mp3/lonely.mp3')
        song = song[0:70 * SEC]

        for i in range(CHUNK,len(song) + CHUNK*0.3, CHUNK):
            rms.append(song[i - CHUNK:i + CHUNK*0.3].rms)

        for i in range(len(rms)):
            signal = rms[i] / 6600 * 100
            print('{} seconds. rms = {} signal = {}'.format(i * CHUNK / SEC,rms[i], signal))
            th = Thread(target=changeLED, args=(signal,))
            th.start()
            time.sleep(CHUNK / SEC)
    finally:
        gpio.cleanup()
        pass
