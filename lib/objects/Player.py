
from lib.misc import *
from .Camera import Camera
from ..weapons import turret, bolter, flakker
from .Projectile import Projectile
from .Playable import Playable
# from .Enemy import Enemy

from pygame import image, surface, transform
import math

class Player(Playable):

    def __init__(self, **kwargs):
        
        kwargs["name"] = kwargs.get("name") or "player"
        kwargs["tag"] = kwargs.get("name") or PLAYER_TAG
        kwargs["texture_name"] = kwargs.get("texture_name") or "player1"
        kwargs["texture_size"] = kwargs.get("texture_size") or (64,64)
                
        super().__init__(**kwargs)
        
        weapon = flakker(projectile_tag = PLAYER_PROJECTILE_TAG,
                        projectile_texture_name = "bullet3",
                        image_dict = self.image_dict,
                        sound_dict = self.sound_dict)
        
        self.turret = turret(name = "turret",
                             tag="turret",
                             min_rot_vel = 200,
                             max_rot_vel = 1000,
                             texture_size = self.texture_size,
                             texture_name="aiming",
                             image_dict = self.image_dict,
                             sound_dict = self.sound_dict)

        self.turret.attach_parent(self)
        self.turret.attach_weapon(weapon)
        
        self.trackRot = False
        self.damp_factor = 1

    def set_world(self, world):
        super().set_world(world)
        self.world.add_game_object(self.turret)

    def rotateLeft(self):
        self.rotvel = self.rotSpeedMax

    def rotateRight(self):
        self.rotvel = -self.rotSpeedMax

    def goForward(self):
        self.acc = (-self.acc_lin * math.sin(self.rot * math.pi / 180),
                    -self.acc_lin * math.cos(self.rot * math.pi / 180))

    def goBack(self):
        self.acc = (self.acc_lin * math.sin(self.rot * math.pi / 180),
                    self.acc_lin * math.cos(self.rot * math.pi / 180))

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

    def shoot(self, **kwargs):
        self.turret.fire(**kwargs)

    def destroy(self):
        self.liveflag = 0
        self.turret.destroy()

    def collisionEffect(self,  dt, obj):
        if obj.tag == ENEMY_PROJECTILE_TAG:
            self.gotHit(obj.damage)
            obj.destroy()
        elif obj.tag == ENEMY_TAG:
            self.gotHit(obj.coll_damage)
            Playable.collisionEffect(self, dt, obj)
            if obj.suicide:
                obj.destroy()
        else:
            return
        
        if self.liveflag:
            self.spawn_particles_on_pos(10,(5,5),200,5,1)
        else:
            self.spawn_particles_on_pos(10,(10,10),300,4,1)

    def render(self):
        if self.collide_box(self.world.camera):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = scalar_div(img0.get_size(),2)
            self.world.screen.blit(img0, element_sub(element_sub(self.pos, self.world.camera.topLeft),dummy))

    def update(self, dt,  **kwargs):
        super().update(dt, **kwargs)

        if self.trackRot and self.acc != (0, 0):
            self.acc = (-self.acc_lin * math.sin(self.rot * math.pi / 180),
                        -self.acc_lin * math.cos(self.rot * math.pi / 180))
        elif self.acc == (0, 0):
            self.vel = scalar_mul(self.vel, math.exp(-self.damp_factor * dt))

        self.vel = (capRange(self.vel[0], -self.speedMax, self.speedMax),
                    capRange(self.vel[1], -self.speedMax, self.speedMax))
        
        # update turret
        target_rot = None
        # if (self.world):
        #     target_rot = math.degrees(math.atan2(*unit_tuple2(element_sub(self.pos,self.world.camera.topLeft),self.world.get_scaled_mouse_pos())))
        
        self.turret.target_rot = target_rot

        self.hull.update(dt)
