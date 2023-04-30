from .Playable import Playable
from .Projectile import Projectile
from lib.misc import *
import math


class Enemy(Playable):
    """
    Generic Enemy Class. Will need simple weapon and AI class
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.max_follow_distance = 0
        self.damp_factor = 0
        self.hover_distance = 0
        self.target = None
        
        self.coll_damage = 10
        self.suicide = False

    def follow_config(self, target, max_dist, damp_fac, hover_dist):
        self.target = target
        self.max_follow_distance = max_dist
        self.damp_factor = damp_fac
        self.hover_distance = hover_dist

    def setTarget(self, target):
        self.target = target

    def collisionEffect(self, dt, obj):
        if  obj.tag == PLAYER_PROJECTILE_TAG:
            self.gotHit(obj.damage)
            obj.destroy()     
        elif obj.tag not in ("gun", ENEMY_PROJECTILE_TAG):
            self.liveflag = self.liveflag and not self.suicide
            Playable.collisionEffect(self, dt, obj)
        elif obj.tag == ENEMY_PROJECTILE_TAG:
            return
        
        if self.liveflag:
            if obj.tag != ENEMY_TAG:
                self.spawn_particles_on_pos(5,(5,5),200,3,1.1)
        else:
            self.spawn_particles_on_pos(5,(13,13),100,3,2)

    def gotHit(self, damage):
        self.damage(damage)
        if self.isDead():
            self.destroy()

    def trackTarget(self, dt):
        if bool(self.target):
            unit = unit_tuple2(self.pos, self.target.pos)
            length = self.dist(self.target)
            self.rot = math.degrees(math.atan2(*unit))
            speedAdd = 0
            if self.hover_distance < length < self.max_follow_distance:
                # move to player
                speedAdd = self.acc_lin*dt 
            elif self.hover_distance > length:
                # move away
                speedAdd = -self.acc_lin*dt 
            else:
                # damp speed
                self.vel = scalar_mul(self.vel, math.exp(-self.damp_factor * dt))
            self.vel = element_sub(self.vel, scalar_mul(unit,speedAdd))
            self.vel = (capRange(self.vel[0], -self.speedMax, self.speedMax),
                        capRange(self.vel[1], -self.speedMax, self.speedMax))

    def update(self, dt: float, **kwargs):
        super().update(dt, **kwargs)
        if self.target:
            self.trackTarget(dt)
