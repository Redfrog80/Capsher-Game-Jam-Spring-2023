import math
from lib.misc import *
from lib.objects import *


class Juggernaut(Enemy):
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/Emperor1.png"):
        super().__init__(name, pos, size, img)
        self.bulletCount = 0
        self.att_range = 0
        self.cooldown = 0
        self.cooldowntimer = 0
        self.dmg = 0
        self.bulletLife = 3
        self.bulletVel = 200
        self.set_weapon_control()
        # post process so I don't have to call this from main
        self.setTextureSize((64, 64))
        self.setStat(0, 100, 50, 0, 50, 50, 1000)
        self.follow_config(None, 800, 1, 200)

    def set_weapon_control(self, dmg=10, att_r=300, cooldowntimer=5):
        self.dmg = dmg
        self.att_range = att_r
        self.cooldowntimer = cooldowntimer

    def shoot(self, dt, aim: tuple, name: str, modified_angle=0):
        bullet_size = (10, 10)
        bullet = Projectile(name, self.dmg, self.bulletLife, size=bullet_size, img="resources/images/bullet1.png")
        bullet.setTextureSize((40, 40))
        bullet.traj(self.pos, self.vel, self.bulletVel, math.degrees(math.atan2(*aim))+modified_angle, 1)
        self.cooldown = self.cooldowntimer
        return bullet

    def update(self, dt: float, **kwargs):
        if self.target:
            self.trackTarget(dt)
            shootvec = subTuple(self.pos, self.target.pos)
            if magnitude(shootvec) < self.att_range and self.cooldown <= 0:
                bullet0 = self.shoot(dt, shootvec, self.name + "b_" + str(self.bulletCount+2), -5)
                bullet1 = self.shoot(dt, shootvec, self.name + "b_" + str(self.bulletCount), 0)
                bullet2 = self.shoot(dt, shootvec, self.name + "b_" + str(self.bulletCount+1), 5)
                self.bulletCount += 3
                return [("enemy_bullet", bullet0), ("enemy_bullet", bullet1), ("enemy_bullet", bullet2)]
            elif self.cooldown > 0:
                self.cooldown -= dt
