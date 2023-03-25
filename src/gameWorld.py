import pygame
import numpy as np
from lib.imageDict import imageDict
from lib.objects.gameObject import gameObject
from lib.objects.physicsObject import physicsObject

class gameWorld:
    def __init__(self, dimensions : np.array, tiledim : np.array, camera) -> None:
        self.__dim__ = dimensions # top left corner is (0,0), bottom left is dimensions 
        self.__tiles__ = tiledim
        self.__camera__ = camera
        self.__static_objects__ = {}
        self.__phys_objects__ = {}
        self.tileMap = {} # TODO FOR COLLISIONS
    
    def add_static_object(self, key, object):
        self.__static_objects__[key] = object
    
    def add_phys_object(self, key, object):
        self.__phys_objects__[key] = object
    
    def update(self,dt, doWrap = False):
        for key in self.__phys_objects__:
            obj = self.__phys_objects__[key]
            obj.update(dt, self.__dim__, np.floor_divide(obj.imageDict.get_image_dimensions(obj.texture),2), doWrap)
        # need to ensure the camera is not looking outside playable area (so things don't seem to pop into existance)
        # check for collisions
        # perform collisions
    def render(self,screen):
        for key in self.__phys_objects__:
            obj = self.__phys_objects__[key]
            obj.render(screen, self.__camera__.position - np.floor_divide(self.__dim__,2))
        for key in self.__static_objects__:
            obj = self.__phys_objects__[key]
            obj.render(screen, self.__camera__.position - np.floor_divide(self.__dim__,2))