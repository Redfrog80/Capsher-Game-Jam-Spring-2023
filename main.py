import pygame
import threading
from lib.managers import soundDict
from lib.misc import *
from lib.managers import *
from lib.objects import *
from lib.enemy import *
from lib.world import GameWorld
from lib.world import EventController

# window initializer
a, b, c= 10, 6, (192,108)
window_dim = [i*a for i in c]
game_dim = [i*b for i in c]
tile_dim = scalar_floor_div(game_dim, b*5)

pygame.init()
game_screen = pygame.display.set_mode(game_dim, flags= pygame.SCALED, vsync=0).copy()
window_screen = pygame.display.set_mode(window_dim, flags= pygame.SCALED | pygame.FULLSCREEN, vsync=1)

# world and render setting
FPS = 120
clock = pygame.time.Clock()

image_dict = imageDict()
image_dict.load_images()

sound_dict = soundDict()
sound_dict.load_sounds()
# player
player = Player(pos = (2000, 2000), image_dict = image_dict, sound_dict = sound_dict)

world = GameWorld(dimensions = pygame.Rect(0, 0, 4000, 4000),
                  screen = game_screen,
                  tile_dim = tile_dim,
                  mouse_area = window_screen.get_size(), 
                  image_dict = image_dict,
                  sound_dict = sound_dict,
                  debug = False)

controller = EventController(player, world)

# world add obj and event
world.set_player(player)
world.set_tracked_object(player, 40)

controller.addEventSpawn(5, 50, (1, 2), Assault, ENEMY_TAG)
controller.addEventSpawn(3, 50, (1, 3), Kamikaze, ENEMY_TAG)
# controller.addEventSpawn(6, 25, (1, 2), Juggernaut, ENEMY_TAG)

run = True
test = 0
while run:
    # update
    dt = clock.tick(FPS) / 1000
    c = pygame.Color(5,5,15,1)
    game_screen.fill(c)  # background
    # render
    t1 = threading.Thread(target = world.update, args=(dt,)).run()
    t2 = threading.Thread(target = world.render, args=()).run()
    if t1:
        t1.join()
    if t2:
        t2.join()
    run = controller.update_events(dt)
    
    # draw on screen
    window_screen.blit(pygame.transform.scale(game_screen, window_dim), (0, 0))
    pygame.display.flip()

pygame.quit()
