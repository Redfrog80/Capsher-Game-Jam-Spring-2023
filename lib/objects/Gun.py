from .GameObject import GameObject
from ..misc import *
from pygame import mouse
from math import *
from pygame import surface, transform, draw
from .Camera import Camera
from .ProjectTile import Projectile


class Gun(GameObject):
    def __init__(self, name: str = "", pos: tuple = ..., size: tuple = ..., win_zise: tuple = ...,
                 img: str = "resources/images/notfound.png"):
        super().__init__(name=name, pos=pos, size=size, img=img)
        self.campos = divTuple(win_zise, 2)
        self.mouse = (0, 0)
        self.bulletSpeed = 200
        self.tracking = None        
        self.follow = None

    # Use this to attach the gun to something
    def trackCenter(self, other_object):
        self.follow = other_object

    def update(self, dt: float):
        # Sets the center position to the object it is attached to
        if self.follow is not None:
            self.pos = addTuple(self.pos, subTuple(self.follow.boundary.center, self.boundary.center))
            self.boundCenterToPos()
        
        #mouse angle calculations
        mangle = 0;
        #print(mouse.get_pos(), self.pos);
        try:
            
            mangle = atan(subTuple(self.campos, mouse.get_pos())[0]/ subTuple(self.campos, mouse.get_pos())[1]) * (180 / pi);
            #print(mangle);
        except:
            
            if subTuple(self.campos, mouse.get_pos())[0] > 0:
                mangle = 90;
            if subTuple(self.campos, mouse.get_pos())[0] < 0:
                mangle = -90;
            #else:
                #mangle = 0;
            #print(subTuple(self.campos, mouse.get_pos())[0], mangle);
        #make angle positive, make rotaton <360 for gun

        #mouse angle
    def track(self, obj: GameObject):
        self.tracking = obj

    def shoot(self, name: str):
        """
        :param name: bullet name, for looking up in dictionary
        """
        bullet = Projectile(name, "bulletEnemy", 20, img="resources/images/bullet2.png")
        bullet.setTextureSize((30, 30))
        bullet.traj(self.pos, self.bulletSpeed, self.rot, 1.2)
        return bullet

    def update(self, dt: float, **kwargs):
        if self.tracking:
            self.pos = self.tracking.pos
        if "mousepos" in kwargs:
            self.mouse = kwargs["mousepos"]
        # mouse angle calculations
        mangle = degrees(atan2(*subTuple(self.campos, self.mouse)))
        # mouse angle
        if mangle < 0:
            mangle += 360
        # gun angle
        gsimpRot = self.rot % 360
        if abs(gsimpRot - mangle) < 1:
            self.rot = mangle
            self.rotvel = 0
        else:
            if -180 < mangle - gsimpRot < 0 or 180 < mangle - gsimpRot < 360:
                self.rotvel = -180
            else:
                self.rotvel = 180

        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))
        self.rot += self.rotvel * dt

    def render(self, screen: surface, cam: Camera):
        if self.checkCollision(cam):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = divTuple(subTuple(img0.get_size(), self.boundary.size), 2)
            screen.blit(img0, subTuple(subTuple(self.boundary.topleft, cam.boundary.topleft), dummy))
            aimPoint = (-600 * sin(self.rot * (pi / 180)), -600 * cos(self.rot * (pi / 180)))
            draw.line(screen, (0, 255, 150), self.campos, mouse.get_pos())
            draw.line(screen, (255, 0, 0), self.campos, addTuple(self.campos, aimPoint))
