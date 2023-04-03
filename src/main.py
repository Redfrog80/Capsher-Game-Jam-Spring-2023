import pygame
from pygame.locals import *
from math import *
import random
# This is somewhat cursed, but it will let me run a __main__ file from anywhere in the python path
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from lib.misc import *
        from lib.objects import *
        from lib.enemy import *;
    else:
        from ..lib.misc import *
        from ..lib.objects import *
        from ..lib.enemy import *;

from gameWorld import gameWorld
from player_controller import player_controller

pygame.init()

# initializer

window_dim, tile_dim = (800,800), (100,100)
game_dim = (800,800)

game_screen = pygame.display.set_mode(game_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0).copy()
window_screen = pygame.display.set_mode(window_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0)
pygame.display.set_caption("test")

# render setting
FPS = 120
clock = pygame.time.Clock()

camera = Camera("camera", (0, 0), size = game_screen.get_size())

world = gameWorld(pygame.Rect(0,0,2000,2000),tile_dim, game_screen, window_screen.get_size(), camera)

player = Player("player", (1000, 1000), (64, 64), game_screen.get_size(), img="resources/images/player1.png")

player.setStat(100,100,100,100,400,1000,300)

controller = player_controller(player, world)

world.add_game_object("Player",player)

world.set_tracked_object("Player", 200)

for i in range(1):
    enemy = Sentinel("s_"+str(i), 40, (1000, 1000), (40, 40), img = "resources/images/enemy1.png")
    enemy.setStat(0, 100, 50, 0, 100, 200, 1000)
    enemy.follow_config(player,500, 1, 10)
    world.add_game_object("enemy",enemy)

run = True
while run:
    
    game_screen.fill((5, 5, 15))
    
    world.render()
    
    dt = clock.tick(FPS)/1000
    
    run = controller.update_player(dt)
    world.update(dt)
    # world.render_tile_map()
    print(player.pos)
    
    window_screen.blit(pygame.transform.scale(game_screen,window_dim),(0,0))
    
    pygame.display.flip()
    
pygame.quit()

