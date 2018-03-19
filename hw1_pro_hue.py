from pydub import AudioSegment

song = AudioSegment.from_mp3('./ocean.mp3')

print(song[:2000])
print(song.raw_data[:2000], end=' ')
