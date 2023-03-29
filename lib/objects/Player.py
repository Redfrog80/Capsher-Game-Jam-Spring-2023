from .Playable import Playable
from ..misc import *;
from math import *;



class Player(Playable):
    """
    Player Class. Support control, power up, etc.
    """
    
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, size, img)
        self.trackRot = False;
        self.accMag = 0.0003;

    def setSpeed(self, spd):
        self.vel = spd;
    def setAccel(self, acc):
        self.acc = acc;

    def update(self, dt: float):
        if self.trackRot and self.acc != (0, 0):
            self.acc = ((-self.accMag * sin(self.rot * pi / 180), -self.accMag * cos(self.rot * pi / 180)));
        
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()
        self.vel = addTuple(self.vel, mulTuple(self.acc, dt))
        self.rot += self.rotv;
        

