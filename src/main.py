from audioop import mul
import pygame
from pygame.locals import *
from math import *
# This is somewhat cursed, but it will let me run a __main__ file from anywhere in the python path
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from lib.misc import *
        from lib.objects import *
    else:
        from ..lib.misc import *
        from ..lib.objects import *

from gameWorld import gameWorld

pygame.init()

# initializer

window_dim, tile_dim = (800,800), (100,100)
screen = pygame.display.set_mode(window_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0)
pygame.display.set_caption("test")

# render setting
FPS = 120
clock = pygame.time.Clock()

camera = Camera("camera", (0, 0), size = screen.get_size())

world = gameWorld(pygame.Rect(-2000,-2000,4000,4000),tile_dim,camera)
for i in range(200):
    world.add_game_object(str(i),Enemy("object", (i*10%2000, 200), (0, 0), img = "resources/images/notfoundTiny.png"))

player = Player("player", (0, 0), (64, 64), img="resources/images/ship.png");
gun = Gun("gun", (0, 0), (10, 10), screen.get_size(), "resources/images/directionalTest.png");

world.add_game_object("Player",player)
world.add_game_object("Player_gun",gun)

world.set_tracked_object("Player", "player")
gun.trackCenter(player)

run = True
while run:
    dt = clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == KEYDOWN:
            if event.key == K_w:
                #print("ship go forward");
                player.setAccel((-player.accMag * sin(player.rot * pi / 180), -player.accMag * cos(player.rot * pi / 180)));
                
            if event.key == K_s:
                player.setAccel((player.accMag * sin(player.rot * pi / 180), player.accMag * cos(player.rot * pi / 180)));
                #ship go backward
            if event.key == K_a:
                #ship go ccw
                player.rotvel = 0.1;
                player.trackRot = True;
                pass;
            if event.key == K_d:
                #ship go cw
                player.rotvel = -0.1;
                player.trackRot = True;
                pass;
        if event.type == KEYUP:
            if event.key == K_w:
                #print("ship go forward");
                #stop acceleration
                player.setAccel((0, 0));
                
            if event.key == K_s:
                #stop acceleration
                player.setAccel((0, 0));
            if event.key == K_a:
                #player stop rotating
                player.rotvel = 0;
                player.trackRot = False;
                pass;
            if event.key == K_d:
                player.rotvel = 0;
                player.trackRot = False;
                #player stop rotating
                pass;
        if event.type == MOUSEBUTTONDOWN:
            bullet = Projectile("bullet", "b", 1);
            bvrot = (-sin(gun.rot * (pi/180)), -cos(gun.rot * (pi/180)))
            bullet.vel = addTuple(bvrot, player.vel);
            bullet.pos = gun.pos;
            #bullet.traj(gun.pos, 1, gun.rot, 1);
            world.add_game_object("Player_bullet",bullet)
            print(len(world.__game_objects__["Player_bullet"]))
            print("SHOOT");
            pass;

            
    
    screen.fill((5, 5, 15))
    
    world.render_tile_map(screen)
    world.render(screen)
    
    world.update(dt)
    
    pygame.display.flip()
    
pygame.quit()

