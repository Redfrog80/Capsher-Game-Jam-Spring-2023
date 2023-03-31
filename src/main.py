from audioop import mul
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

window_dim, tile_dim = (800,800), (10,10)
screen = pygame.display.set_mode(window_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0)
pygame.display.set_caption("test")

# render setting
FPS = 120
clock = pygame.time.Clock()

camera = Camera("camera", (0, 0), size = screen.get_size())

world = gameWorld(pygame.Rect(-2000,-2000,4000,4000),tile_dim,camera)
for i in range(200):
    world.add_game_object(str(i),GameObject("object", (i*10%2000, 200), (0, 0), img = "resources/images/notfoundTiny.png"))
world.add_game_object("Player",GameObject("IWANTTOMOVETHIS", (400, 400), (0, 0), img = "resources/images/ship.png"))
world.set_tracked_object("Player")

def defaultUpdate(self, dt, object, key):
    object.boundCenterToPos()
    object.pos = addTuple(object.pos, mulTuple(object.vel, dt))
    object.vel = addTuple(object.vel, mulTuple(object.acc, dt))

# This is temporary - just for prototyping
def drag(self, dt, object, key):
    if object.name!="IWANTTOMOVETHIS":
        object.vel = mulTuple(object.vel,0.999)
        object.vel = (object.vel[0], object.vel[1] + 1)
    else:
        object.vel = mulTuple(object.vel,0.999)
        

def dragToMouse(self, dt, object, key):
    if object.name=="IWANTTOMOVETHIS":
        object.vel = addTuple(object.vel,mulTuple(unitTuple(addTuple(pygame.mouse.get_pos(),self.__camera__.boundary.topleft),object.pos), 1000*dt))

def tmpHardBoundary(self, dt, object, key):
    object.boundCenterToPos()
    r = object.boundary
    
    if (r.top < self.__dim__.top):
        object.pos = (object.pos[0], object.pos[1] + self.__dim__.top - r.top)
        object.vel = (object.vel[0],-object.vel[1]/10)
    if (r.left < self.__dim__.left):
        object.pos = (object.pos[0] + self.__dim__.left - r.left, object.pos[1])
        object.vel = (-object.vel[0]/10,object.vel[1])

    if (r.bottom > self.__dim__.bottom):
        object.pos = (object.pos[0], object.pos[1] + self.__dim__.bottom - r.bottom)
        object.vel = (object.vel[0],-object.vel[1]/10)
    if (r.right > self.__dim__.right):
        object.pos = (object.pos[0] + self.__dim__.right - r.right, object.pos[1])
        object.vel = (-object.vel[0]/10,object.vel[1])
        
run = True
while run:
    dt = clock.tick(FPS)/1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
            
    
    screen.fill((5, 5, 15))
    
    world.render_tile_map(screen)
    world.render(screen)
    
    world.update(dt,defaultUpdate, drag, dragToMouse,tmpHardBoundary)
    
    pygame.display.flip()
    
pygame.quit()

