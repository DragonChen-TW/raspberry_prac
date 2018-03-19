from pydub import AudioSegment

song = AudioSegment.from_mp3('./ocean.mp3')
song = song.get_array_of_samples()

print(song[:2000])

for i in range(0,10000,100):
    print(song[i])
