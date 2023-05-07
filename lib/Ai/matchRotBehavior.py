from .steering import *
from lib.misc import *
from lib.objects import Base

class matchRotBehavior(steering):
    def __init__(self, weight) -> None:
        super().__init__()
        self.weight = weight
        self.target = None
        
    def get_steering(self, steering_base: steeringBehavior, *args, **kwargs):
        steering = steering_data()
        
        if not self.target.liveflag:
            return steering
        
        self.obj.rot = self.target.rot

        return steering