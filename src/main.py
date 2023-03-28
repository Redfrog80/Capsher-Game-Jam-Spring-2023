import pygame
from pygame.locals import *;
from math import *;

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from lib.objects import *;
        #from lib.imageDict import *
    else:
        from ..lib.objects import *
        #from ..lib.imageDict import *

pygame.init()

# initializer
win = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Bug shooter")

# render setting
FPS = 60
clock = pygame.time.Clock()

handler = [];
testThing = GameObject("reeeeee", (100, 100), (64, 64));
testThing1 = GameObject("reeeeeee", (1900, 1000), (64, 64));
testThing2 = GameObject("reeeeeeee", (1300, 800), (64, 64));
testThing3 = GameObject("reeeeeeeee", (1300, 100), (64, 64));

player = Player("player", (1200, 200), (64, 64), "resources/images/directionalTest.png");

camera = Camera("camera", (0, 0), win.get_size());



handler.append(player);
handler.append(testThing);
handler.append(testThing1);
handler.append(testThing2);
handler.append(testThing3);

camera.trackCenter(player);
run = True
while run:
    print(player.vel);
    dt = clock.tick(FPS)
    #print(str(clock.get_fps()) + " dt:" + str(dt))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == KEYDOWN:
            if event.key == K_w:
                print("ship go forward");
                player.setAccel((-0.0003 * sin(player.rot * pi / 180), -0.0003 * cos(player.rot * pi / 180)));
                
            if event.key == K_s:
                player.setAccel((0.0003 * sin(player.rot * pi / 180), 0.0003 * cos(player.rot * pi / 180)));
                #ship go backward
            if event.key == K_a:
                #ship go ccw
                player.rotv = 2;
                pass;
            if event.key == K_d:
                #ship go cw
                player.rotv = -2;
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
                player.rotv = 0;
                pass;
            if event.key == K_d:
                player.rotv = 0;
                #player stop rotating
                pass;
        if event.type == MOUSEBUTTONDOWN:
            #SHOOT
            pass;

    camera.update();
    win.fill((255, 255, 255));
    for i in handler:
        i.render(win, camera);
        i.update(dt);
    pygame.display.update();
    
pygame.quit()

