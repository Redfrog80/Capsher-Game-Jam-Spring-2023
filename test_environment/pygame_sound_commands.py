

#Pygame audio
from pygame import *

boost_sound = pygame.mixer.Sound("boost.wav") # loads sounds

shot_sound = [pygame.mixer.Sound("shot.wav"),pygame.mixer.Sound("shot_2.wav")] # loads two sounds to be played randomly

pygame.mixer.music.load("music.wav") # loads music

pygame.mixer.music.play(-1) # plays music indefinitely

'''
https://spotify.github.io/pedalboard/
https://pytorch.org/tutorials/beginner/audio_preprocessing_tutorial.html
https://www.youtube.com/watch?v=z0aOffHrTac
https://www.pygame.org/docs/ref/mixer.html

'''