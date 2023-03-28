import pygame
# This is somewhat cursed, but it will let me run a __main__ file from anywhere in the python path
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from lib.misc import *
        from lib.objects import Camera, GameObject
    else:
        from ..lib.misc import *
        from ..lib.objects import Camera, GameObject

from gameWorld import gameWorld

pygame.init()

# initializer
screen = pygame.display.set_mode((800, 800), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0)
pygame.display.set_caption("Bug shooter")

# render setting
FPS = 120
clock = pygame.time.Clock()

camera = Camera("cam", (0, 0), size = screen.get_size())

world = gameWorld(((0,0),(800,800)),(100,100),camera)
world.add_game_object("Player",GameObject("dummyTag", (400, 400), (100, 100)))
world.add_game_object("object",GameObject("dummyTag", (400, 400), (0, 0)))
world.set_tracked_object("object")

def defaultUpdate(dt,object, key):
    object.boundCenterToPos()
    object.pos = addTuple(object.pos, mulTuple(object.vel, dt))
    object.vel = addTuple(object.vel, mulTuple(object.acc, dt))

def drag(dt,object, key):
    object.vel = subTuple(object.vel, mulTuple(object.vel, dt * 0.5))
    print(object.vel)

run = True
while run:
    dt = clock.tick(FPS)/1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            
    
    screen.fill((255, 255, 255))
    
    world.render(screen)
    
    world.update(dt,defaultUpdate, drag)
    
    pygame.display.flip()
    
pygame.quit()

