from ..misc import *


class thruster():
    def __init__(self,
                 vel_max = 100,
                 acc = 10,
                 rot_vel = 45) -> None:
        
        self.vel_max_real = None
        self.vel_max_base = vel_max
        self.vel_max_multiplier = 1
        
        self.acc_real = None
        self.acc_base = acc
        self.acc_multiplier = 1

        self.rot_vel_real = None
        self.rot_vel_base = rot_vel
        self.rot_vel_multiplier = 1
        
        self.update_stats()

    def update_stats(self):
        self.vel_max_real = self.vel_max_base * self.vel_max_multiplier
        self.acc_real = self.acc_base * self.acc_multiplier
        self.rot_vel_real = self.rot_vel_base * self.rot_vel_multiplier
        
    def get_vel_max(self):
        return self.vel_max_real
    def get_acc(self):
        return self.acc_real
    def get_rot_vel(self):
        return self.rot_vel_real

    def check_vel(self, vel):
        if (magnitude(vel) > self.vel_max_real):
            vel = scalar_mul(unit_tuple1(vel), self.vel_max_real)
        return vel