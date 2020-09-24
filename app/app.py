from __future__ import print_function
import time
import subprocess


def play_audio():
    audio = '/home/pi/pi_loop/app/garbage.mp3'
    print('playing {}'.format(audio))
    subprocess.call(['mpg321', audio])


def play_sound_continuously():
    """Continuously plays the sound"""
    try:
        while True:
            play_audio()
            time.sleep(5)
    except KeyboardInterrupt:
	    print('Exiting...')


if __name__ == '__main__':
    play_sound_continuously()
