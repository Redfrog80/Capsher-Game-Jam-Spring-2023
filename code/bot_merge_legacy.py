print("yeet")

import pygame
import os
import math
import random
from bugger_class import Bugger

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Target Practice")

target_image = pygame.image.load("resources/images/amogus.png")
bugger_image = pygame.image.load("resources/images/amogus.png")

buggers=[]
for i in range(4):
    bugger = Bugger(0, 0)
    bugger.randomize_position(screen_width, screen_height)
    buggers.append(bugger)
    
running = True # Makes sure game closes after manually quitting. It Mac it won't otherwise.
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    for bugger in buggers:
        bugger.update(0, 0)
        screen.blit(bugger_image, (bugger.x - bugger_image.get_width() / 2, bugger.y - bugger_image.get_height() / 2))

    pygame.display.flip()
    clock.tick(fps) # limits FPS and keeps frames consistent
    print("tick finished")


pygame.quit()
