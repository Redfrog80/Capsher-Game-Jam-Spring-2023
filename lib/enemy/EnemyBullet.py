
from ..misc import *
from lib.objects import *;
from pygame import image, surface, transform

import math


class Projectile(GameObject):
    def __init__(self, name: str = "bullet", dmg: float = 0, life : float = 10, size: tuple = (16, 16),
                 img: str = "resources/images/plasmaball.png"):
        """
        since we're using rectangle collider, all bullet will be small square to prevent bug when bullet travel at an
        angle
        """
        super().__init__(name=name, pos=(100000,100000), size=size, img=img)
        self.boundary.update(subTuple(self.pos, divTuple(self.texture.get_size(), 2)), (5,5))
        self.dmg = dmg
        self.totallife = life
        self.life = life

    def traj(self, pos: tuple, gun_velocity: tuple, speed: float, rot: float, speed_amp: float):
        """
        :param speed: projectTile Speed
        :param rot: rotation
        :param pos: starting position
        :param speed_amp: speed amplifier factor
        """
        self.rot = rot
        self.pos = pos
        self.vel = addTuple(gun_velocity,(-speed*math.sin(math.radians(self.rot))*speed_amp, -speed*math.cos(math.radians(self.rot))*speed_amp))

    def collisionEffect(self,dt, object):
        pass

    def update(self, dt: float, **kwargs):
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))
        self.life -= dt
        if (self.life < 0):
            self.destroy()

    def matchBoundaryToTexture(self):
        """match size of boundary to texture"""
        self.boundary.update(subTuple(self.pos, divTuple(self.texture.get_size(), 2)), divTuple(self.texture.get_size(), 2))


    def render(self, screen: surface, cam: Camera):
        if self.checkCollision(cam):  # render when object collide with camera view
            self.setTextureSize(mulTuple(self.size,abs(self.life / self.totallife)))
            img0 = transform.rotate(self.texture, self.rot)
            dummy = divTuple(subTuple(img0.get_size(), self.boundary.size), 2)
            screen.blit(img0, subTuple(subTuple(self.boundary.topleft, cam.boundary.topleft), dummy))