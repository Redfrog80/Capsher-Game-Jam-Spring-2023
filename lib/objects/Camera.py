from .Base import Base
from ..misc import *


class Camera(Base):
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0)):
        super().__init__(name=name, pos=pos, vel=(0, 0), acc=(0, 0), size=size)
        self.follow = None
        self.world = None
    def trackCenter(self, other_object: Base):
        self.follow = other_object
    
    def set_world(self, world):
        self.world = world

    def update(self):
        if self.follow is not None:
            self.pos = addTuple(self.pos, subTuple(self.follow.boundary.center, self.boundary.center))
            self.boundCenterToPos()
            self.world.border_default(dt = 0, object = self, key = "camera")
                