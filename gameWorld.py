import pygame
from lib.ImageDict import imageDict
from .lib.objects.GameObject import gameObject

class gameWorld:
    def __init__(self, dimensions : tuple, tiledim : tuple, camera) -> None:
        self.__dim__ = dimensions # top left corner is (0,0), bottom left is dimensions 
        self.__tiles__ = tiledim
        self.__camera__ = camera
        self.__game_objects__ = {}
        self.tileMap = {} # TODO FOR COLLISIONS
    
    def add_static_object(self, key, object):
        self.__static_objects__[key] = object
    
    def add_phys_object(self, key, object):
        self.__game_objects__[key] = object
    
    def update(self,dt):
        for key in self.__game_objects__:
            obj = self.__game_objects__[key]
            obj.update(dt, self.__dim__, np.floor_divide(obj.imageDict.get_image_dimensions(obj.texture),2), doWrap)
        # need to ensure the camera is not looking outside playable area (so things don't seem to pop into existance)
        # check for collisions
        # perform collisions
    def render(self,screen):
        for key in self.__game_objects__:
            obj = self.__game_objects__[key]
            obj.render(screen, self.__camera__)
