from .GameObject import GameObject;
from pygame import draw;
from math import *;


class Beam(GameObject):

    def __init__(self, pos:tuple, name: str = "beam", dmg: float = 300, life : float = 10, rot: float = 0, size: tuple = (16, 16), img: str = "resources/images/plasmaball.png"):
        super().__init__(name, pos=(9999999, 9999999), vel = (0, 0), acc = (0, 0), img = img);

        self.life = life;
        self.dmg = dmg;
        self.origdmg = self.dmg;
        self.life = life;
        self.origlife = self.life;
        self.pos = pos;
        self.endpoint = (-1500 * sin(self.rot * (pi / 180)), -1500 * cos(self.rot * (pi / 180)));

        self.boundary = (self.pos, self.endpoint);

    def update(self, dt:float, **kwargs):
        print(self.pos);
        self.life-=dt;
        if self.life <= 2*dt:
            self.destroy();

    def render(self, screen, camera):
        draw.line(screen, (200, 200, 200), self.pos, self.endpoint, 5);
