import pygame
from pygame.locals import *
from lib.objects import *
from lib.world.GameWorld import GameWorld


class EventController:
    """
    use to handle player input and world event
    """
    def __init__(self, player_object: Player, game_world: GameWorld) -> None:
        self.extraEventList = {}
        self.player = player_object
        self.world = game_world
        self.run = True
        self.bullet_num = 0
        self.shooting = False
        self.player.gun.firerate = 0.2

    def update_events(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == KEYDOWN:
                if event.key == K_w:
                    self.player.goForward()
                if event.key == K_s:
                    self.player.goBack()
                if event.key == K_a:
                    self.player.rotateLeft()
                    self.player.trackRot = True
                if event.key == K_d:
                    self.player.rotateRight()
                    self.player.trackRot = True
            if event.type == KEYUP:
                if event.key == K_w:
                    self.player.setAccel((0, 0))
                if event.key == K_s:
                    self.player.setAccel((0, 0))
                if event.key == K_a:
                    self.player.rotvel = 0
                    self.player.trackRot = False
                if event.key == K_d:
                    self.player.rotvel = 0
                    self.player.trackRot = False
            if event.type == MOUSEBUTTONDOWN:
                self.shooting = True
            if event.type == MOUSEBUTTONUP:
                self.shooting = False
            if event.type in self.extraEventList:
                data = self.extraEventList[event.type]
                data[0](data[1], data[2], data[3], data[4])

        if self.shooting and self.player.liveflag:
            bullet = self.player.shoot(dt, "b_" + str(self.bullet_num))
            if bullet:
                self.world.add_game_object("player_bullet", bullet)
                self.bullet_num += 1

        return True

    def addEventSpawn(self, time, chance, num_range, obj_class, tag):
        """
        :param time: time occur in s
        :param chance: probability of something happen 0 - 1
        :param num_range: tuple: lower and upper bound
        :param obj_class: which class to spawn
        :param tag: obj tag
        """
        newEvent = pygame.USEREVENT + 1
        pygame.time.set_timer(newEvent, time * 1000)
        self.extraEventList.update({newEvent: (self.world.spawnObj, chance, num_range, obj_class, tag)})
