import random
import pygame
from pygame.locals import *
from math import *
import random
from sound_class import SoundEffects

# This is somewhat cursed, but it will let me run a __main__ file from anywhere in the python path
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path

        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from lib.objects import *
        from lib import enemy
    else:
        from ..lib.objects import *
        from ..lib import enemy

from gameWorld import GameWorld
from playercontroller import PlayerController

pygame.init()
pygame.mixer.init()

# initializer

window_dim, tile_dim = (800, 800), (100, 100)
game_dim = (800, 800)

game_screen = pygame.display.set_mode(game_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0).copy()
window_screen = pygame.display.set_mode(window_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0)
pygame.display.set_caption("test")

# render setting
FPS = 120
clock = pygame.time.Clock()

camera = Camera("camera", (0, 0), size=game_screen.get_size())

world = GameWorld(pygame.Rect(0, 0, 2000, 2000), tile_dim, game_screen, window_screen.get_size(), camera)
# world.debug_title_map = True
player = Player("player", (1000, 1000), (48, 48), game_screen.get_size(), img="resources/images/player1.png")
player.setTextureSize((64, 64))
print(player.boundary)

player.setStat(100, 100, 100, 100, 500, 500, 300)

controller = PlayerController(player, world)

world.add_game_object("Player", player)

world.set_tracked_object("Player", 100)

start_screen = True # Click to play game
while start_screen:
    game_screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_screen = False                    # ends start screen
    
    start_image = pygame.image.load("resources/images/click_to_start.png").convert()
 
    # Using blit to copy content from one surface to other
    window_screen.blit(start_image, (0, 0))

for i in range(10):
    newEnemy = enemy.Assault("a_" + str(i), (random.randint(0, 2000), random.randint(0, 2000)), (48, 48),
                             img="resources/images/enemy2.png")
    newEnemy.setTextureSize((64, 64))
    newEnemy.setStat(0, 100, 50, 0, 100, 150, 1000)
    newEnemy.follow_config(player, 800, 1, 400)
    world.add_game_object("enemy", newEnemy)

for i in range(20):
    newEnemy = enemy.Kamikaze("k_" + str(i), (random.randint(0, 2000), random.randint(0, 2000)), (48, 48),
                             img="resources/images/enemy3.png")
    newEnemy.setTextureSize((48, 48))
    newEnemy.setStat(0, 0, 20, 20, 150, 300, 1000)
    newEnemy.follow_config(player, 800, 1, 0)
    world.add_game_object("enemy", newEnemy)

for i in range(10):
    newEnemy = enemy.Juggernaut("j_" + str(i), (random.randint(0, 2000), random.randint(0, 2000)), (48, 48),
                             img="resources/images/enemy4.png")
    newEnemy.setTextureSize((80, 80))
    newEnemy.setStat(0, 100, 50, 0, 50, 50, 1000)
    newEnemy.follow_config(player, 800, 1, 200)
    world.add_game_object("enemy", newEnemy)

SoundEffects.Battle_Music()

run = True
while run:
    # background -- maybe move to game world render
    game_screen.fill((5, 5, 15))
    # print(player.shield, player.health)
    world.render()

    dt = clock.tick(FPS) / 1000

    run = controller.update_player(dt)
    world.update(dt)
    # world.render_tile_map()
    # print(player.pos)

    window_screen.blit(pygame.transform.scale(game_screen, window_dim), (0, 0))

    pygame.display.flip()

pygame.quit()
