import math
from .defaultWeapon import weapon

from pygame import  transform
from lib.misc import *

from lib.objects.GameObject import GameObject
from lib.objects.Projectile import Projectile

class turret(GameObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.parent = kwargs.get("parent") or None
        self.weapon = kwargs.get("weapon") or weapon(turret = self)
        
        self.target_rot = None
        self.min_rot_vel = kwargs.get("min_rot_vel") or None
        self.max_rot_vel = kwargs.get("max_rot_vel") or None
    
    # Use this to attach the gun to something
    def attach_parent(self, other_object):
        self.parent = other_object
    
    def attach_weapon(self, weapon : weapon):
        self.weapon = weapon
        self.weapon.turret = self
    
    def set_rotation_behavior(self, min_rot_vel, max_rot_vel):
        self.min_rot_vel = min_rot_vel
        self.max_rot_vel = max_rot_vel
    
    def collisionEffect(self, *args, **kwargs):
        pass

    def update(self, dt, **kwargs):
        self.target_rot = self.target_rot or self.parent.rot

        if self.parent is not None:
            self.set_pos(self.parent.pos)
            self.vel = self.parent.vel
        
            if (self.min_rot_vel and self.max_rot_vel):
                difference = self.target_rot - self.rot
                while (abs(difference) > 180):
                    difference -= 360*sign(difference) 
                if (abs(difference) > self.min_rot_vel*dt):
                    self.rot += (self.parent.rotvel + sign(difference)*lerp(self.min_rot_vel, self.max_rot_vel, abs(difference)/180))*dt
            else:
                self.rot = self.parent.rot

    def fire(self, dt, **kwargs):
        self.weapon.fire(dt, world = self.world, **kwargs)
        
    def get_range(self):
        return self.weapon.get_range()

    def render(self):
        if self.collide_box(self.world.camera):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = scalar_div(img0.get_size(), 2)
            self.world.screen.blit(img0, element_sub(element_sub(self.pos, self.world.camera.topLeft), dummy))