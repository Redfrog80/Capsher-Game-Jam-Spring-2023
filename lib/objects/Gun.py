from .GameObject import GameObject;
from ..misc import *;
from pygame import mouse;
from math import *;

class Gun(GameObject):
    def __init__(self, name: str = "", pos: tuple = ..., size: tuple = ..., campos: tuple = ..., img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, size, img);
        self.campos = divTuple(campos, 2);

    def update(self, dt: float):

        #mouse angle calculations
        mangle = 0;
        #print(mouse.get_pos(), self.pos);
        try:
            mangle = atan(subTuple(self.campos, mouse.get_pos())[0]/ subTuple(self.campos, mouse.get_pos())[1]) * (180 / pi);
        except:
            if subTuple(self.campos, mouse.get_pos())[0] > 0:
                mangle = 180;
            if subTuple(self.campos, mouse.get_pos())[0] < 0:
                mangle = -180;
            else:
                mangle = 0;
        #make angle positive, make rotaton <360 for gun

        #mouse angle
        if mangle < 0:
            mangle += 180;
        
        #gun angle
        gsimpRot = self.rot%360;

        if mouse.get_pos()[0] > self.campos[0]:
            mangle += 180;
        # print(mangle);

        if abs(gsimpRot - mangle) < 2.1 :
            #if the angle of the mouse is close enough to the angle of the gun
            self.rot = mangle;
            self.rotv = 0;
        
        elif mangle-gsimpRot > 0:
            if abs(mangle-gsimpRot) > 180:
                self.rotv = -2;
            else:
                self.rotv = 2;
        else:
            if abs(mangle-gsimpRot) > 180:
                self.rotv = 2;
            else:
                self.rotv = -2;
        
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))
        self.rot += self.rotv;
        
        

