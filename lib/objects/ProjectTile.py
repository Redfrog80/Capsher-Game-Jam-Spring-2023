from .GameObject import GameObject
from lib.misc import *
import math


class Projectile(GameObject):
    def __init__(self, name: str = "bullet", dmg: float = 0, size: tuple = (16, 16),
                 img: str = "resources/images/plasmaball.png"):
        """
        since we're using rectangle collider, all bullet will be small square to prevent bug when bullet travel at an
        angle
        """
        super().__init__(name=name, pos=(0, 0), size=size, img=img)
        self.matchTextureToBoundary()  # small bullet
        print(self.boundary.size)
        self.dmg = dmg

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

    def update(self, dt: float, **kwargs):
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))
