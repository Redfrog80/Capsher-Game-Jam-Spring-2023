from .steering import *
from lib.misc import *
from lib.objects import Base

class fleeBehavior(steering):
    def __init__(self, weight) -> None:
        super().__init__()
        self.weight = weight
        self.target = None
        
    def get_steering(self, steering_base: steeringBehavior, *args, **kwargs):
        steering = steering_data()
        
        if not self.target.liveflag:
            return steering
        
        steering.acc = unit_tuple2(self.target.pos, self.obj.pos)
        steering.acc = scalar_mul(steering.acc, -steering_base.acc_max)
        steering.rot_vel = 0
        return steering