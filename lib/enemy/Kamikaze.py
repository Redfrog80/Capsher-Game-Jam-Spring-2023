from lib.objects import *


class Kamikaze(Enemy):
    def __init__(self, name: str = "", pos: tuple = (0, 0), size: tuple = (0, 0),
                 img: str = "resources/images/enemy1.png"):
        super().__init__(name, pos, size, img)
        self.coll_dmg = 50
        self.sucide = True
        # post process so I don't have to call this from main
        self.setTextureSize((64, 64))
        self.setStat(0, 0, 20, 20, 150, 300, 1000)
        self.follow_config(None, 800, 1, 0)
