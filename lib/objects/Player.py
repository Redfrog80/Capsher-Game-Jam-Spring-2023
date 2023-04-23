
from lib.misc import *
from .Camera import Camera
from .Gun import Gun
from .Projectile import Projectile
from .Playable import Playable
# from .Enemy import Enemy

from pygame import image, surface, transform
import math

class Player(Playable):
    """
    Player Class. Support control, power up, etc.
    """

    def __init__(self, **kwargs):
        
        kwargs["name"] = kwargs.get("name") or "player"
        kwargs["tag"] = kwargs.get("name") or PLAYER_TAG
        kwargs["texture_name"] = kwargs.get("texture_name") or "player1"
        kwargs["texture_size"] = kwargs.get("texture_size") or (64,64)
                
        super().__init__(**kwargs)
        
        self.gun = Gun(name="gun",tag="gun", texture_size = self.texture_size, texture_name="aiming")
        self.gun.trackCenter(self)
        self.trackRot = False
        self.damp_factor = 1

    def rotateLeft(self):
        self.rotvel = self.rotSpeedMax

    def rotateRight(self):
        self.rotvel = -self.rotSpeedMax

    def goForward(self):
        self.acc = (-self.acc_lin * math.sin(self.rot * math.pi / 180),
                    -self.acc_lin * math.cos(self.rot * math.pi / 180))

    def goBack(self):
        self.acc = (
        self.acc_lin * math.sin(self.rot * math.pi / 180), self.acc_lin * math.cos(self.rot * math.pi / 180))

    def rotateLeftStop(self):
        self.rotvel = 0

    def rotateRightStop(self):
        self.rotvel = 0

    def goForwardStop(self):
        self.acc = (0, 0)

    def goBackStop(self):
        self.acc = (0, 0)

    def setAccel(self, ac):
        self.acc = ac

    def shoot(self, dt, name, tag):
        return self.gun.shoot(dt, name, tag)

    def destroy(self):
        self.liveflag = 0
        self.gun.destroy()

    def collisionEffect(self, world,  dt, obj):
        if obj.tag == ENEMY_PROJECTILE_TAG:
            self.gotHit(obj.damage)
            obj.destroy()
        elif obj.tag == ENEMY_TAG:
            self.gotHit(obj.coll_damage)
            Playable.collisionEffect(self,world, dt, obj)
            if obj.suicide:
                obj.destroy()
        else:
            return
        
        if self.liveflag:
            self.spawn_particles_on_pos(world,10,(5,5),200,5,1)
        else:
            self.spawn_particles_on_pos(world,100,(7,7),300,20,1)

    def render(self, world):
        if self.collide_box(world.camera):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = scalar_div(img0.get_size(),2)
            world.screen.blit(img0, element_sub(element_sub(self.pos, world.camera.topLeft),dummy))
            self.gun.render(world)

    def update(self, **kwargs):
        dt = kwargs.get("dt") or 0
        
        if self.trackRot and self.acc != (0, 0):
            self.acc = (-self.acc_lin * math.sin(self.rot * math.pi / 180),
                        -self.acc_lin * math.cos(self.rot * math.pi / 180))
        elif self.acc == (0, 0):
            self.vel = scalar_mul(self.vel, math.exp(-self.damp_factor * dt))
        self.set_pos(element_add(self.pos, scalar_mul(self.vel, dt)))

        self.vel = element_add(self.vel, scalar_mul(self.acc, dt))

        self.vel = (capRange(self.vel[0], -self.speedMax, self.speedMax),
                    capRange(self.vel[1], -self.speedMax, self.speedMax))
        self.rot += self.rotvel * dt
        # update gun
        self.gun.update(**kwargs)
