from pygame import image, surface, transform
from lib.ImageDict import imageDict
from lib.misc import floorDivTuple, floorElementDiv
from lib.objects import Camera, GameObject

class gameWorld:
    def __init__(self, dimensions : tuple, tiledim : tuple, camera : Camera) -> None:
        self.__dim__ = dimensions # two tuples, top left cord, bottom right cord
        self.__tiles__ = tiledim
        self.__camera__ = camera
        self.__game_objects__ = {}
        self.tileMap = {} 
    
    
    def __update_tile_map__(self):
        for key in self.__game_objects__:
            for tup in [floorElementDiv(i,self.tileMap) for i in self.__game_objects__[key].get_boundary_corners()]:
                self.tileMap[tup] = key
    
    def add_game_objects(self, key : str, object : GameObject):
        self.__game_objects__[key] = object
    
    # args will be functions which we want to apply to every object, but we don't want in our object classes
    def update(self, dt : float, *args):
        for key in self.__game_objects__:
            obj = self.__game_objects__[key]
            obj.update(dt)
            for fun in args:
                fun(key = key, object = obj)
        # need to ensure the camera is not looking outside playable area (so things don't seem to pop into existance)
        # check for collisions
        # perform collisions
    def render(self, screen : surface, *args):
        for key in self.__game_objects__:
            obj = self.__game_objects__[key]
            obj.render(screen, self.__camera__)
            for fun in args:
                fun(key = key, object = obj)
