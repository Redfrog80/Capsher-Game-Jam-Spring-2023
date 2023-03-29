from .GameObject import GameObject;
from ..misc import *;
from pygame import mouse;
from math import *;

class Gun(GameObject):
    def __init__(self, name: str = "", pos: tuple = ..., size: tuple = ..., img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, size, img);

    def update(self, dt: float):

        angle = atan(subTuple(self.pos, mouse.get_pos())[0]/ subTuple(self.pos, mouse.get_pos())[1]) * 180 / pi;
        #make angle positive, make rotaton <360
        if angle < 0:
            angle += 360;
        simpRot = self.rot%360;

        if abs(simpRot - angle) < 3.2 :
            #if the angle of the mouse is close enough to the angle of the gun
            self.rot = angle;
            self.rotv = 0;
        
        else:
            self.rotv = 3;
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))
        self.rot += self.rotv;
        
        

