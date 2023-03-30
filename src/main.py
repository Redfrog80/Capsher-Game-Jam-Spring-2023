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

window_dim, tile_dim = (800,800), (50,50)
screen = pygame.display.set_mode(window_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0)
pygame.display.set_caption("test")

# render setting
FPS = 120
clock = pygame.time.Clock()

camera = Camera("camera", (0, 0), size = screen.get_size())

world = gameWorld(((0,0),(800,800)),tile_dim,camera)
world.add_game_object("Player",GameObject("IWANTTOMOVETHIS", (401, 400), (0, 0), img = "resources/images/player.png"))
world.add_game_object("object",GameObject("object", (400, 400), (0, 0)))
world.set_tracked_object("Player")

def defaultUpdate(self, dt, object, key):
    object.boundCenterToPos()
    object.pos = addTuple(object.pos, mulTuple(object.vel, dt))
    object.vel = addTuple(object.vel, mulTuple(object.acc, dt))

# This is temporary - just for prototyping
def drag(self, dt, object, key):
    if object.name!="IWANTTOMOVETHIS":
        object.vel = subTuple(object.vel, mulTuple(object.vel, dt * 200))
    else:
        object.vel = subTuple(object.vel, mulTuple(object.vel, dt * 2))

def dragToMouse(self, dt, object, key):
    if object.name=="IWANTTOMOVETHIS":
        object.vel = addTuple(object.vel,mulTuple(unitTuple(addTuple(pygame.mouse.get_pos(),self.__camera__.boundary.topleft),object.pos), 1000*dt))

run = True
while run:
    dt = clock.tick(FPS)/1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            
    
    screen.fill((5, 5, 15))
    
    world.render_tile_map(screen)
    world.render(screen)
    
    world.update(dt,defaultUpdate, drag, dragToMouse)
    
    pygame.display.flip()
    
pygame.quit()

