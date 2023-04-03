import pygame
from pygame.locals import *
from lib.objects import *
from gameWorld import GameWorld


class PlayerController:
    def __init__(self, player_object :Player, game_world : GameWorld) -> None:
        self.player = player_object
        self.world = game_world
        self.run = True
        self.bullet_num = 0
        self.shooting = False
        
        self.player.gun.firerate = 0.1

    def update_player(self, dt):
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
        
        if self.shooting and self.player.liveflag:
            bullet = self.player.shoot(dt, "b_" + str(self.bullet_num))
            if bullet:
                self.world.add_game_object("player_bullet", bullet)
                self.bullet_num += 1

        return True
