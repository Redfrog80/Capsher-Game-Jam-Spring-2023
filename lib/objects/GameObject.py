
from ..misc import *
from .Base import Base
from .Camera import Camera
from pygame import image, surface, transform, draw


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
    def checkCollision(self, other: Base):
        try:
            return self.boundary.colliderect(other.boundary)
        except:
            try:
                #make lines from sides of rectangle, (start, end)
                line1 = ((self.boundary.x, self.boundary.y), (self.boundary.x, self.boundary.y + self.boundary.height));
                line2 = ((self.boundary.x, self.boundary.y), (self.boundary.x + self.boundary.width, self.boundary.y));
                line3 = ((self.boundary.x, self.boundary.y + self.boundary.height), (self.boundary.x + self.boundary.width, self.boundary.y + self.boundary.height));
                line4 = ((self.boundary.x + self.boundary.width, self.boundary.y), (self.boundary.x + self.boundary.width, self.boundary.y + self.boundary.height));

                #check for intersections
                return checkIntersection(self.boundary, line1) or checkIntersection(self.boundary, line2) or checkIntersection(self.boundary, line3) or checkIntersection(self.boundary, line4);
            except:
                return True;

    def collisionEffect(self, dt, object):
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
        draw.rect(screen, (255, 0, 0), self.boundary);
        if self.checkCollision(cam):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = divTuple(subTuple(img0.get_size(), self.boundary.size), 2)
            screen.blit(img0, subTuple(subTuple(self.boundary.topleft, cam.boundary.topleft), dummy))

    def update(self, dt: float, **kwargs):
        pass
    
    