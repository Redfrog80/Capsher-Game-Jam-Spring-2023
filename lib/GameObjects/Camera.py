import Base
import pygame.display


class Camera(Base.Base):
    def __init__(self, name: str = "", coo: tuple = (0, 0), vel: tuple = (0, 0), acc: tuple = (0, 0)):
        super().__init__(name, coo, vel, acc)
        