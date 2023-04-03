from .GameObject import GameObject
from ..misc import *
from pygame import mouse
from math import *
from pygame import surface, transform, draw
from .Camera import Camera
from .ProjectTile import Projectile
from .Beam import Beam;


class Gun(GameObject):
    def __init__(self, name: str = "", pos: tuple = ..., size: tuple = ..., win_size: tuple = ...,
                 img: str = "resources/images/notfound.png"):
        super().__init__(name=name, pos=pos, size=size, img=img)
        self.mouse = (0, 0)
        
        self.bulletVel = 200
        self.bulletLife = 4
        self.beamLife = 1;
        
        self.damage = 40
        self.beamDmg = 300;
        self.cooldown = 0
        self.firerate = 0.1
        
        self.tracking = None        
        self.follow = None

    # Use this to attach the gun to something
    def trackCenter(self, other_object):
        self.follow = other_object

    def update(self, dt: float, **kwargs):
        # Sets the center position to the object it is attached to
        if self.follow is not None:
            self.pos = addTuple(self.pos, subTuple(self.follow.boundary.center, self.boundary.center))
            self.boundCenterToPos()
        
        if "mousepos" in kwargs:
            self.mouse = kwargs["mousepos"]
            #print(self.mouse, end="\r")
        if "camera" in kwargs:
            offset = subTuple(self.pos, kwargs["camera"].boundary.topleft)
        else:
            return
        # mouse angle calculations
        mangle = degrees(atan2(*subTuple(offset, self.mouse)))
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

        self.rot += self.rotvel * dt

    def shoot(self, dt, name: str, canLaser):
        """
        :param name: bullet name, for looking up in dictionary
        """

        if canLaser:
            #shoot da laser
            bullet_size = (80,80)
            bullet = Projectile(name, self.damage*100, self.bulletLife, size = bullet_size, img="resources/images/plasma4.png")
            bullet.setTextureSize(bullet_size)
            bullet.traj(self.pos, self.follow.vel, self.bulletVel*6, self.rot, 1.5)
            self.cooldown = self.firerate
            return bullet
        else:
            self.cooldown -= dt
            #print(self.cooldown)
            if (self.cooldown < 0):
                bullet_size = (20,20)
                bullet = Projectile(name, self.damage*5, self.bulletLife, size = bullet_size, img="resources/images/bullet2.png")
                bullet.setTextureSize(bullet_size)
                bullet.traj(self.pos, self.follow.vel, self.bulletVel, self.rot, 1.5)
                self.cooldown = self.firerate
                #print(self.cooldown)
                return bullet
            return None
        return None;


    def render(self, screen: surface, cam: Camera):
        if self.checkCollision(cam):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = divTuple(subTuple(img0.get_size(), self.boundary.size), 2)
            screen.blit(img0, subTuple(subTuple(self.boundary.topleft, cam.boundary.topleft), dummy))
            aimPoint = (-600 * sin(self.rot * (
                pi / 180)), -600 * cos(self.rot * (pi / 180)))
            offset = subTuple(self.pos, cam.boundary.topleft)
            draw.line(screen, (0, 255, 150), offset, self.mouse)
            draw.line(screen, (255, 0, 0), offset, addTuple(offset, aimPoint))
