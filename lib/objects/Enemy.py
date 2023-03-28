from .Playable import Playable
from lib.misc import *
import math


class Enemy(Playable):
    """
    Generic Enemy Class. Will need simple weapon and AI class
    """
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, size, img)



    def update(self, dt: float):
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))
        # rotation
        self.rot += self.rotvel * dt
        self.vel = (-self.speed*math.sin(math.radians(self.rot)), -self.speed*math.cos(math.radians(self.rot)))

