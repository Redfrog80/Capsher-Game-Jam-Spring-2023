import pygame
from lib.ImageDict import imageDict
from lib.objects import Camera, GameObject
from gameWorld import gameWorld

pygame.init()

# initializer
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Bug shooter")

# render setting
FPS = 60
clock = pygame.time.Clock()

run = True
while run:
    dt = clock.tick(FPS)
    print(str(clock.get_fps()) + " dt:" + str(dt))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
    
    camera = Camera("cam", (0, 0), win.get_size())
    firstObject = GameObject("dummy", (400, 400), (0, 0))
    firstObject.matchBoundaryToTexture()
    secondObject = GameObject("dummy", (100, 100), (0, 0))
    secondObject.matchBoundaryToTexture()
    
pygame.quit()

