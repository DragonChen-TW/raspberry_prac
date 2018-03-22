import RPi.GPIO as gpio
from pydub import AudioSegment
from threading import Thread
import numpy as np
import time

global lights = [17, 27, 22,  16, 20, 21]
def setup():
    global lights
    gpio.setmode(gpio.BCM)
    p = []
    for light in lights:
        gpio.setup(light, gpio.OUT)
        p.append(gpio.PWM(light, 100))  # why can I just setting freq=1
        p.start(0)
    lights = p

def changeLED(signal):
    # signal should be 0~100 !
    global lights
    signals = countSignal(signal)
    for i in range(len(lights)):
        lights[i].ChangeDutyCycle(signals[i])

def countSignal(signal):
    signals = [signal / 33 * 100,
        (signal - 33) / 33 * 100,
        (signal - 66) / 33 * 100 ]
    for i in range(len(signals)):
        if signals[i] > 100.0:
            signals[i] = 100.0
        elif signals[i] < 0:
            signals[i] = 0
    signals = signals * 2
    return signals

if __name__ == '__main__':
    try:
        # setup
        setup()

        global lights
        for light in lights:
            print(type(light))

        # variable setting
        SEC = 1000
        CHUNK = 100
        rms = []

        # get data from mp3
        song = AudioSegment.from_mp3('mp3/lonely.mp3')
        song = song[0:70 * SEC]

        for i in range(CHUNK,int(len(song) + CHUNK*0.3), CHUNK):
            rms.append(song[i - CHUNK:i + CHUNK*0.3].rms)

        for i in range(len(rms)):
            signal = rms[i] / 7000 * 100
            print('{} seconds. rms = {} signal = {}'.format(i * CHUNK / SEC,rms[i], signal))
            th = Thread(target=changeLED, args=(signal,))
            th.start()
            time.sleep(CHUNK / SEC)
    finally:
        gpio.cleanup()
        pass
