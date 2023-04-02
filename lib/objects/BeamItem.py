from .GameObject import GameObject;
from .Player import Player;


class BeamItem(GameObject):
    
    def __init__(self, name: str = "powerup", pos: tuple = ..., vel: tuple = (0, 0), acc: tuple = (0, 0), size: tuple = (30, 30), img: str = "resources/images/amogus.png"):
        super().__init__(name, pos, vel, acc, size, img);
        self.pos = pos;

    def collisionEffect(self, dt, object):
        if isinstance(object, Player):
            object.laserBeam = True;
            self.destroy();

        