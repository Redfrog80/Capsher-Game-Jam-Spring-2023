from lib.objects import *
from lib.misc import *

class Kamikaze(Enemy):
    def __init__(self, **kwargs):
        
        kwargs["name"] = kwargs.get("name") or "Kamikaze"
        kwargs["tag"] = kwargs.get("tag") or ENEMY_TAG
        kwargs["texture_size"] = kwargs.get("texture_size") or (24,24)
        kwargs["texture_name"] = kwargs.get("texture_name") or "enemy1"
        
        super().__init__(**kwargs)
        self.coll_damage = 10
        self.suicide = True

        self.setStat(0, 0, 20, 50, 200, 300, 20)
        self.follow_config(None, 2000, 1, 0)