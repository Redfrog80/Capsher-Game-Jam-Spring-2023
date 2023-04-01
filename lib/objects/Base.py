import numpy as np
from pygame.rect import Rect
from ..misc import *


class Base:
    """
    Base class for all game object
    Currently using rectangular boundary provided by pygame since it already have collider detector
    """

    def __init__(self, name: str = "", pos: tuple = (0, 0), vel: tuple = (0, 0), acc: tuple = (0, 0),
                 size: tuple = (0, 0), tag: str = "") -> None:
        self.name = name
        self.tag = tag
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.rot = 0
        self.rotvel = 0
        self.size = size
        self.boundary = Rect(pos, size)
        self.boundCenterToPos()  # update pos on generation to prevent confusion due to previous called
        self.liveflag = 1  # use in GameWorld to check if object should be destroyed (go out of bound, died, etc.)

    def boundCenterToPos(self):
        self.boundary.move_ip(subTuple(self.pos, self.boundary.center))
    
    def check_collide_direction(self, other):
        r = other.boundary
        b = self.boundary
        return (not r.top < b.top,
                not r.left < b.left,
                not r.bottom > b.bottom,
                not r.right > b.right)

    def destroy(self):
        self.liveflag = 0

    def objAlive(self):
        return bool(self.liveflag)
