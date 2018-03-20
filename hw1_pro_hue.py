from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt

song = AudioSegment.from_mp3('mp3/lonely.mp3')
song = song.set_frame_rate(192)
song = song.get_array_of_samples()
song = np.abs(song)

# for i in range(1,10000,200):
#     print(i, song[i])

plt.plot(song[:9000])
plt.show()
