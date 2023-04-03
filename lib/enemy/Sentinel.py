import math
from lib.misc import *
from lib.objects import *



class Sentinel(Enemy):
    def __init__(self, name: str = "", pos: tuple = ..., size: tuple = ..., img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, size, img);

        #This guy will stay at a large distance from the player and shoot stuff


    def trackTarget(self, dt):
        self.pos = addTuple(self.pos, mulTuple(self.vel, dt))
        self.boundCenterToPos()

        if bool(self.target):
            x, y = self.target.pos
            #difference between this and player pos
            dx = x - self.pos[0]
            dy = y - self.pos[1]
            length = math.sqrt(dx ** 2 + dy ** 2)
            self.rot = math.degrees(math.atan2(dy, dx)) - 180
            speedAdd = 0
            if self.hover_distance < length < self.max_follow_distance:
                # move to player
                speedAdd = self.acc_lin * dt
            elif self.hover_distance > length:
                # move away
                speedAdd = -self.acc_lin * dt
            else:
                #damp speed
                self.vel = mulTuple(self.vel, math.exp(- self.damp_factor))
            self.vel = addTuple(self.vel, (-speedAdd * math.sin(math.radians(self.rot+90)), speedAdd * math.cos(math.radians(self.rot+90))))
            self.vel = (capRange(self.vel[0], -self.speedMax, self.speedMax), capRange(self.vel[1], -self.speedMax, self.speedMax))