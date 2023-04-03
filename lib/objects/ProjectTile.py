from ..misc import *
from .Base import Base
from .GameObject import GameObject
from .Camera import Camera
from .Particle import ParticleSimple
import lib.objects
import lib.enemy

from pygame import image, surface, transform

import math

class Projectile(GameObject):
    def __init__(self, name: str = "bullet", dmg: float = 0, life: float = 10, size: tuple = (10, 10),
                 img: str = "resources/images/plasmaball.png"):
        """
        since we're using rectangle collider, all bullet will be small square to prevent bug when bullet travel at an
        angle
        """
        super().__init__(name=name, pos=(100000, 100000), size=size, img=img)
        self.dmg = dmg
        self.totallife = life
        self.life = life

    def traj(self, pos: tuple, gun_velocity: tuple, speed: float, rot: float, speed_amp: float):
        """
        :param gun_velocity: current velocity of the gun
        :param speed: projectTile Speed
        :param rot: rotation
        :param pos: starting position
        :param speed_amp: speed amplifier factor
        """
        self.rot = rot
        self.pos = pos
        self.vel = addTuple(gun_velocity, (-speed * math.sin(math.radians(self.rot)) * speed_amp, -speed *
                                           math.cos(math.radians(self.rot)) * speed_amp))


    def collisionEffect(self, world, dt, object):
        if not isinstance(object, (ParticleSimple,lib.objects.Gun,Projectile)):
            if isinstance(object, (lib.enemy.Assault,lib.enemy.Juggernaut, lib.enemy.Kamikaze)) and object.tag == "player_bullet":
                self.spawn_particles_on_pos(world,10,(1,1),(100,100),3,1)
            elif isinstance(object, lib.objects.Player) and object.tag == "enemy_bullet":
                self.spawn_particles_on_pos(world,10,(1,1),(100,100),3,1)

    def update(self, dt: float, **kwargs):
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))
        self.life -= dt
        if self.life < 0:
            self.destroy()

    def matchBoundaryToTexture(self):
        """match size of boundary to texture"""
        self.boundary.update(subTuple(self.pos, divTuple(self.texture.get_size(), 2)),
                             divTuple(self.texture.get_size(), 2))

    def render(self, screen: surface, cam: Camera):
        if self.checkCollision(cam):  # render when object collide with camera view
            # self.setTextureSize(mulTuple(self.orig_text_size, abs(self.life / self.totallife)))
            img0 = transform.rotate(self.texture, self.rot)
            img1 = transform.scale_by(img0, abs(self.life / self.totallife))
            dummy = divTuple(subTuple(img1.get_size(), self.boundary.size), 2)
            screen.blit(img1, subTuple(subTuple(self.boundary.topleft, cam.boundary.topleft), dummy))
