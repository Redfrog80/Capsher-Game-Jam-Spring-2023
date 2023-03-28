import pygame
import os

def load_sounds(self, directory : str = "sounds/"):
    for filename in os.listdir(directory):
        print(filename)