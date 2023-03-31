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
        self.max_follow_distance = 0
        self.damp_factor = 0
        self.hover_distance = 0
        self.target = None

    def follow_config(self, target, max_dist, damp_fac, hover_dist):
        self.target = target
        self.max_follow_distance = max_dist
        self.damp_factor = damp_fac
        self.hover_distance = hover_dist

    def collisionEffect(self, others: dict):
        for k in others:
            if isinstance(others[k], Projectile) and others[k].tag == "bulletEnemy" and self.checkCollision(others[k]):
                self.gotHit(others[k])

    def gotHit(self, bullet: Projectile):
        self.damage(bullet.dmg)
        bullet.destroy()
        if self.isDead():
            self.destroy()

    def trackTarget(self, dt):
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()

        if bool(self.target):
            x, y = self.target.pos
            dx = x - self.pos[0]
            dy = y - self.pos[1]
            length = math.sqrt(dx ** 2 + dy ** 2)
            self.rot = math.degrees(math.atan2(dy, dx)) - 90
            speedAdd = 0
            if self.hover_distance < length < self.max_follow_distance:
                # move to player
                speedAdd = self.acc_lin * dt
            elif self.hover_distance > length:
                # move away
                speedAdd = -self.acc_lin * dt
            else:
                # damp speed
                self.vel = mulTuple(self.vel, math.exp(- self.damp_factor * dt))
            self.vel = addTuple(self.vel, (-speedAdd * math.sin(math.radians(self.rot)), speedAdd *
                                           math.cos(math.radians(self.rot))))
            self.vel = (capRange(self.vel[0], -self.speedMax, self.speedMax),
                        capRange(self.vel[1], -self.speedMax, self.speedMax))

    def update(self, dt: float, **kwargs):
        if self.target:
            self.trackTarget(dt)

        if "gameobjs" in kwargs:
            self.collisionEffect(kwargs["gameobjs"])
