from pydub import AudioSegment

song = AudioSegment.from_mp3('./ocean.mp3')

print(song[:2000])
for i in range(0,10000,100):
    print(int(song.raw_data[i]))
