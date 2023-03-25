import pygame
import numpy as np
import os

class imageDict:
    def __init__(self, location : str = None) -> None:
        self.__image_dict__ = {}
        if location:
            self.load_images(location)
    
    def load_image(self, location  : str = "images/notfound.png"):
        key = os.path.split[1]
        if key:
            self.__image_dict__[key] = pygame.image.load(location).convert()
    
    def load_images(self, directory : str = "images/"):
        for filename in os.listdir(directory):
            if filename.endswith('.png'):
                path = os.path.join(directory,filename)
                key = filename[:-4]
                self.__image_dict__[key] = pygame.image.load(path).convert()
    
    def get_image(self, name : str, notFound = None):
        return self.__image_dict__.get(name, notFound)
    
    def get_image_dimensions(self, name : str, notFound = None):
        image = self.__image_dict__.get(name, None)
        if image != None:
            return np.array([image.get_width(), image.get_height()])
        else:
            return notFound