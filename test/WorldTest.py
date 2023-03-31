from lib import objects, enemy

import pygame
import random

pygame.init()

# initializer
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Bug shooter")

# render setting
FPS = 60
clock = pygame.time.Clock()

camera = objects.Camera("cam", (0, 0), win.get_size())

player = objects.Player("player", (0, 0), (64, 64), "resources/images/ship.png")
player.matchTextureToBoundary()
player.setStat(0, 200, 100, 0, 100, 500, 360)
# camera track second object
camera.trackCenter(player)


def createEnemy(name, pos, target):
    new_enemy = enemy.Assault(name, pos, (60, 60))
    new_enemy.matchTextureToBoundary()
    new_enemy.setStat(0, 100, 50, 0, 50, 100, 200)
    new_enemy.follow_config(target, 300, .9, 100)
    return new_enemy


def chance(c):
    return random.randint(0, 100) < c


def randDist(obj: objects.GameObject):
    return random.randrange(-300, 300) + obj.pos[0], random.randrange(-300, 300) + obj.pos[1]


# enemy generator
# maxEnemy = 100
# countEnemy = 0
RAND_SPAWN = pygame.USEREVENT+1
pygame.time.set_timer(RAND_SPAWN, 1000)
an_enemy = createEnemy("ee", randDist(player), player)
everything = {player.name: player, an_enemy.name: an_enemy}  # everything

destroylist = []


run = True
while run:
    dt = clock.tick(FPS) / 1000
    # get and analyze pygame event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == RAND_SPAWN and chance(50):  # off
            for i in range(random.randint(0, 3)):
                while True:
                    # prevent overwriting key
                    nametest = "enemy" + str(random.randint(0, 1000))
                    if nametest not in everything:
                        everything.update({nametest: createEnemy(nametest, randDist(player), player)})
                        break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rotateLeft()
            elif event.key == pygame.K_RIGHT:
                player.rotateRight()
            elif event.key == pygame.K_UP:
                player.goForward()
            elif event.key == pygame.K_DOWN:
                player.goBack()
            elif event.key == pygame.K_SPACE:
                while True:
                    # prevent overwriting key
                    nametest = "bullet" + str(random.randint(0, 1000))
                    if nametest not in everything:
                        everything.update({nametest: player.shoot(nametest)})
                        break
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.rotateLeftStop()
            elif event.key == pygame.K_RIGHT:
                player.rotateRightStop()
            elif event.key == pygame.K_UP:
                player.goForwardStop()
            elif event.key == pygame.K_DOWN:
                player.goBackStop()

    # update calculation
    # player.rot += 2
    for key in everything:
        everything[key].update(dt, gameobjs=everything)
    camera.update()
    # destroy object with dead flag
    for key in everything:
        if not everything[key].objAlive():
            print("murder {}".format(key))
            destroylist.append(key)
    for k in destroylist:
        del everything[k]
    destroylist.clear()

    # render
    win.fill((255, 255, 255))
    for key in everything:
        everything[key].render(win, camera)
    camera.update()

    pygame.display.update()
pygame.quit()
