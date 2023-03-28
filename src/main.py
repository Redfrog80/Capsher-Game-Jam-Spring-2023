import pygame
from pygame.locals import *;

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
player = Player("player", (1200, 200), (64, 64));
testThing = GameObject("reeeeee", (1000, 100), (64, 64));
camera = Camera("camera", (0, 0), win.get_size());



handler.append(player);
handler.append(testThing);

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
                player.setAccel((0, -0.0005));
                
            if event.key == K_s:
                player.setAccel((0, 0.0005));
                #ship go backward
            if event.key == K_a:
                #ship go ccw
                pass;
            if event.key == K_d:
                #ship go cw
                pass;
        if event.type == KEYUP:
            if event.key == K_w:
                print("ship go forward");
                player.setAccel((0, 0));
                
            if event.key == K_s:
                player.setAccel((0, 0));
                #ship go backward
            if event.key == K_a:
                #ship go ccw
                pass;
            if event.key == K_d:
                #ship go cw
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

