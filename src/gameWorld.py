from turtle import st
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
    
    def __update_tile_map__(self):
        self.tileMap = {}
        for key in self.__game_objects__:
            boundary = self.__game_objects__[key].boundary
            topLeft, bottomRight = [floorElementDiv(i,self.__tiledim__) for i in [boundary.topleft, boundary.bottomright]]
            for tup in [(i,j) for i in range(topLeft[0],bottomRight[0]+1) for j in range(topLeft[1],bottomRight[1]+1)]:
                old = self.tileMap.get(tup,[])
                self.tileMap[tup] = [key] + old
    
    def add_game_object(self, key : str, object : GameObject):
        self.__game_objects__[key] = object
    
    def set_tracked_object(self, key):
        self.__camera__.trackCenter(self.__game_objects__[key])
    
    # args will be functions which we want to apply to every object, but we don't want in our object classes
    def update(self, dt : float, *args):
        self.__camera__.update()
        for key in self.__game_objects__:
            obj = self.__game_objects__[key]
            obj.update(dt)
            for fun in args:
                fun(self = self, dt = dt, key = key, object = obj)

        self.__update_tile_map__()
        # for key in self.tileMap:
        #     if len(self.tileMap[key]) > 1:
        #         for key_a in self.tileMap[key]:
        #             for key_b in self.tileMap[key]:
        #                 if key_a!=key_b and Rect.colliderect(self.__game_objects__[key_a].boundary, self.__game_objects__[key_b].boundary):
        #                     obj_a = self.__game_objects__[key_a]
        #                     obj_b = self.__game_objects__[key_b]
        #                     obj_a.boundCenterToPos()
        #                     obj_b.boundCenterToPos()
        #                     b_a = obj_a.boundary
        #                     b_b = obj_b.boundary
        #                     # obj_a.vel = addTuple(obj_a.vel, elementDiv(mulTuple(unitTuple(obj_a.boundary.center,obj_b.boundary.center), 1000*dt), self.__tiledim__))
        #                     if (b_a.top < b_b.bottom and not b_b.top < b_a.bottom):
        #                         v_a, v_b = obj_a.vel[1], obj_b.vel[1]
        #                         obj_a.vel = (obj_b.vel[0],v_b-v_a)
        #                         obj_b.vel = (obj_a.vel[0],v_a-v_b)

        pass
                
    def render(self, screen : surface, *args):
        for key in self.__game_objects__:
            obj = self.__game_objects__[key]
            obj.render(screen, self.__camera__)
            for fun in args:
                fun(self = self, screen = screen, key = key, object = obj)
    
    def render_tile_map(self,screen):
        for tile in self.tileMap:
            screen.fill((tile[0]*4%200+55,55,tile[1]*4%200+55), Rect(subTuple(mulElements(tile,self.__tiledim__), self.__camera__.boundary.topleft),self.__tiledim__))