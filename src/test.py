import pygame
import numpy as np
from object import *
pygame.init()

screen = pygame.display.set_mode([500,500])

running = True
obj = physics_object()
obj.position = np.array([0,0])
obj.velocity = np.array([100,100])

clock = pygame.time.Clock()

while(running):
    clock.tick(120)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    obj.update(clock.get_time()/1000)
    obj.render(screen)

    # Flip the display
    pygame.display.flip()
    

# Done! Time to quit.
pygame.quit()
