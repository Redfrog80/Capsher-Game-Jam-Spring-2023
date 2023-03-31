import pygame
import os
import random

# Initialize pygame
pygame.init()

# Set the screen size
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the font and font size
font = pygame.font.SysFont("Libra", 24)

class Text:                         # defines a text spawner class
    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y
        self.alpha = 255
        self.surface = font.render(text, True, (255, 255, 255))

    def update(self, dt):
        self.alpha = max(self.alpha - dt * 1.5*51, 0)
        self.surface.set_alpha(self.alpha)

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def is_faded(self):
        return self.alpha == 0

plot_text = [                       # defines a list of text
    "WASD to move",
    "Mouse to aim",
    "Click to fire",
    "(This is when enemies spawn)",
    "<<KILL THEM>>",
    "<<GET TO THE QUEEN>>",
    "<<PROTECT HUMANITY>>",
    "hey kiddo",
    "There’s something you should know",
    "i’m not a hero",
    "(This is when QUEEN spawns)",
    "and they're not monsters",
    "<<DIE>>",
    "(player kills QUEEN)",
    "<<MURDERER>>",
    "but i killed them all",
    "i didn't know it was genocide",
    "i didn't know they would all die",
    "BUT THE EMPEROR KNEW",
    "my son. i’m not the hero you think i am",
    "there’s something I need to do",
    "(This is when EMPEROR spawns in front of the player)",
    "(player kills EMPEROR)",
    "(if player runs into EMPEROR, kill both immediately)",
    "turns out we're the monsters",
    "see ya round, kid (explodes)",
]



text_index = 0
text_objects = []

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if text_index < len(plot_text):
                text = plot_text[text_index]
                x = random.randint(0, screen_width - font.size(text)[0])
                y = random.randint(0, screen_height - font.size(text)[1])
                text_objects.append(Text(text, x, y))
                text_index += 1


    screen.fill((0, 0, 0))
    dt = clock.tick(60) / 1000
    for text_object in text_objects:
        text_object.update(dt)
        text_object.draw(screen)
    text_objects = [text_object for text_object in text_objects if not text_object.is_faded()]
    pygame.display.flip()

pygame.quit()