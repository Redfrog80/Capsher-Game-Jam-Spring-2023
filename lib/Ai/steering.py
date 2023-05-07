
from lib.misc import element_add, magnitude, scalar_mul, unit_tuple1, sign


class steering_data():
    def __init__(self) -> None:
        self.acc = (0,0)
        self.rot_vel = 0
        
class steeringBehavior():
    def __init__(self, obj, acc_max, rot_vel_max) -> None:
        self.obj = obj
        self.steerings = []
        self.acc_max = acc_max
        self.rot_vel_max = rot_vel_max
    
    def add_steering_behavior(self, behavior, target = None):
        behavior.obj = self.obj
        behavior.target = target
        self.steerings.append(behavior)
    
    def clear_steering_behaviors(self):
        self.steerings.clear()
    
    def set_new_target(self, target):
        for behavior in self.steerings:
            behavior.target = target
    
    def update(self, dt):
        acc = (0,0)
        rot_vel = 0
        for behavior in self.steerings:
            s = behavior.get_steering(self, dt=dt)
            acc = element_add(acc, scalar_mul(s.acc, behavior.weight))
            rot_vel = rot_vel + s.rot_vel * behavior.weight
            
        if magnitude(acc) > self.acc_max:
            acc = scalar_mul(unit_tuple1(acc),self.acc_max)
            
        if abs(rot_vel) > self.rot_vel_max:
            rot_vel = sign(rot_vel)*self.rot_vel_max
        
        self.obj.acc = acc
            
        if rot_vel:
            self.obj.rotvel = rot_vel

class steering():
    def __init__(self) -> None:
        self.obj = None
        self.weight = 1
    def get_steering(self, steering_base: steeringBehavior):
        pass
        