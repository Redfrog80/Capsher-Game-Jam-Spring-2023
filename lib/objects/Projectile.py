
from ..misc import *
from .GameObject import GameObject

from pygame import image, surface, transform

import math

class Projectile(GameObject):
    def __init__(self, **kwargs):
        
        kwargs["texture_name"] = kwargs.get("texture_name") or "bullet1"
        
        super().__init__(**kwargs)
        
        self.damage = kwargs.get("damage") or 10
        self.velocity = kwargs.get("velocity") or 200
        self.life = kwargs.get("life") or 10
        self.total_life = self.life

    def traj(self, pos: tuple, gun_velocity: tuple, speed: float, rot: float, speed_amp: float):
        self.rot = rot
        self.set_pos(pos)
        self.vel = element_add(gun_velocity, 
                               (-speed * math.sin(math.radians(self.rot)) * speed_amp,
                                -speed * math.cos(math.radians(self.rot)) * speed_amp))

    def collisionEffect(self, world, dt, obj):
        if obj.tag == PLAYER_TAG and self.tag == ENEMY_PROJECTILE_TAG:
            self.spawn_particles_on_pos(world,10,(7,7),100,1,1)
        elif obj.tag == ENEMY_TAG and self.tag == PLAYER_PROJECTILE_TAG:
            self.spawn_particles_on_pos(world,10,(7,7),100,1,1)

    def update(self, dt: float, **kwargs):
        self.set_pos(element_add(self.pos, scalar_mul(self.vel, dt)))
        self.vel = element_add(self.vel, scalar_mul(self.acc, dt))

        self.life -= dt
        if self.life < 0:
            self.destroy()

    def render(self, world):
        if self.collide_box(world.camera):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            img1 = transform.scale_by(img0, abs(self.life / self.total_life))
            dummy = scalar_div(img1.get_size(), 2)
            world.screen.blit(img1, element_sub(element_sub(self.pos, world.camera.topLeft), dummy))
