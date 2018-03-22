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
    # signal should be 0~100 !
    global p
    p.ChangeDutyCycle(signal)

if __name__ == '__main__':
    try:
        # setup
        setup()

        # get data from mp3
        song = AudioSegment.from_mp3('mp3/lonely.mp3')
        song = song.get_array_of_samples()
        song = np.abs(song)

        song_clean = []
        CHUNK = 100

        for i in range(CHUNK,7000000, CHUNK):
            data = song[i - CHUNK:i + CHUNK]
            peak = np.average(data)

            if peak > 12000:
                song_clean.append(12000)
            else:
                song_clean.append(peak)

        print(len(song_clean))

        # import matplotlib.pyplot as plt
        # plt.plot(song_clean)
        # plt.show()

        for i in range(len(song_clean)):
            print(i, song_clean[i] / 12000 * 100)
            changeLED(int(song[i] / 12000 * 100))
            time.sleep(1 / CHUNK)
    finally:
        gpio.cleanup()
        pass
