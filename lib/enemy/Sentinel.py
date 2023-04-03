import math
from lib.misc import *
from lib.objects import *
from enemy import *;
from pygame import surface, transform;


class Sentinel(Enemy):
    def __init__(self, name: str = "", pos: tuple = ..., size: tuple = ..., img: str = "resources/images/notfound.png"):
        super().__init__(name, pos, size, img);

        self.gun = EnemyGun(self.name + " gun", (0, 0), self.size, "resources/images/aiming.png")
        #This guy will stay at a large distance from the player and shoot stuff
        self.gun.setTextureSize((128, 128))
        self.gun.trackCenter(self)
        self.cooldown = 10;
        self.timer = 0;

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

    def shoot(self, dt, name):
        return self.gun.shoot(dt,name);

    def update(self, dt: float, **kwargs):
        self.timer += dt;
        if self.timer >= self.cooldown:
            self.shoot(dt, "hostileBullet");

        if self.target:
            self.trackTarget(dt)
    
    def render(self, screen: surface, cam: Camera):
        if self.checkCollision(cam):  # render when object collide with camera view
            img0 = transform.rotate(self.texture, self.rot)
            dummy = divTuple(subTuple(img0.get_size(), self.boundary.size), 2)
            screen.blit(img0, subTuple(subTuple(self.boundary.topleft, cam.boundary.topleft), dummy))
            self.gun.render(screen, cam)