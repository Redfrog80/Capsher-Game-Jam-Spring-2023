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
        super().__init__(name, pos, size, img)
        self.campos = divTuple(win_zise, 2)
        self.mouse = (0, 0)
        self.bulletSpeed = 200
        self.tracking = None

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
