from .steering import *
from lib.misc import *
from lib.objects import Base

class faceVelBehavior(steering):
    def __init__(self, weight) -> None:
        super().__init__()
        self.weight = weight
        self.target = None
        
    def get_steering(self, steering_base: steeringBehavior, *args, **kwargs):
        steering = steering_data()
        
        if not self.target.liveflag:
            return steering
        
        direction = degrees(atan2(*unit_tuple1(self.obj.vel)))

        difference = self.obj.rot - direction
        
        while (abs(difference) > 180):
            difference -= 360*sign(difference)

        steering.rot_vel = difference
        steering.acc = (0,0)
        return steering