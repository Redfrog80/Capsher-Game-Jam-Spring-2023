print("yeet")

import pygame
import os
import math
import random
class Bugger:
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join('images', 'amogus.png'))
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0 # init values, do not change
        self.accel_x = 0.1
        self.accel_y = 0.1
        self.max_speed_x = 8
        self.max_speed_y = 8
        self.speed_multiplier = 1 # warning, this changes overall speed
        self.damp_factor = 0.3
        self.max_follow_distance = 1000 # may not be necessary
    
    def randomize_position(self, screen_width, screen_height):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)

    def update(self, player_x, player_y):

        player_x, player_y = pygame.mouse.get_pos() # makes bot follow mouse
        self.dir_x = player_x - self.x
        self.dir_y = player_y - self.y
        self.dir_length = max(1, math.sqrt(self.dir_x ** 2 + self.dir_y ** 2))
        self.dir_x /= self.dir_length
        self.dir_y /= self.dir_length # Normalizes vector
        
        # Move towards the player if within range
        if self.dir_length < self.max_follow_distance:
            if self.dir_x < 0:
                self.speed_x -= self.accel_x
                if self.speed_x < -self.max_speed_x:
                    self.speed_x = -self.max_speed_x
            elif self.dir_x > 0:
                self.speed_x += self.accel_x
                if self.speed_x > self.max_speed_x:
                    self.speed_x = self.max_speed_x
            if self.dir_y < 0:
                self.speed_y -= self.accel_y
                if self.speed_y < -self.max_speed_y:
                    self.speed_y = -self.max_speed_y
            elif self.dir_y > 0:
                self.speed_y += self.accel_y
                if self.speed_y > self.max_speed_y:
                    self.speed_y = self.max_speed_y
        else:
                if self.speed_x > 0:
                    self.speed_x -= self.accel_x * self.damp_factor
                elif self.speed_x < 0:
                    self.speed_x += self.accel_x * self.damp_factor
                if self.speed_y > 0:
                    self.speed_y -= self.accel_y * self.damp_factor
                elif self.speed_y < 0:
                    self.speed_y += self.accel_y * self.damp_factor

        self.x += self.speed_x * self.speed_multiplier
        self.y += self.speed_y * self.speed_multiplier

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Target Practice")

target_image = pygame.image.load(os.path.join('images', 'gameImage.png'))
bugger_image = pygame.image.load(os.path.join('images', 'amogus.png'))

buggers=[] # Initialize and spawn 4 buggers inside the dimensions of the screen
for i in range(4):
    bugger = Bugger(0, 0)
    bugger.randomize_position(screen_width, screen_height)
    buggers.append(bugger)
    
running = True # Makes sure game closes after manually quitting. It Mac it won't otherwise.
while running:
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