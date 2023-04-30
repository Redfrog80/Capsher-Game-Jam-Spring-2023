
from ..objects import Camera
from ..misc import *
from .Base import Base

import pygame
from pygame import Surface
import math
import random

class ParticleSimple(Base):
    def __init__(self, name: str = "", tag: str = "", pos: tuple = (0,0), vel: tuple = (0,0), acc: tuple = (0,0), shape: tuple = (1,1)):
        """
        Just a simple particle object
        """
        super().__init__(name=name,tag=tag, pos=pos, shape=shape)

        self.totallife = 0
        self.life = 0
        self.drag = 1
        self.color = (255,255,255)

    def set_random(self, velMax: int, lifeMax: float, drag: int):
        self.vel = scalar_mul((random.uniform(-1,1),random.uniform(-1,1)),random.random()*velMax)
        self.totallife = random.random()*lifeMax
        self.life = self.totallife
        self.drag = drag

    def collisionEffect(self, dt, object):
        pass

    def update(self, dt: float, **kwargs):
        self.set_pos(element_add(self.pos, scalar_mul(self.vel, dt)))
        self.vel = scalar_div(element_add(self.vel, scalar_mul(self.acc, dt)),1+dt*self.drag)
        
        self.life -= dt
        if (self.life < 0):
            self.destroy()

    def render(self):
        if self.collide_box(self.world.camera):  # render when object collide with camera view
            pygame.draw.ellipse(self.world.screen,self.color,(element_sub(self.pos, self.world.camera.topLeft),scalar_mul(self.shape,self.life/self.totallife)))