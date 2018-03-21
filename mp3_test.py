from pydub import AudioSegment
import matplotlib.pyplot as plt
import numpy as np

def positive(n):
    if n <= 0:
        return 0
    else:
        return n

song = AudioSegment.from_mp3('mp3/lonely.mp3')
# song = song.set_frame_rate(10)
song = song.get_array_of_samples()
song = np.abs(song)
song_clean = [positive(each) for each in song]

print(len(song))

plt.plot(song_clean)
plt.show()
