from audioop import mul
import pygame
from pygame.locals import *
from math import *
# This is somewhat cursed, but it will let me run a __main__ file from anywhere in the python path
if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from lib.misc import *
        from lib.objects import *
    else:
        from ..lib.misc import *
        from ..lib.objects import *

from gameWorld import gameWorld
from player_controller import player_controller

pygame.init()

# initializer

window_dim, tile_dim = (800,800), (100,100)
screen = pygame.display.set_mode(window_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0)
pygame.display.set_caption("test")

# render setting
FPS = 120
clock = pygame.time.Clock()

camera = Camera("camera", (0, 0), size = screen.get_size())

world = gameWorld(pygame.Rect(-100000, -100000,100000,100000),tile_dim,camera)

player = Player("player", (0, 0), (64, 64), screen.get_size(), img="resources/images/player1.png");
player.setTextureSize((50,50))
player.setStat(100,100,100,100,1000,100,200)

controller = player_controller(player, world)

world.add_game_object("Player",player)

world.set_tracked_object("Player", "player")

for i in range(10):
    enemy = Enemy(str(i), (i*1%2000, 200), (0, 0), img = "resources/images/enemy1.png")
    enemy.setTextureSize((10,10))
    enemy.setStat(0, 100, 50, 0, 1000, 100, 200)
    enemy.follow_config(player,500, 0.9, 100)
    world.add_game_object("enemy",enemy)

run = True
while run:
    dt = clock.tick(FPS)/1000
    

    
    screen.fill((5, 5, 15))
    
    run = controller.update_player(dt)
    world.render_tile_map(screen)
    world.render(screen)
    
    world.update(dt)
    
    pygame.display.flip()
    
pygame.quit()

