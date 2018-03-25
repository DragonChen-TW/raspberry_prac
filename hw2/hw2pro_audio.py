from pygame.mixer import init
from pygame.mixer import music
import time

if __name__ == '__main__':
    # init(frequency=22050, size=-16, channels=2, buffer=4096)
    init()
    music.load('powerless.mp3')
    music.play()
    while True:
        time.sleep(3)
        music.pause()
        time.sleep(3)
        music.unpause()
        print('looping')
