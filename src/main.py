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
        from lib.misc import *
        #from lib.imageDict import *
    else:
        from ..lib.objects import *
        from ..lib.misc import *
        #from ..lib.imageDict import *

pygame.init()

# initializer
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Bug shooter")

# render setting
FPS = 120
clock = pygame.time.Clock()

handler = []
testThing = GameObject("reeeeee", (100, 100), (64, 64));
testThing1 = GameObject("reeeeeee", (1900, 1000), (64, 64));
testThing2 = GameObject("reeeeeeee", (1300, 800), (64, 64));
testThing3 = GameObject("reeeeeeeee", (1300, 100), (64, 64));

player = Player("player", (0, 0), (64, 64), "resources/images/ship.png");
gun = Gun("gun", (0, 0), (10, 10), win.get_size(), "resources/images/directionalTest.png");

camera = Camera("camera", (0, 0), win.get_size());



#handler.append(player);
#append objects to handler in order of appearence, ex: append gun after player if it is to be displayed above the player
handler.append(testThing);
handler.append(testThing1);
handler.append(testThing2);
handler.append(testThing3);

handler.append(player);
handler.append(gun);

camera.trackCenter(player);
run = True
while run:
    #print(camera.pos);
    #print(player.trackRot);
    dt = clock.tick(FPS)
    #print(str(clock.get_fps()) + " dt:" + str(dt))

    #set position of gun to always be on the player
    gun.pos = player.pos;
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        if event.type == KEYDOWN:
            if event.key == K_w:
                #print("ship go forward");
                player.goForward()

            if event.key == K_s:
                player.goForward()
                #ship go backward
            if event.key == K_a:
                player.rotateLeft()
            if event.key == K_d:
                player.rotateRight()
        if event.type == KEYUP:
            if event.key == K_w:
                player.goForwardStop()
            if event.key == K_s:
                player.goBackStop()
            if event.key == K_a:
                player.rotateLeftStop()
            if event.key == K_d:
                player.rotateRightStop()
        if event.type == MOUSEBUTTONDOWN:
            bullet = Projectile("bullet", "b", 1);
            bvrot = (-sin(gun.rot * (pi/180)), -cos(gun.rot * (pi/180)))
            bullet.vel = addTuple(bvrot, player.vel);
            bullet.pos = gun.pos;
            #bullet.traj(gun.pos, 1, gun.rot, 1);
            handler.append(bullet);
            print("SHOOT");
            pass;

    camera.update();
    win.fill((70, 70, 70));
    for i in handler:
        i.render(win, camera);
        i.update(dt);
    pygame.display.update();
    
pygame.quit()

