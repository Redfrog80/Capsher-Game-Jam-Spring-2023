import math
from lib.misc import *
from lib.hulls.defaultHull import hull

from lib.objects import *


class Juggernaut(Enemy):
    def __init__(self, **kwargs):
        
        kwargs["name"] = kwargs.get("name") or "Juggernaut"
        kwargs["tag"] = kwargs.get("tag") or ENEMY_TAG
        kwargs["texture_size"] = kwargs.get("texture_size") or (128,128)
        kwargs["texture_name"] = kwargs.get("texture_name") or "Emperor1"
        
        enemy_hull = hull(200, 0.005, 0.1)
        
        super().__init__(hull=enemy_hull, **kwargs)

        self.att_range = 0
        self.cooldown = 0
        self.cooldowntimer = 0
        self.projectile_damage = 0
        self.bulletLife = 6
        self.bulletVel = 200
        self.set_weapon_control()
        # post process so I don't have to call this from main
        self.setStat(0, 100, 50, 0, 50, 100, 10)
        self.follow_config(None, 1200, 1, 200)

    def set_weapon_control(self, damage=20, att_r=500, cooldowntimer=5):
        self.projectile_damage = damage
        self.att_range = att_r
        self.cooldowntimer = cooldowntimer

    def shoot(self, dt, aim: tuple, name: str, modified_angle=0):
        bullet_size = (40, 40)
        bullet = Projectile(name = name,
                            tag = ENEMY_PROJECTILE_TAG,
                            damage = self.projectile_damage,
                            life = self.bulletLife,
                            texture_size = bullet_size,
                            texture_name = "bullet5",
                            image_dict = self.image_dict,
                            sound_dict = self.sound_dict)
        bullet.traj(self.pos, self.vel, self.bulletVel, math.degrees(math.atan2(*aim))+modified_angle, 1)
        self.world.__addlist__.append(bullet)
        self.cooldown = self.cooldowntimer
        
    def update(self, dt: float, **kwargs):
        super().update(dt, **kwargs)
        if self.target:
            self.trackTarget(dt)
            shootvec = element_sub(self.pos, self.target.pos)
            if magnitude(shootvec) < self.att_range and self.cooldown <= 0:
                self.shoot(dt, shootvec, self.name + "_1", -5)
                self.shoot(dt, shootvec, self.name + "_2", 0)
                self.shoot(dt, shootvec, self.name + "_3", 5)

            elif self.cooldown > 0:
                self.cooldown -= dt
