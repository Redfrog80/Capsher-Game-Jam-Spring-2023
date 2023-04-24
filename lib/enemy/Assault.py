import math
from lib.misc import *
from lib.hulls.defaultHull import hull

from lib.objects import *


class Assault(Enemy):
    def __init__(self, **kwargs):
        
        kwargs["name"] = kwargs.get("name") or "Assault"
        kwargs["tag"] = kwargs.get("tag") or ENEMY_TAG
        kwargs["texture_size"] = kwargs.get("texture_size") or (64,64)
        kwargs["texture_name"] = kwargs.get("texture_name") or "enemy2"
        
        enemy_hull = hull(50, 0.02, 0.005)
        
        super().__init__(hull=enemy_hull, **kwargs)

        self.att_range = 0
        self.cooldown = 0
        self.cooldowntimer = 0
        self.projectile_damage = 0
        self.bulletLife = 4
        self.bulletVel = 300
        self.set_weapon_control()
        # post process so I don't have to call this from main
        self.setStat(0, 0, 50, 50, 100, 150, 20)
        self.follow_config(None, 1000, 1, 200)

    def set_weapon_control(self, damage=10, att_r=600, cooldowntimer=2):
        self.projectile_damage = damage
        self.att_range = att_r
        self.cooldowntimer = cooldowntimer

    def shoot(self, dt, aim: tuple, name: str):
        bullet_size = (35,35)
        bullet = Projectile(name = name,
                            tag = ENEMY_PROJECTILE_TAG,
                            damage = self.projectile_damage,
                            life = self.bulletLife,
                            texture_size=bullet_size,
                            texture_name="bullet6",
                            image_dict = self.image_dict)
        bullet.traj(self.pos, self.vel, self.bulletVel, math.degrees(math.atan2(*aim)), 1)
        self.cooldown = self.cooldowntimer
        return bullet

    def update(self, dt: float, **kwargs):
        if self.target:
            self.trackTarget(dt)
            shootvec = element_sub(self.pos, self.target.pos)
            if magnitude(shootvec) < self.att_range and self.cooldown <= 0:
                bullet = self.shoot(dt, shootvec, self.name)
                return [bullet]
            elif self.cooldown > 0:
                self.cooldown -= dt
