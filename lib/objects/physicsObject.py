import pygame
import numpy as np
from ..imageDict import imageDict
from .gameObject import gameObject

class physicsObject(gameObject):
    def __init__(self, position : np.array = np.array([0,0]),
                 imageDict : imageDict = None,
                 texture : str = "",
                 velocity : np.array = np.array([0,0]),
                 acceleration : np.array = np.array([0,0]),) -> None:
        super().__init__(position, imageDict, texture)
        self.__last_position__ = None
        self.velocity = velocity
        self.acceleration = acceleration
    
    def update(self, dt, boundary : np.array, tolerance : np.array = np.array([0,0]), doWrap = False):
        self.__last_position__ = np.array(self.position)
        self.position = self.position + self.velocity * dt
        self.velocity = self.velocity + self.acceleration * dt
        ####################################################
        #EXPERIMENNTAL WILL MOVE INTO OWN MODULE... PROBABLY
        ####################################################
        if (doWrap):
            for axis in range(2):
                if self.position[axis] > boundary[axis]+tolerance[axis]:
                    self.position[axis] = 0-tolerance[axis]
                if self.position[axis] < 0-tolerance[axis]:
                    self.position[axis] = boundary[axis]+tolerance[axis]
        else:
            for axis in range(2):
                if self.position[axis] > boundary[axis]+tolerance[axis]:
                    self.position[axis] = boundary[axis]+tolerance[axis]
                    self.velocity[axis] = -self.velocity[axis]/100
                if self.position[axis] < 0-tolerance[axis]:
                    self.position[axis] = 0-tolerance[axis]
                    self.velocity[axis] = -self.velocity[axis]/100