import random
from lib import enemy
import pygame

# This is somewhat cursed, but it will let me run a __main__ file from anywhere in the python path
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path

        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from lib.objects import *
    else:
        from lib.objects import *

from world import GameWorld
from world import EventController

# window initializer
window_dim, tile_dim = (800, 800), (100, 100)
game_dim = (800, 800)

game_screen = pygame.display.set_mode(game_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0).copy()
window_screen = pygame.display.set_mode(window_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0)
pygame.display.set_caption("BuggyShooter")

# world and render setting
FPS = 120
clock = pygame.time.Clock()

camera = Camera("camera", (0, 0), size=game_screen.get_size())
world = GameWorld(pygame.Rect(0, 0, 2000, 2000), tile_dim, game_screen, window_screen.get_size(), camera)
# world.debug_title_map = True

# player
player = Player("player", (1000, 1000), (48, 48), game_screen.get_size(), img="resources/images/player.png")
player.setTextureSize((64, 64))
player.setStat(100, 100, 100, 100, 500, 500, 360)
controller = EventController(player, world)

# world add obj and event
world.add_game_object("Player", player)
world.player = player
world.set_tracked_object("Player", 100)

controller.addEventSpawn(2, 100, (1, 6), enemy.Assault, "enemy")
controller.addEventSpawn(3, 100, (1, 5), enemy.Kamikaze, "enemy")
controller.addEventSpawn(4, 100, (2, 2), enemy.Juggernaut, "enemy")

run = True
while run:
    # update
    dt = clock.tick(FPS) / 1000
    run = controller.update_events(dt)
    world.update(dt)
    # render
    game_screen.fill((5, 5, 15))  # background
    world.render()
    # draw on screen
    window_screen.blit(pygame.transform.scale(game_screen, window_dim), (0, 0))
    pygame.display.flip()

pygame.quit()
