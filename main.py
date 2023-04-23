import pygame
from lib.misc import *
from lib.managers import *
from lib.objects import *
from lib.enemy import *
from lib.world import GameWorld
from lib.world import EventController

# window initializer
a, b, c= 10, 4, (192,108)
window_dim = [i*a for i in c]
game_dim = [i*b for i in c]

pygame.init()
game_screen = pygame.display.set_mode(game_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED, vsync=0).copy()
window_screen = pygame.display.set_mode(window_dim, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED |pygame.FULLSCREEN, vsync=0)

# world and render setting
FPS = 120
clock = pygame.time.Clock()

image_dict = imageDict()
# player
player = Player(pos = (2000, 2000))
player.setStat(150, 150, 250, 250, 500, 500, 360)

world = GameWorld(dimensions = pygame.Rect(0, 0, 4000, 4000),
                  screen = game_screen,
                  mouse_area = window_screen.get_size(), 
                  player = player,
                  image_dict = image_dict)
# world.debug_title_map = True

controller = EventController(player, world)

# world add obj and event
world.add_game_object(player)
world.set_tracked_object(player, 40)

controller.addEventSpawn(3, 50, (1, 2), Assault, ENEMY_TAG)
controller.addEventSpawn(3, 50, (1, 5), Kamikaze, ENEMY_TAG)
controller.addEventSpawn(6, 25, (1, 4), Juggernaut, ENEMY_TAG)

run = True
while run:
    # update
    dt = clock.tick(FPS) / 1000
    run = controller.update_events(dt)
    
    game_screen.fill((5, 5, 15))  # background
    # render
    world.render()

    world.update(dt)
    # draw on screen
    window_screen.blit(pygame.transform.scale(game_screen, window_dim), (0, 0))
    pygame.display.flip()

pygame.quit()
