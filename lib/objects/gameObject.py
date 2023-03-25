import pygame
import numpy as np
from ..imageDict import imageDict

class gameObject:
    def __init__(self, position : np.array = np.array([0,0]),
                 imageDict : imageDict = None,
                 texture : str = None) -> None:
        self.position = position
        self.imageDict = imageDict
        self.texture = texture
    def render(self, screen, offset = np.array([0,0])):
        if self.imageDict:
            image = self.imageDict.get_image(self.texture)
            if image != None:
                screen.blit(image,self.position - offset - np.floor_divide(self.imageDict.get_image_dimensions(self.texture),2))