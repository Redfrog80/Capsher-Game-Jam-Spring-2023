import math
from lib.misc import *
from lib.objects import *


class Queen(Enemy):
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/amogus.png"):
        super().__init__(name, pos, size, img)
