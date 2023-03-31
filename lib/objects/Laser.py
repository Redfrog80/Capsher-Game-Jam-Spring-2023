from .GameObject import GameObject;


class Laser(GameObject):
    def __init__(self, name: str = "", pos: tuple = ..., size: tuple = ..., img: str = "", dmg: float = 0):
        super().__init__(name, pos, size, img);
        self.dmg = dmg;