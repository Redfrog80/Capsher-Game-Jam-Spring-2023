from .Base import Base
from ..misc import *
import math


class Camera(Base):
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0)):
        super().__init__(name=name, pos=pos, vel=(0, 0), acc=(0, 0), size=size)
        self.follow_distance = 0
        self.target = None
        self.world = None

    def set_world(self, world):
        self.world = world

    def follow_config(self, target,follow_distance):
        self.follow_distance = follow_distance
        self.target = target
        self.pos = target.pos

    def trackTarget(self, dt):
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()

        if bool(self.target):
            length = magnitude(subTuple(self.target.pos, self.pos))
            unit = unitTuple(self.target.pos, self.pos)
            
            if length > self.follow_distance:
                self.pos = addTuple(self.pos,mulTuple(unit, length-self.follow_distance))

    def update(self, dt):
        if self.target:
            self.trackTarget(dt)
            self.boundCenterToPos()
            self.world.border_default(dt = 0, object = self, key = "camera")
                