from ..misc import *
from .Base import Base
from .Camera import Camera
from pygame import image, surface, transform


class GameObject(Base):
    """
    game object: can be rendered and have update movement
    """
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, (0, 0), (0, 0), size)
        self.texture = image.load(img)

    def checkCollision(self, other: Base):
        return self.boundary.colliderect(other.boundary)

    def matchBoundaryToTexture(self):
        """match size of boundary to texture"""
        self.boundary.update(subTuple(self.pos, divTuple(self.texture.get_size(), 2)), self.texture.get_size())

    def matchTextureToBoundary(self):
        """match size of texture to boundary"""
        self.texture = transform.scale(self.texture, self.boundary.size)

    def render(self, screen: surface, cam: Camera):
        if self.checkCollision(cam):  # render when object collide with camera view
            if self.rot == 0:
                screen.blit(self.texture, subTuple(self.boundary.topleft, cam.boundary.topleft))
            else:
                img0 = transform.rotate(self.texture, self.rot)
                dummy = divTuple(subTuple(img0.get_size(), self.boundary.size), 2)
                screen.blit(img0, subTuple(subTuple(self.boundary.topleft, cam.boundary.topleft), dummy))

    def update(self, dt: float):
        pass

    def get_boundary_corners(self):
        return (self.boundary.topleft,self.boundary.topright, self.boundary.bottomleft, self.boundary.bottomright)
