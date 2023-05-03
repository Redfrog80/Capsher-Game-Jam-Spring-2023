from lib.Ai import *
from lib.objects import *
from lib.misc import *
from lib.hulls.defaultHull import hull

class Kamikaze(Enemy):
    def __init__(self, **kwargs):
        
        kwargs["name"] = kwargs.get("name") or "Kamikaze"
        kwargs["tag"] = kwargs.get("tag") or ENEMY_TAG
        kwargs["texture_size"] = kwargs.get("texture_size") or (24,24)
        kwargs["texture_name"] = kwargs.get("texture_name") or "enemy1"
        
        self.steeringBehavior = steeringBehavior(self, 400, 120)
        enemy_hull = hull(30, 0.03)
        
        super().__init__(hull = enemy_hull, **kwargs)
        
        self.coll_damage = 10
        self.suicide = True
        
    def setTarget(self, target):
        self.steeringBehavior.add_steering_behavior(pursueBehavior(1,2), target)
        self.steeringBehavior.add_steering_behavior(dragBehavior(1,.4))
        self.steeringBehavior.add_steering_behavior(faceVelBehavior(2), target)
        super().setTarget(target)
        