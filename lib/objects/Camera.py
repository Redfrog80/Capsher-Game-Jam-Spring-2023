from .Base import Base
from ..misc import *


class Camera(Base):
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0)):
        super().__init__(name, pos, (0, 0), (0, 0), size)
        self.follow = None

    def trackCenter(self, other_object: Base):
        self.follow = other_object

    def update(self):
        if self.follow is not None:
            self.pos = addTuple(self.pos, subTuple(self.follow.boundary.center, self.boundary.center))
            self.boundCenterToPos()