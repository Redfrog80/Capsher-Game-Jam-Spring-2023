from pygame import surface, transform, draw
from math import *
from lib.misc import *

from lib.objects.GameObject import GameObject
from lib.objects.Projectile import Projectile

class Gun(GameObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bulletVel = 400
        self.bulletLife = 2

        self.damage = 10

        self.cooldown = 0
        self.firerate = 0.1

        self.follow = None

    # Use this to attach the gun to something
    def trackCenter(self, other_object):
        self.follow = other_object
    
    def collisionEffect(self, world, dt, object):
        pass

    def update(self, **kwargs):
        dt = kwargs.get("dt") or 0
        # Sets the center position to the object it is attached to
        if self.follow is not None:
            self.set_pos(self.follow.pos)
        self.rot = self.follow.rot

    def shoot(self, dt, name: str, tag: str):
        self.cooldown -= dt
        if self.cooldown < 0:
            bullet_size = (30,30)
            bullet = Projectile(name = name,
                                tag = tag,
                                damage = self.damage,
                                life = self.bulletLife,
                                texture_size=bullet_size,
                                texture_name = "bullet3",
                                image_dict = self.image_dict)
            bullet.traj(self.pos, self.follow.vel, self.bulletVel, self.rot, 1.5)
            self.cooldown = self.firerate
            return bullet
        return None

    def render(self, world):
        if self.collide_box(world.camera):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = scalar_div(img0.get_size(), 2)
            world.screen.blit(img0, element_sub(element_sub(self.pos, world.camera.topLeft), dummy))
            # aimPoint = (-600 * sin(self.rot * (
            #         pi / 180)), -600 * cos(self.rot * (pi / 180)))
            # offset = element_sub(self.pos, world.camera.topLeft)
            # draw.line(world.screen, (0, 255, 150), offset, self.mouse)
            # draw.line(world.screen, (255, 0, 0), offset, element_add(offset, aimPoint))
