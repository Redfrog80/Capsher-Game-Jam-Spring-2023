from pygame import Surface, surface, Rect, font
import pygame
from lib.misc import *
from lib.objects import Camera, GameObject

class gameWorld:
    def __init__(self, dimensions : Rect, tiledim : tuple, screen: Surface, mouseArea: tuple, camera : Camera) -> None:
        self.__dim__ = dimensions
        self.__tiledim__ = tiledim
        self.__camera__ = camera
        self.__camera__.set_world(self)
        self.__game_objects__ = {}
        self.__screen__ = screen
        self.__mouse_area__ = mouseArea
        self.__garbage__ = []
        self.tileMap = {} 
        self.collided_pairs = {}
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
    
    
    def __get_collided_pairs__(self):
        self.collided_pairs = {}
        for tile in self.tileMap:
            for object in self.tileMap[tile]:
                for other_object in self.tileMap[tile]:
                    if (object != other_object and object.checkCollision(other_object)):
                        if (object.name < other_object.name):
                            self.collided_pairs[object.name + "x" + other_object.name] = [object,other_object]
        
    def __garbage_collection__(self):
        while (len(self.__garbage__)):
            obj = self.__garbage__.pop()
            if (self.__game_objects__.get(obj.tag, {}).get(obj.name)):
                del self.__game_objects__[obj.tag][obj.name]
    
    def get_scaled_mouse_pos(self):
        return mulElements(self.__screen__.get_size(), elementDiv(pygame.mouse.get_pos(),self.__mouse_area__))
    
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
                world.delete_game_object(object)
        elif key == "camera":
            b = world.__dim__
            
            bounds = world.check_out_of_bound(b,object)
            
            if bounds[0]:
                object.pos = (object.pos[0], object.pos[1] + b.top - r.top)
                object.vel = (object.vel[0],0)
            if bounds[1]:
                object.pos = (object.pos[0] + b.left - r.left, object.pos[1])
                object.vel = (0,object.vel[1])
            if bounds[2]:
                object.pos = (object.pos[0], object.pos[1] + b.bottom - r.bottom)
                object.vel = (object.vel[0],0)
            if bounds[3]:
                object.pos = (object.pos[0] + b.right - r.right, object.pos[1])
                object.vel = (0,object.vel[1])
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
        object.tag = key
        if self.__game_objects__.get(key):
            self.__game_objects__[key][object.name] = object
        else:
            self.__game_objects__[key] = {object.name : object}
    
    def delete_game_object(self, object : GameObject):
        self.__garbage__.append(object)
    
    def delete_if_dead(self,object):
        if (object and not object.liveflag):
            self.delete_game_object(object)

    def set_tracked_object(self, key, follow_distance):
        for object_name in self.__game_objects__[key]:
            self.__camera__.follow_config(self.__game_objects__[key][object_name], follow_distance)
    
    # args will be functions which we want to apply to every object, but we don't want in our object classes
    def update(self, dt : float, *args):
        self.__camera__.update(dt)
        mousePos = self.get_scaled_mouse_pos()
        
        for key in self.__game_objects__:
            for object_key in self.__game_objects__[key]:
                object = self.__game_objects__[key][object_key]
                object.update(dt, mousepos = mousePos, camera = self.__camera__)
                
                self.border_behavior(dt = dt, key = key, object = object)
                
                for fun in args:
                    fun(world = self, dt = dt, key = key, object = object)

        self.__garbage_collection__()
        self.__update_tile_map__()
        self.__get_collided_pairs__()
        
        for pair in self.collided_pairs:
            obj_a, obj_b = self.collided_pairs[pair]
            obj_a.collisionEffect(dt,obj_b)
            obj_b.collisionEffect(dt,obj_a)
            self.delete_if_dead(obj_a)
            self.delete_if_dead(obj_b)

        pass
                
    def render(self, *args):
        for key in self.__game_objects__:
            for object_key in self.__game_objects__[key]:
                object = self.__game_objects__[key][object_key]
                object.render(self.__screen__, self.__camera__)
            
                for fun in args:
                    fun(self = self, screen = self.__screen__, key = key, object = object)
    
    def render_tile_map(self):
        for tile in self.tileMap:
            self.__screen__.fill((tile[0]*4%200+55,55,tile[1]*4%200+55), Rect(subTuple(mulElements(tile,self.__tiledim__), self.__camera__.boundary.topleft),self.__tiledim__))