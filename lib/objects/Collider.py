from math import dist
from lib.misc import *

class Collider:
    def __init__(self, **kwargs):
        
        self.pos = kwargs.get("pos") or (0,0)
        self.radius = kwargs.get("radius") or 1
        self.shape = kwargs.get("shape") or (1,1)
        self.__update__()

    def dist(self, other):
        return dist(self.pos, other.pos)
    
    def set_pos(self, pos):
        self.pos = pos
        self.__update__()
    
    def __update__(self):
        self.top = int(self.pos[1] - self.radius*self.shape[1])
        self.bottom = int(self.pos[1] + self.radius*self.shape[1])
        self.left = int(self.pos[0] - self.radius*self.shape[0])
        self.right = int(self.pos[0] + self.radius*self.shape[0])
        self.topLeft = element_int(element_add(self.pos, (-self.radius*self.shape[0],-self.radius*self.shape[1])))
        self.topRight = element_int(element_add(self.pos, (self.radius*self.shape[0],-self.radius*self.shape[1])))
        self.bottomLeft = element_int(element_add(self.pos, (-self.radius*self.shape[0],self.radius*self.shape[1])))
        self.bottomRight = element_int(element_add(self.pos, (self.radius*self.shape[0],self.radius*self.shape[1])))

    def collide_circle(self, other)->bool:
        mag = dist(self.pos, other.pos)
        dif = element_sub(self.pos, other.pos)
        if (mag):
            unit = scalar_div(dif,mag)
            a = magnitude(element_mul(scalar_mul(unit,self.radius),self.shape))
            b = magnitude(element_mul(scalar_mul(unit,other.radius),other.shape))
            return (mag <= (a+b))
        else:
            return True

    def collide_box(self, other)->bool:
        return (self.top <= other.bottom and
                self.bottom >= other.top or
                self.left <= other.right and
                self.right >= other.left)

    def collide_point(self,point: tuple):
        return (dist(self.pos, point) <= self.radius)
    
    def resolve_circle_overlap(self,other):
        mag = self.dist(other)
        dif = element_sub(self.pos, other.pos)
        if (mag):
            unit = scalar_div(dif,mag)
            a = magnitude(element_mul(scalar_mul(unit,self.radius),self.shape))
            b = magnitude(element_mul(scalar_mul(unit,other.radius),other.shape))
            self.set_pos(element_add(self.pos,scalar_mul(unit,((a+b)-mag)/2)))
            other.set_pos(element_add(other.pos,scalar_mul(unit,(-(a+b)+mag)/2)))
    
    
    def get_direction(self, other)->bool:
        mag = dist(self.pos, other.pos)
        dif = element_sub(self.pos, other.pos)
        if (mag):
            return scalar_div(dif,mag)
        else:
            return (0,0)