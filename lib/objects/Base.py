from lib.misc import *
from lib.objects.Collider import Collider

class Base(Collider):
    """
    Base class for all game object
    """

    def __init__(self, **kwargs) -> None:
        
        super().__init__(**kwargs)
        
        self.name = kwargs.get("name") or "unnamed_object"
        self.tag = kwargs.get("tag") or ""
        self.vel = kwargs.get("vel") or (0,0)
        self.acc = kwargs.get("acc") or (0,0)
        self.rot = kwargs.get("rot") or 0
        self.rotvel = kwargs.get("rotvel") or 0
        self.liveflag = 1  # use in GameWorld to check if object should be destroyed (go out of bound, died, etc.)

    def destroy(self):
        self.liveflag = 0

    def objAlive(self):
        return bool(self.liveflag)
    
    def update(self, dt, **kwargs):
        self.set_pos(element_add(self.pos, scalar_mul(self.vel, dt)))
        self.vel = (element_add(self.vel, scalar_mul(self.acc, dt)))
        
        self.rot += self.rotvel*dt
