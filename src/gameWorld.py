from pygame import surface, Rect, font
import pygame
from lib.misc import *
from lib.objects import Camera, GameObject

class gameWorld:
    def __init__(self, dimensions : Rect, tiledim : tuple, camera : Camera) -> None:
        self.__dim__ = dimensions
        self.__tiledim__ = tiledim
        self.__camera__ = camera
        self.__camera__.set_world(self)
        self.__game_objects__ = {}
        self.__garbage__ = []
        self.tileMap = {} 
        self.border_behavior = self.border_default
    
    def __update_tile_map__(self):
        self.tileMap = {}
        for key in self.__game_objects__:
            for object_name in self.__game_objects__[key]:
                object = self.__game_objects__[key][object_name]
                boundary = object.boundary
                topLeft, bottomRight = [floorElementDiv(i,self.__tiledim__) for i in [boundary.topleft, boundary.bottomright]]
                for tup in [(i,j) for i in range(topLeft[0],bottomRight[0]+1) for j in range(topLeft[1],bottomRight[1]+1)]:
                    self.tileMap[tup] = [object] + self.tileMap.get(tup,[])
    
    def get_collided_pairs(self):
        
        pass
    
    def check_out_of_bound(self, boundary, object):
        r = object.boundary
        b = boundary
        return (r.top < b.top,
                r.left < b.left,
                r.bottom > b.bottom,
                r.right > b.right)
    
    def border_default(world, dt, key, object):
        r = object.boundary
        if key == "player_bullet":
            bb = world.__dim__.copy()
            bb.inflate_ip(r.size)
            
            bounds = world.check_out_of_bound(bb,object)
            
            if True in bounds:
                world.__garbage__.append((key,object.name))
        else:
            b = world.__dim__
            
            bounds = world.check_out_of_bound(b,object)
            
            if bounds[0]:
                object.pos = (object.pos[0], object.pos[1] + b.top - r.top)
                object.vel = (object.vel[0],-object.vel[1])
            if bounds[1]:
                object.pos = (object.pos[0] + b.left - r.left, object.pos[1])
                object.vel = (-object.vel[0],object.vel[1])
            if bounds[2]:
                object.pos = (object.pos[0], object.pos[1] + b.bottom - r.bottom)
                object.vel = (object.vel[0],-object.vel[1])
            if bounds[3]:
                object.pos = (object.pos[0] + b.right - r.right, object.pos[1])
                object.vel = (-object.vel[0],object.vel[1])
        object.boundCenterToPos()
            
    
    def add_game_object(self, key : str, object : GameObject):
        if self.__game_objects__.get(key):
            self.__game_objects__[key][object.name] = object
        else:
            self.__game_objects__[key] = {object.name : object}
    
    def set_tracked_object(self, key, name):
        for object_name in self.__game_objects__[key]:
            self.__camera__.trackCenter(self.__game_objects__[key][object_name])
    
    # args will be functions which we want to apply to every object, but we don't want in our object classes
    def update(self, dt : float, *args):
        self.__camera__.update()
        for key in self.__game_objects__:
            for object_key in self.__game_objects__[key]:
                object = self.__game_objects__[key][object_key]
                object.update(dt, mousepos = pygame.mouse.get_pos(), camera = self.__camera__)
                
                self.border_behavior(dt = dt, key = key, object = object)
                
                for fun in args:
                    fun(world = self, dt = dt, key = key, object = object)

        while (len(self.__garbage__)):
            tup = self.__garbage__.pop()
            del self.__game_objects__[tup[0]][tup[1]]

        self.__update_tile_map__()
        # NEED WAY TO GROUP COLLIDED OBJECTS WITHOUT DUPLICATES...
        # PERFORM COLLISION

        pass
                
    def render(self, screen : surface, *args):
        for key in self.__game_objects__:
            for object_key in self.__game_objects__[key]:
                object = self.__game_objects__[key][object_key]
                object.render(screen, self.__camera__)
            
                for fun in args:
                    fun(self = self, screen = screen, key = key, object = object)
    
    def render_tile_map(self,screen):
        for tile in self.tileMap:
            screen.fill((tile[0]*4%200+55,55,tile[1]*4%200+55), Rect(subTuple(mulElements(tile,self.__tiledim__), self.__camera__.boundary.topleft),self.__tiledim__))