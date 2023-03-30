import pygame
pygame.init()

# initializer
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Bug shooter")

# render setting
FPS = 120
clock = pygame.time.Clock()

run = True
while run:
    dt = clock.tick(FPS)
    print(str(clock.get_fps()) + " dt:" + str(dt))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
pygame.quit()

