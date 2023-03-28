from .Playable import Playable
import math
from lib.misc import *


class Player(Playable):
    """
    Player Class. Support control, power up, etc.
    """
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, size, img)

    def rotateLeft(self):
        self.rotvel = self.rotspeedMax

    def rotateRight(self):
        self.rotvel = -self.rotspeedMax

    def goForward(self):
        self.speed = self.speedMax

    def goBack(self):
        self.speed = -self.speedMax

    def rotateLeftStop(self):
        self.rotvel = 0

    def rotateRightStop(self):
        self.rotvel = 0

    def goForwardStop(self):
        self.speed = 0

    def goBackStop(self):
        self.speed = 0

    def update(self, dt: float):
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))
        # rotation
        self.rot += self.rotvel * dt
        self.vel = (-self.speed*math.sin(math.radians(self.rot)), -self.speed*math.cos(math.radians(self.rot)))
