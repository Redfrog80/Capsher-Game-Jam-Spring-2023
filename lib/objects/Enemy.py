from .Playable import Playable
from .ProjectTile import Projectile
from lib.misc import *
import math


class Enemy(Playable):
    """
    Generic Enemy Class. Will need simple weapon and AI class
    """
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, size, img)

    def collisionEffect(self, others: dict):
        for k in others:
            if isinstance(others[k], Projectile) and others[k].tag == "bulletEnemy" and self.checkCollision(others[k]):
                self.gotHit(others[k])

    def gotHit(self, bullet: Projectile):
        self.damage(bullet.dmg)
        bullet.destroy()
        if self.isDead():
            self.destroy()

    def update(self, dt: float, **kwargs):
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))

        if "gameobjs" in kwargs:
            self.collisionEffect(kwargs["gameobjs"])
