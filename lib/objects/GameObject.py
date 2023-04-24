import pygame

from ..misc import *
from ..managers import *
from .Base import Base
from .Particle import ParticleSimple
from pygame import image, surface, transform

class GameObject(Base):
    """
    game object: can be rendered and have update movement
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.texture_name = kwargs.get("texture_name") or "notFound"
        self.image_dict = kwargs.get("image_dict") or imageDict()
        self.texture = self.image_dict.get_image(self.texture_name) or self.image_dict.load_image("resources/images/" + self.texture_name + ".png")
        
        self.texture_size = kwargs.get("texture_size") or self.texture.get_size()
        self.shape = scalar_div(self.texture_size,4)
        self.setTextureSize(self.texture_size)

    def collisionEffect(self, world, dt, obj):
        self.prevent_circle_overlap(obj)
        self.vel = element_sub(scalar_mul(unit_tuple1(self.vel), -0.7*magnitude(self.vel)),
                            scalar_mul(unit_tuple1(obj.vel), 0.7*magnitude(obj.vel)))

    def spawn_particles_on_pos(self, world, quantity: int, size: tuple, velMax: int, lifeMax: float, drag: float ):
        for i in range(quantity):
            p = ParticleSimple(self.name, PARTICLE_TAG, pos = self.pos,shape = size)
            p.set_random(velMax,lifeMax,drag)
            p.color = pygame.transform.average_color(self.texture, consider_alpha = True)
            world.add_game_object(p)

    def setTextureSize(self, size: tuple):
        self.texture = transform.scale(self.texture, size)

    def render(self, world):
        if self.collide_box(world.camera):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = scalar_div(img0.get_size(),2)
            world.screen.blit(img0, element_sub(element_sub(self.pos, world.camera.topLeft),dummy))

    def update(self, dt, **kwargs):
        super().update(dt, **kwargs)