from lib.hulls import hull
from .GameObject import GameObject

class Playable(GameObject):
    """Generic class for both player and enemy"""
    def __init__(self, hull: hull = hull(), **kwargs):
        super().__init__(**kwargs)

        self.hull = hull
        # stat
        self.shield = 0
        self.shieldMax = 0
        self.speedMax = 0
        self.acc_lin = 0
        self.rotSpeedMax = 0

    def setStat(self, s: float, shm: float, h: float, hm: float, a: float, sm: float, rm: float):
        self.shield = s
        self.shieldMax = shm
        self.acc_lin = a
        self.speedMax = sm
        self.rotSpeedMax = rm

    def isDead(self):
        return self.hull.is_broken()

    def damage(self, value: float):
        return self.hull.damage(value)

    def gotHit(self, damage):
        if self.damage(damage):
            self.destroy()
    
    def update(self, dt, **kwargs):
        super().update(dt, **kwargs)
        self.hull.update(dt)
