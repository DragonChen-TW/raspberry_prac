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
    p.start(100)

def changeLED(signal):
    global p
    p.ChangeDutyCycle(signal)

if __name__ == '__main__':
    try:
        setup()

        song = AudioSegment.from_mp3('mp3/lonely.mp3')
        song = song.set_frame_rate(192)
        song = song.get_array_of_samples()
        song = np.abs(song)

        max_signal = 20000

        for i in range(0,20000,100):
            print(i, song[i] * 100 / max_signal)
            changeLED(song[i] * 100 / max_signal)
            time.sleep(0.1)
    finally:
        gpio.cleanup()
