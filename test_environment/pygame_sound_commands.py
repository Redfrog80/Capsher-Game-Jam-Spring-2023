

#Pygame audio
from pygame import *

jump_sound = pygame.mixer.Sound("jump.wav") # loads sounds

grass_sound = [pygame.mixer.Sound("grass.wav"),pygame.mixer.Sound("grass_2.wav")] # loads two sounds to be played randomly

pygame.mixer.music.load("music.wav") # loads music

pygame.mixer.music.play(-1) # plays music indefinitely

'''
https://spotify.github.io/pedalboard/
https://pytorch.org/tutorials/beginner/audio_preprocessing_tutorial.html
https://www.youtube.com/watch?v=z0aOffHrTac
https://www.pygame.org/docs/ref/mixer.html

'''