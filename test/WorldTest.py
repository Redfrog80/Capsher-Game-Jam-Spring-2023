from lib import objects
import pygame


pygame.init()

# initializer
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Bug shooter")

# render setting
FPS = 60
clock = pygame.time.Clock()

camera = objects.Camera("cam", (0, 0), win.get_size())
firstObject = objects.GameObject("dummy", (400, 400), (0, 0))
firstObject.matchBoundaryToTexture()
# secondObject = objects.GameObject("player", (100, 100), (0, 0),)
# secondObject.matchBoundaryToTexture()
# secondObject.vel = (200, 200)

player = objects.Player("player", (0, 0), (64, 64), "resources/images/ship.png")
player.matchTextureToBoundary()
player.speedMax = 500
player.rotspeedMax = 360
# camera track second object
camera.trackCenter(player)

updateList = [player, firstObject]

run = True
while run:
    dt = clock.tick(FPS)/1000
    # get and analyze pygame event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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
                updateList.append(player.shoot())
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
    [i.update(dt) for i in updateList]
    camera.update()
    # render
    win.fill((255, 255, 255))
    [i.render(win, camera) for i in updateList]

    pygame.display.update()
pygame.quit()

