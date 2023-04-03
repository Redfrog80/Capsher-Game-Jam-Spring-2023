import math
from lib.misc import *
from lib.objects import *
from pygame import surface, transform
from .EnemyGun import EnemyGun


class Sentinel(Enemy):
    def __init__(self, name: str = "", pos: tuple = ..., size: tuple = ..., img: str = "resources/images/enemy3.png"):
        super().__init__(name, pos, size, img)
        self.bulletCount = 0
        self.att_range = 0
        self.cooldown = 0
        self.cooldowntimer = 0
        self.dmg = 0
        self.bulletLife = 4
        self.bulletVel = 250
        self.set_weapon_control()
        # post process so I don't have to call this from main
        self.setTextureSize((64, 64))
        self.setStat(0, 0, 200, 200, 10, 10, 1000)
        self.follow_config(None, 800, 1, 400)

    def set_weapon_control(self, dmg=5, att_r=500, cooldowntimer=.2):
        self.dmg = dmg
        self.att_range = att_r
        self.cooldowntimer = cooldowntimer

    def shoot(self, dt, aim: tuple, name: str):
        bullet_size = (10, 10)
        bullet = Projectile(name, self.dmg, self.bulletLife, size=bullet_size, img="resources/images/bullet1.png")
        bullet.setTextureSize((40, 40))
        bullet.traj(self.pos, self.vel, self.bulletVel, math.degrees(math.atan2(*aim)), 1)
        self.cooldown = self.cooldowntimer
        return bullet

    def update(self, dt: float, **kwargs):
        if self.target:
            self.trackTarget(dt)
            shootvec = subTuple(self.pos, self.target.pos)
            if magnitude(shootvec) < self.att_range and self.cooldown <= 0:
                bullet = self.shoot(dt, shootvec, self.name + "b_" + str(self.bulletCount))
                self.bulletCount += 1
                return [("enemy_bullet", bullet)]
            elif self.cooldown > 0:
                self.cooldown -= dt
