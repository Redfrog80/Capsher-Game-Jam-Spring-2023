from .GameObject import GameObject


class Playable(GameObject):
    """Generic class for both player and enemy"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # stat
        self.health = 0
        self.shield = 0
        self.healthMax = 0
        self.shieldMax = 0
        self.speedMax = 0
        self.acc_lin = 0
        self.rotSpeedMax = 0

    def setStat(self, s: float, shm: float, h: float, hm: float, a: float, sm: float, rm: float):
        self.shield = s
        self.health = h
        self.shieldMax = shm
        self.healthMax = hm
        self.acc_lin = a
        self.speedMax = sm
        self.rotSpeedMax = rm

    def isDead(self):
        return self.health <= 0

    def addHealth(self, value: float):
        self.health += value
        if self.health > self.healthMax:
            self.health = self.healthMax

    def addShield(self, value: float):
        self.shield += value
        if self.shield > self.shieldMax:
            self.shield = self.shieldMax

    def damage(self, value: float):
        if self.shield > 0:
            self.shield -= value
            if self.shield < 0:
                self.shield = 0
        else:
            self.health -= value

    def gotHit(self, damage):
        self.damage(damage)
        if self.isDead():
            self.destroy()
