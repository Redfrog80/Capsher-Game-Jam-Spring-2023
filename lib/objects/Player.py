import math
from random import random
from pygame import image, surface, transform

from lib.misc import *
from .Camera import Camera
from ..weapons import turret, bolter, flakker
from ..thrusters import thruster
from ..hulls import hull
from .Projectile import Projectile
from .Playable import Playable


class Player(Playable):

    def __init__(self, **kwargs):
        
        kwargs["name"] = kwargs.get("name") or "player"
        kwargs["tag"] = kwargs.get("tag") or PLAYER_TAG
        kwargs["texture_name"] = kwargs.get("texture_name") or "player1"
        kwargs["texture_size"] = kwargs.get("texture_size") or (64,64)
                
        player_hull = hull()
        player_thruster = thruster(1000,600,360)
        
        super().__init__(hull = player_hull,
                         thruster = player_thruster,  **kwargs)
        
        weapon = flakker(projectile_tag = PLAYER_PROJECTILE_TAG,
                        projectile_texture_name = "bullet3",
                        image_dict = self.image_dict,
                        sound_dict = self.sound_dict)
        
        self.turret = turret(name = "turret",
                             tag = TURRET_TAG,
                             min_rot_vel = 200,
                             max_rot_vel = 1000,
                             texture_size = self.texture_size,
                             texture_name = "aiming",
                             image_dict = self.image_dict,
                             sound_dict = self.sound_dict)

        self.turret.attach_parent(self)
        self.turret.attach_weapon(weapon)
        
    def set_world(self, world):
        super().set_world(world)
        self.world.add_game_object(self.turret)

    def rotateLeft(self):
        self.rotvel = self.thruster.get_rot_vel()

    def rotateRight(self):
        self.rotvel = -self.thruster.get_rot_vel()

    def goForward(self):
        self.acc = (-self.thruster.get_acc() * math.sin(self.rot * math.pi / 180),
                    -self.thruster.get_acc() * math.cos(self.rot * math.pi / 180))

    def goBack(self):
        self.acc = (self.thruster.get_acc() * math.sin(self.rot * math.pi / 180),
                    self.thruster.get_acc() * math.cos(self.rot * math.pi / 180))

    def rotateLeftStop(self):
        self.rotvel = 0

    def rotateRightStop(self):
        self.rotvel = 0

    def goForwardStop(self):
        self.acc = (0, 0)

    def stopAcc(self):
        self.acc = (0, 0)
        
    def stopRotVel(self):
        self.rotvel = 0

    def shoot(self, dt,  **kwargs):
        self.turret.fire(dt, **kwargs)

    def destroy(self):
        self.liveflag = 0
        self.turret.destroy()

    def collisionEffect(self,  dt, obj):
        if obj.tag == PLAYER_PROJECTILE_TAG:
            return
        if obj.tag != ENEMY_PROJECTILE_TAG:
            self.gotHit(obj.coll_damage)
            Playable.collisionEffect(self, dt, obj)
        
        if self.liveflag:
            self.spawn_particles_on_pos(10,(5,5),200,5,1)
        else:
            self.spawn_particles_on_pos(10,(10,10),300,4,1)

    def destroy(self):
        super().destroy()
        self.turret.destroy()
        self.liveflag = 0
        
        sound = self.sound_dict.get_sound("Death" + str(1+int(random())))
        if sound:
            sound.set_volume(0.3)
            sound.play()

    def render(self):
        if self.collide_box(self.world.camera):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = scalar_div(img0.get_size(),2)
            self.world.screen.blit(img0, element_sub(element_sub(self.pos, self.world.camera.topLeft),dummy))

    def update(self, dt,  **kwargs):
        super().update(dt, **kwargs)
        # update turret
        target_rot = None
        # if (self.world):
        #     target_rot = math.degrees(math.atan2(*unit_tuple2(element_sub(self.pos,self.world.camera.topLeft),self.world.get_scaled_mouse_pos())))
        
        self.turret.target_rot = target_rot

