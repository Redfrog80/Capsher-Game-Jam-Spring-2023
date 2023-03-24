from turtle import position
import numpy
import pygame
import numpy as np
class object:
    def __init__(self) -> None:
        self.name = "None"
        self.position = np.array([0,0])
        self.velocity = np.array([0,0])
        self.acceleration = np.array([0,0])
        self.texture = pygame.image.load("images/notfound.png")
    def render(self, screen):
        #Centers the image on the object's position
        def texturePos():
            return (self.position[0]-self.texture.get_width()//2,
                    self.position[1]-self.texture.get_height()//2)
        screen.blit(self.texture,texturePos())

class physics_object(object):
    def __init__(self) -> None:
        super().__init__()
    def update(self, dt):
        self.position = self.position + self.velocity * dt
        self.velocity = self.velocity + self.acceleration * dt
        
# Camera is just a game object, to give a camera effect. just sub its cords with every game object