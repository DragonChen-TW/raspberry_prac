from pydub import AudioSegment

song = AudioSegment.from_mp3('ocean.mp3')

print(song[:2000])
