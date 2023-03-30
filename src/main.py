import pygame
from pygame.locals import *
from math import *

#print(468.51563%360);

if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from lib.objects import *
        #from lib.imageDict import *
    else:
        from ..lib.objects import *
        #from ..lib.imageDict import *

pygame.init()

# initializer
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Bug shooter")

# render setting
FPS = 60
clock = pygame.time.Clock()

handler = []
testThing = GameObject("reeeeee", (100, 100), (64, 64));
testThing1 = GameObject("reeeeeee", (1900, 1000), (64, 64));
testThing2 = GameObject("reeeeeeee", (1300, 800), (64, 64));
testThing3 = GameObject("reeeeeeeee", (1300, 100), (64, 64));

player = Player("player", (0, 0), (64, 64), "resources/images/directionalTest.png");
gun = Gun("gun", (0, 0), (10, 10), win.get_size(), "resources/images/directionalTest.png");
player.setStat(0, 100, 0, 100, 500, 360)
player.trackRot = True

camera = Camera("camera", (0, 0), win.get_size());



#handler.append(player);
handler.append(testThing)
handler.append(testThing1)
handler.append(testThing2)
handler.append(testThing3)
handler.append(gun)
handler.append(player)

camera.trackCenter(player)
run = True
while run:
    #print(camera.pos);
    #print(player.trackRot);
    dt = clock.tick(FPS) / 1000
    #print(str(clock.get_fps()) + " dt:" + str(dt))

    #set position of gun to always be on the player
    gun.pos = player.pos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == KEYDOWN:
            if event.key == K_w:
                #print("ship go forward")
                player.acc = (-player.accMag * sin(player.rot * pi / 180), -player.accMag * cos(player.rot * pi / 180))
            if event.key == K_s:
                player.acc = (player.accMag * sin(player.rot * pi / 180), player.accMag * cos(player.rot * pi / 180))
                #ship go backward
            if event.key == K_a:
                #ship go ccw
                player.rotateLeft()
                player.trackRot = True
                pass
            if event.key == K_d:
                #ship go cw
                player.rotateRight()
                player.trackRot = True
                pass;
        if event.type == KEYUP:
            if event.key == K_w:
                #print("ship go forward");
                #stop acceleration
                player.acc = (0, 0)
                
            if event.key == K_s:
                #stop acceleration
                player.acc = (0, 0)
            if event.key == K_a:
                #player stop rotating
                player.rotateLeftStop()
                player.trackRot = False
                pass;
            if event.key == K_d:
                player.rotateRightStop()
                player.trackRot = False
                #player stop rotating
                pass;
        if event.type == MOUSEBUTTONDOWN:
            #SHOOT
            pass

    camera.update()
    win.fill((255, 255, 255))
    for i in handler:
        i.render(win, camera)
        i.update(dt)
    pygame.display.update()
    
pygame.quit()

