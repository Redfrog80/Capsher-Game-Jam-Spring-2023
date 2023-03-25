

# This is somewhat cursed, but it will let me run a __main__ file from anywhere in the python path
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from lib.objects.physicsObject import *
        from lib.objects.staticCamera import *
        from lib.imageDict import *
    else:
        from ..lib.objects.physicsObject import *
        from ..lib.objects.staticCamera import *
        from ..lib.imageDict import *

from tkinter import W
import pygame
import numpy as np
from gameWorld import gameWorld

pygame.init()

screen = pygame.display.set_mode([1200,800])

# Loads ALL png files in images/ into a surface dictionary.
imgDict = imageDict("images/")

camera = staticCamera(np.array([0,0]))

# Game world, will be a container which forces our objects to stay within its bounds and provides a means for collision detection
# Will need to make it so we can define both corners 
# Will need to make the camera stay inside the viewable area so things don't pop into existance
world = gameWorld(np.array([1200,800]), np.array([0,0]), camera)

running = True
obj = physicsObject(np.array([0,0]), imgDict, "notfound2", np.array([400,400]))
obj2 = physicsObject(np.array([250,250]), imgDict, "notfound", np.array([-50,40]))


world.add_phys_object("obj",obj)
world.add_phys_object("obj2",obj2)

clock = pygame.time.Clock()

while(running):
    clock.tick(120)
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))
    
    # Set camera on object's position
    camera.position = obj.position
    
    # Draw everything
    world.render(screen)
    # Update physics, enable objects to wrap around
    world.update(clock.get_time()/1000, doWrap=True)


    print(world.__phys_objects__["obj"].position)

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
