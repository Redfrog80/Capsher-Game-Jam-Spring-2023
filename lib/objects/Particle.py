from ..objects import Camera
from ..misc import *
from .Base import Base

import pygame
from pygame import Surface
import math
import random

class ParticleSimple(Base):
    def __init__(self, name: str = "", pos: tuple = (0,0), vel: tuple = (0,0), acc: tuple = (0,0), size: tuple = (10,10)):
        """
        Just a simple particle object
        """
        super().__init__(name=name, pos=pos, size=size)

        self.totallife = 0
        self.life = 0
        self.drag = 1
        self.color = (255,255,255)
        self.radius = magnitude(size)

    def set_random(self, velMax: tuple, lifeMax: float, drag: int):
        self.vel = addTuple(self.vel, (random.randint(0,velMax[0]), random.randint(0,velMax[1])))
        self.totallife = random.uniform(0,lifeMax)
        self.life = self.totallife
        self.drag = drag

    def collisionEffect(self, world, dt, object):
        pass

    def update(self, dt, **kwargs):
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = divTuple(addTuple(self.vel, mulTuple(self.acc, dt)),1+dt*self.drag)
        self.life -= dt
        
        if (self.life < 0):
            self.destroy()

    def render(self, screen: Surface, cam: Camera):
        if self.checkCollision(cam):  # render when object collide with camera view
            pygame.draw.circle(screen,self.color,subTuple(self.pos, cam.boundary.topleft),self.radius*self.life/self.totallife)