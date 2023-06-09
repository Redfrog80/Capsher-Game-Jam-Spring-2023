
import pygame

from ..misc import *
from .Base import Base
from .Camera import Camera
from .Particle import ParticleSimple
from pygame import image, surface, transform


class GameObject(Base):
    """
    game object: can be rendered and have update movement
    """
    def __init__(self, name: str = "", pos: tuple = (0, 0), vel: tuple = (0, 0), acc: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/notfound.png"):
        super().__init__(name=name, pos=pos, vel=vel, acc=acc, size=size)
        self.texture = image.load(img).convert_alpha()
        self.setTextureSize(size)
        self.matchBoundaryToTexture()

    def collisionEffect(self,world , dt, object):
        direction = self.check_collide_direction(object)
        r = self.boundary
        b = self.boundary
        if direction[2] and not direction[0]:
            self.pos = (self.pos[0], self.pos[1] - r.top + b.bottom )
        elif direction[0] and not direction[2]:
            self.pos = (self.pos[0], self.pos[1] - r.bottom + b.top )
        elif direction[3] and not direction[1]:
            self.pos = (self.pos[0] - r.left + b.right, self.pos[1])
        elif direction[1] and not direction[3]:
            self.pos = (self.pos[0] - r.right + b.left, self.pos[1])
            
        self.vel = subTuple(mulTuple(unitTuple((0,0),self.vel), magnitude(self.vel)),  mulTuple(unitTuple((0,0),object.vel), -magnitude(object.vel)))
        


    def spawn_particles_on_pos(self, world, quantity: int, size: tuple, velMax: tuple, lifeMax: float, drag: float ):
        for i in range(quantity):
            p = ParticleSimple(str(i) + self.name + str(self.pos), pos=self.pos,size=(2,2))
            p.set_random(velMax,lifeMax,drag)
            p.color = pygame.transform.average_color(self.texture, consider_alpha=True)
            world.add_game_object("particles",p)

    def matchBoundaryToTexture(self):
        """match size of boundary to texture"""
        self.boundary.update(subTuple(self.pos, divTuple(self.texture.get_size(), 4)), divTuple(self.texture.get_size(), 4))

    def matchTextureToBoundary(self):
        """match size of texture to boundary"""
        self.texture = transform.scale(self.texture, self.boundary.size)

    def setTextureSize(self, size: tuple):
        self.texture = transform.scale(self.texture, size)
        self.matchBoundaryToTexture()

    def render(self, screen: surface, cam: Camera):
        
        if self.checkCollision(cam):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = divTuple(subTuple(img0.get_size(), self.boundary.size), 2)
            screen.blit(img0, subTuple(subTuple(self.boundary.topleft, cam.boundary.topleft), dummy))

    def update(self, dt: float, **kwargs):
        pass
