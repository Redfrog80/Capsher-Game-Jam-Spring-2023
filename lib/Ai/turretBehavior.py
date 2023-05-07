from .steering import *
from lib.misc import *
from lib.objects import Base

class turretBehavior(steering):
    def __init__(self, weight) -> None:
        super().__init__()
        self.weight = weight
        self.target = None
        
    def get_steering(self, steering_base: steeringBehavior, dt, *args, **kwargs):
        steering = steering_data()
        
        if not self.target.liveflag or self.obj.tag != TURRET_TAG:
            return steering
        
        distance = dist(self.target.pos, self.obj.pos)
        delta = element_sub(self.target.pos, self.obj.pos)
        unit = scalar_div(delta, distance) if (distance) else (0,0)
        
        
        direction = degrees(atan2(*unit))
        
        difference = self.obj.rot - direction
        
        while (abs(difference) > 180):
            difference -= 360*sign(difference)
        
        steering.rot_vel = difference

        self.obj.distance = distance
        self.obj.angle_diff = difference
        
        return steering