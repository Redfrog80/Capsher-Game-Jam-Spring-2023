from .steering import *
from lib.misc import *
from lib.objects import Base

class faceBehavior(steering):
    def __init__(self, weight) -> None:
        super().__init__()
        self.weight = weight
        self.target = None
        
    def get_steering(self, steering_base: steeringBehavior, *args, **kwargs):
        steering = steering_data()
        
        if not self.target.liveflag:
            return steering
        
        direction = degrees(atan2(*unit_tuple2(self.target.pos, self.obj.pos)))
        
        difference = self.obj.rot - direction
        
        while (abs(difference) > 180):
            difference -= 360*sign(difference)

        steering.rot_vel = difference

        return steering