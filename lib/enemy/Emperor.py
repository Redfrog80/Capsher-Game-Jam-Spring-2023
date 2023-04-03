import math
from lib.misc import *
from lib.objects import *


import math
from lib.misc import *
from lib.objects import *

# CURRENTLY JUST A DUPLICATE OF ASSAULT
class Emperor(Enemy):
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/amogus.png"):
        super().__init__(name, pos, size, img)
        self.bulletCount = 0
        self.att_range = 0
        self.cooldown = 0
        self.cooldowntimer = 0
        self.dmg = 0
        self.coll_dmg = 10
        self.bulletLife = 4
        self.bulletVel = 200
        self.set_weapon_control()

    def set_weapon_control(self, dmg=10, att_r=600, cooldowntimer=2):
        self.dmg = dmg
        self.att_range = att_r
        self.cooldowntimer = cooldowntimer

    def shoot(self, dt, aim: tuple, name: str):
        bullet_size = (20, 20)
        bullet = Projectile(name, self.dmg, self.bulletLife, size=bullet_size, img="resources/images/bullet6.png")
        bullet.setTextureSize(bullet_size)
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
