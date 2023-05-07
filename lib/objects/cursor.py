import pygame
from pygame import image, surface, transform
from random import random

from ..misc import *
from ..managers import *
from .Base import Base
from .Particle import ParticleSimple
from ..misc import *

class cursor(Base):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.texture_name = kwargs.get("texture_name") or "cursor2"
        self.image_dict = kwargs.get("image_dict") or imageDict()
        self.sound_dict = kwargs.get("sound_dict") or soundDict()
        
        self.texture = self.image_dict.get_image(self.texture_name) or self.image_dict.load_image("resources/images/" + self.texture_name + ".png")
        
        self.texture_size = kwargs.get("texture_size") or (16,16)
        self.shape = scalar_div(self.texture_size,4)
        self.setTextureSize(self.texture_size)
        

    def setTextureSize(self, size: tuple):
        self.texture = transform.scale(self.texture, size)

    def render(self):
        if self.collide_box(self.world.camera):  # render when object collide with camera view
            dummy = scalar_div(self.texture.get_size(),2)
            self.world.screen.blit(self.texture, element_sub(element_sub(self.pos, self.world.camera.topLeft),dummy))

    def update(self, dt, **kwargs):
        self.set_pos(element_add(self.world.get_scaled_mouse_pos(), self.world.camera.topLeft))