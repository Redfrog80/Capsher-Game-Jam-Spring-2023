print("yeet")

import pygame
import os

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()
fps = 60

# Set up the display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Target Practice")

# Load the target image
target_image = pygame.image.load(os.path.join('images', 'gameImage.png'))

# Set up the bot
bot_image = pygame.image.load(os.path.join('images', 'amogus.png'))
bot_rect = bot_image.get_rect(center=(screen_width / 2, screen_height / 2))

bot_speed_x = 0
bot_speed_y = 0

bot_accel_x = 0.5
bot_accel_y = 0.5

max_speed_x = 10
max_speed_y = 7

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the bot
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bot_speed_x -= bot_accel_x
    if keys[pygame.K_RIGHT]:
        bot_speed_x += bot_accel_x
    if keys[pygame.K_UP]:
        bot_speed_y -= bot_accel_y
    if keys[pygame.K_DOWN]:
        bot_speed_y += bot_accel_y
        
    # Clamp the bot's speed to the maximum speed
    bot_speed_x = max(-max_speed_x, min(bot_speed_x, max_speed_x))
    bot_speed_y = max(-max_speed_y, min(bot_speed_y, max_speed_y))
    
    # Update the bot's position
    bot_rect.move_ip(bot_speed_x, bot_speed_y)

    # Draw the screen
    screen.fill((255, 255, 255))
    screen.blit(target_image, (screen_width / 2 - target_image.get_width() / 2, screen_height / 2 - target_image.get_height() / 2))
    screen.blit(bot_image, bot_rect)
    pygame.display.flip()
    
    clock.tick(fps) # limit FPS

# Clean up Pygame
pygame.quit()