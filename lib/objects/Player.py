from .ProjectTile import Projectile
from .Playable import Playable
from .Enemy import Enemy
import math
from lib.misc import *
from .Gun import Gun
from .Camera import Camera
from pygame import surface, transform


class Player(Playable):
    """
    Player Class. Support control, power up, etc.
    """

    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0), win_size=(0, 0), cam: Camera = None,
                 img: str = "resources/images/player1.png"):
        super().__init__(name=name, pos=pos, size=size, img=img)
        self.trackRot = False
        self.gun = Gun("gun", (0, 0), (64, 64), win_size, "resources/images/aiming.png")
        # self.gun.matchTextureToBoundary()
        self.gun.setTextureSize((128, 128))
        self.gun.trackCenter(self)
        self.cam = cam
        self.damp_factor = 1

    def rotateLeft(self):
        self.rotvel = self.rotSpeedMax

    def rotateRight(self):
        self.rotvel = -self.rotSpeedMax

    def goForward(self):
        self.acc = (-self.acc_lin * math.sin(self.rot * math.pi / 180),
                    -self.acc_lin * math.cos(self.rot * math.pi / 180))

    def goBack(self):
        self.acc = (
        self.acc_lin * math.sin(self.rot * math.pi / 180), self.acc_lin * math.cos(self.rot * math.pi / 180))

    def rotateLeftStop(self):
        self.rotvel = 0

    def rotateRightStop(self):
        self.rotvel = 0

    def goForwardStop(self):
        self.acc = (0, 0)

    def goBackStop(self):
        self.acc = (0, 0)

    def setAccel(self, ac):
        self.acc = ac

    def shoot(self, dt, name):
        return self.gun.shoot(dt, name)

    def destroy(self):
        self.liveflag = 0
        self.gun.destroy()

    def collisionEffect(self, dt, obj):
        if isinstance(obj, Projectile) and obj.tag == "enemy_bullet":
            self.gotHit(obj.dmg)
            obj.destroy()
        elif isinstance(obj, Enemy):
            self.gotHit(obj.coll_dmg)
            Playable.collisionEffect(self, dt, obj)
            if obj.sucide:
                obj.destroy()

    def render(self, screen: surface, cam: Camera):
        if self.checkCollision(cam):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = divTuple(subTuple(img0.get_size(), self.boundary.size), 2)
            screen.blit(img0, subTuple(subTuple(self.boundary.topleft, cam.boundary.topleft), dummy))
            self.gun.render(screen, cam)

    def update(self, dt: float, **kwargs):
        if self.trackRot and self.acc != (0, 0):
            self.acc = (-self.acc_lin * math.sin(self.rot * math.pi / 180),
                        -self.acc_lin * math.cos(self.rot * math.pi / 180))
        elif self.acc == (0, 0):
            self.vel = mulTuple(self.vel, math.exp(-self.damp_factor * dt))
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()

        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))

        self.vel = (capRange(self.vel[0], -self.speedMax, self.speedMax),
                    capRange(self.vel[1], -self.speedMax, self.speedMax))
        self.rot += self.rotvel * dt
        # update gun
        self.gun.update(dt, **kwargs)
