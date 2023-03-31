from pygame import image, surface, transform
#from lib.ImageDict import imageDict
#from lib.misc import floorDivTuple, floorElementDiv
#from lib.objects import Camera, GameObject


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from lib.objects import *;
        #from lib.objects import Camera;
        from lib.misc import*;
        from lib.ImageDict import *;
        #from lib.imageDict import *
    else:
        from ..lib.objects import *
        from ..lib.misc import *;
        from ..lib.ImageDict import *;
        #from ..lib.objects import Camera;
        #from ..lib.imageDict import *

class gameWorld:
    def __init__(self, dimensions : tuple, tiledim : tuple, camera : Camera) -> None:
        self.__dim__ = dimensions # top left corner is (0,0), bottom left is dimensions 
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
    
    def update(self, dt : float):
        for key in self.__game_objects__:
            obj = self.__game_objects__[key]
            obj.update(dt)
        # need to ensure the camera is not looking outside playable area (so things don't seem to pop into existance)
        # check for collisions
        # perform collisions
    def render(self, screen : surface):
        for key in self.__game_objects__:
            obj = self.__game_objects__[key]
            obj.render(screen, self.__camera__)
