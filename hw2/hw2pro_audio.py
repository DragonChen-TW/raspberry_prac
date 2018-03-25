from pygame.mixer import init
from pygame.mixer import music
import time

def setup():
    init()
    music.load('powerless.mp3')

def stop():
    music.stop()
def play():
    music.play()
def unpause():
    music.unpause()
def pause():
    music.pause()
def nextSong():
    music.load('slow.mp3')
