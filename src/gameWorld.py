from pygame import surface, Rect, font
from lib.ImageDict import ImageDict
from lib.misc import *
from lib.objects import Camera, GameObject

class gameWorld:
    def __init__(self, dimensions : Rect, tiledim : tuple, camera : Camera) -> None:
        self.__dim__ = dimensions
        self.__tiledim__ = tiledim
        self.__camera__ = camera
        self.__game_objects__ = {}
        self.tileMap = {} 
        self.border_behavior = self.border_default
    
    def __update_tile_map__(self):
        self.tileMap = {}
        for key in self.__game_objects__:
            for object in self.__game_objects__[key]:
                boundary = object.boundary
                topLeft, bottomRight = [floorElementDiv(i,self.__tiledim__) for i in [boundary.topleft, boundary.bottomright]]
                for tup in [(i,j) for i in range(topLeft[0],bottomRight[0]+1) for j in range(topLeft[1],bottomRight[1]+1)]:
                    self.tileMap[tup] = [key] + self.tileMap.get(tup,[])
    
    def border_default(world, dt, key, object):
        object.boundCenterToPos()
        r = object.boundary
        b = world.__dim__
        
        if (r.top < b.top):
            object.pos = (object.pos[0], object.pos[1] + b.top - r.top)
            object.vel = (object.vel[0],-object.vel[1])
        if (r.left < b.left):
            object.pos = (object.pos[0] + b.left - r.left, object.pos[1])
            object.vel = (-object.vel[0],object.vel[1])

        if (r.bottom > b.bottom):
            object.pos = (object.pos[0], object.pos[1] + b.bottom - r.bottom)
            object.vel = (object.vel[0],-object.vel[1])
        if (r.right > b.right):
            object.pos = (object.pos[0] + b.right - r.right, object.pos[1])
            object.vel = (-object.vel[0],object.vel[1])

    
    def add_game_object(self, key : str, object : GameObject):
        self.__game_objects__[key] = [object] + self.__game_objects__.get(key,[])
    
    def set_tracked_object(self, key, name):
        for object in self.__game_objects__[key]:
            if object.name == name:
                self.__camera__.trackCenter(object)
    
    # args will be functions which we want to apply to every object, but we don't want in our object classes
    def update(self, dt : float, *args):
        self.__camera__.update()
        for key in self.__game_objects__:
            for object in self.__game_objects__[key]:
                object.update(dt)
                
                self.border_behavior(dt = dt, key = key, object = object)
                
                for fun in args:
                    fun(world = self, dt = dt, key = key, object = object)

        self.__update_tile_map__()
        # NEED Way TO GROUP COLLIDED OBJECTS WITHOUT DUPLICATES...

        pass
                
    def render(self, screen : surface, *args):
        for key in self.__game_objects__:
            for object in self.__game_objects__[key]:
                object.render(screen, self.__camera__)
            
                for fun in args:
                    fun(self = self, screen = screen, key = key, object = object)
    
    def render_tile_map(self,screen):
        for tile in self.tileMap:
            screen.fill((tile[0]*4%200+55,55,tile[1]*4%200+55), Rect(subTuple(mulElements(tile,self.__tiledim__), self.__camera__.boundary.topleft),self.__tiledim__))