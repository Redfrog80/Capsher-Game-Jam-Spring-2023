from .Playable import Playable
from .ProjectTile import Projectile
import math
from lib.misc import *


class Player(Playable):
    """
    Player Class. Support control, power up, etc.
    """
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/notfound.png"):
        super().__init__(name=name, pos=pos, size=size, img=img)
        self.trackRot = False

    def rotateLeft(self):
        self.rotvel = self.rotSpeedMax

    def rotateRight(self):
        self.rotvel = -self.rotSpeedMax

    def goForward(self):
        self.acc = (-self.acc_lin * math.sin(self.rot * math.pi / 180), -self.acc_lin * math.cos(self.rot * math.pi / 180))

    def goBack(self):
        self.acc = (self.acc_lin * math.sin(self.rot * math.pi / 180), self.acc_lin * math.cos(self.rot * math.pi / 180))
    
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

    def shoot(self, name: str):
        """
        :param name: bullet name, for looking up in dictionary
        """
        bullet = Projectile(name, "bulletEnemy", 20)
        bullet.traj(self.pos, self.speedMax, self.rot, 1)
        return bullet

    def update(self, dt: float, **kwargs):
        if self.trackRot and self.acc != (0, 0):
            self.acc = (-self.acc_lin * math.sin(self.rot * math.pi / 180), -self.acc_lin * math.cos(self.rot * math.pi / 180))
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        origV = self.vel
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))

        #if too fast set to preset velocity
        # if magnitude(self.vel) > self.speedMax:
        #     self.vel = origV
        # print(self.vel)
        # self.vel = addTuple(self.vel, (1, 1))
        # rotation
        self.rot += self.rotvel * dt
        # self.vel = (-self.speed*math.sin(math.radians(self.rot)), -self.speed*math.cos(math.radians(self.rot)))
