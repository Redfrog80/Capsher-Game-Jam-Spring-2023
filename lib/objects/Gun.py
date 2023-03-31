from .GameObject import GameObject;
from ..misc import *;
from pygame import mouse;
from math import *;
from pygame import surface, transform, draw;
from .Camera import Camera;

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
            #print(mangle);
        except:
            
            if subTuple(self.campos, mouse.get_pos())[0] > 0:
                #print("poo");
                mangle = 90;
            if subTuple(self.campos, mouse.get_pos())[0] < 0:
                mangle = -90;
            #else:
                #mangle = 0;
            #print(subTuple(self.campos, mouse.get_pos())[0], mangle);
        #make angle positive, make rotaton <360 for gun

        #mouse angle
        if mangle < 0:
            mangle += 180;
        #print(mangle, "pt 2");
        #gun angle
        gsimpRot = self.rot%360;

        if mouse.get_pos()[0] > self.campos[0]:
            mangle += 180;
        
        if mouse.get_pos()[1] > self.campos[1] and mangle == 0:
            mangle += 180;
        #print(mangle);
        #print(mangle, gsimpRot);
        if abs(gsimpRot - mangle) < 4.1 :
            #if the angle of the mouse is close enough to the angle of the gun
            self.rot = mangle;
            self.rotv = 0;
        
        elif mangle-gsimpRot > 0:
            if abs(mangle-gsimpRot) > 180:
                self.rotv = -4;
            else:
                self.rotv = 4;
        else:
            if abs(mangle-gsimpRot) > 180:
                self.rotv = 4;
            else:
                self.rotv = -4;
        
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))
        self.rot += self.rotv;
        
    def render(self, screen: surface, cam: Camera):

        aimPoint = (-600*sin(self.rot * (pi/180)), -600*cos(self.rot * (pi/180)));
        draw.line(screen, (0, 255, 150), self.campos, mouse.get_pos());
        draw.line(screen, (255, 0, 0), self.campos, addTuple(self.campos, aimPoint));

        if self.checkCollision(cam):  # render when object collide with camera view
            #if self.rot == 0:
                #screen.blit(self.texture, subTuple(self.boundary.topleft, cam.boundary.topleft))
            #else:
                img0 = transform.rotate(self.texture, self.rot)
                dummy = divTuple(subTuple(img0.get_size(), self.boundary.size), 2)
                screen.blit(img0, subTuple(subTuple(self.boundary.topleft, cam.boundary.topleft), dummy))


