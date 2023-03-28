from lib import objects
import pygame
pygame.init()
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
        
# initializer
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Bug shooter")

# render setting
FPS = 60
clock = pygame.time.Clock()

camera = objects.Camera("cam", (0, 0), win.get_size())
firstObject = objects.GameObject("dummy", (400, 400), (0, 0))
firstObject.matchBoundaryToTexture()
secondObject = objects.GameObject("dummy", (100, 100), (0, 0))
secondObject.matchBoundaryToTexture()
secondObject.vel = (200, 200)

# camera track second object
camera.trackCenter(secondObject)

run = True
while run:
    dt = clock.tick(FPS)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # update calculation
    secondObject.rot += 1
    secondObject.update(dt)
    camera.update()
    # render
    win.fill((255, 255, 255))
    firstObject.render(win, camera)
    secondObject.render(win, camera)

    pygame.display.update()
pygame.quit()

