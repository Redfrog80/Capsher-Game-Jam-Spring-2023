from lib.objects import *
from ..misc import *
from math import *
from pygame import surface, transform, draw


class EnemyGun(GameObject):
    def __init__(self, name: str = "", pos: tuple = ..., size: tuple = ...,
                 img: str = "resources/images/notfound.png"):
        super().__init__(name=name, pos=pos, size=size, img=img)

        self.target = None

        self.bulletVel = 200
        self.bulletLife = 4

        self.damage = 15

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

        Tpos = self.target.pos

        # mouse angle calculations
        angle = degrees(atan2(*subTuple(self.pos, Tpos)))
        # mouse angle
        if angle < 0:
            angle += 360
        # gun angle
        gsimpRot = self.rot % 360
        if abs(gsimpRot - angle) < 1:
            self.rot = angle
            self.rotvel = 0
        else:
            if -180 < angle - gsimpRot < 0 or 180 < angle - gsimpRot < 360:
                self.rotvel = -90
            else:
                self.rotvel = 90

        self.rot += self.rotvel * dt

    def shoot(self, dt, name: str):
        """
        :param name: bullet name, for looking up in dictionary
        """
        self.cooldown -= dt
        if self.cooldown < 0:
            bullet_size = (10, 10)
            bullet = Projectile(name, self.damage, self.bulletLife, size=bullet_size,
                                img="resources/images/bullet1.png")
            bullet.setTextureSize((40, 40))
            bullet.traj(self.pos, self.follow.vel, self.bulletVel, self.rot, 1.5)
            self.cooldown = self.firerate
            print(self.cooldown)
            return bullet
        return None


    def render(self, screen: surface, cam: Camera):
        if self.checkCollision(cam):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = divTuple(subTuple(img0.get_size(), self.boundary.size), 2)
            screen.blit(img0, subTuple(subTuple(self.boundary.topleft, cam.boundary.topleft), dummy))
            aimPoint = (-600 * sin(self.rot * (
                    pi / 180)), -600 * cos(self.rot * (pi / 180)))
            offset = subTuple(self.pos, cam.boundary.topleft)

