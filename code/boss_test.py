import pygame
import math
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Boss Demo")
background = pygame.Color("black")

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 50))
        self.image.fill(pygame.Color("red"))
        self.rect = self.image.get_rect(center=(400, 50))
        self.health = 100
        self.max_health = 100
        self.speed = 3
        self.direction = 1
        self.shoot_delay = 500
        self.last_shot = pygame.time.get_ticks()
        
    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.right > 800 or self.rect.left < 0:
            self.direction *= -1
            print("moved")
        
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.bottom, player.rect.center)
            all_sprites.add(bullet)
            bullets.add(bullet)
            print("added bullet")
    
    def draw_health_bar(self):
        pygame.draw.rect(screen, pygame.Color("green"), (self.rect.x, self.rect.y - 10, int(self.health / self.max_health * self.rect.width), 5))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, player_pos):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(pygame.Color("white"))
        self.rect = self.image.get_rect(center=(x, y + 50))  # Add 50 to y-coordinate
        self.speed = 1
        self.player_pos = player_pos
        
    def update(self):
        dx = self.player_pos[0] - self.rect.centerx
        dy = self.player_pos[1] - self.rect.centery
        angle = math.atan2(dy, dx)
        
        self.rect.x += self.speed * math.cos(angle)
        self.rect.y += self.speed * math.sin(angle)

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
boss_group = pygame.sprite.Group()

player = pygame.sprite.Sprite()
player.image = pygame.Surface((50, 50))
player.image.fill(pygame.Color("blue"))
player.rect = player.image.get_rect(center=(400, 300))
all_sprites.add(player)

boss = Boss()
boss_group.add(boss)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    boss.update()
    all_sprites.update()
    bullets.update()

    hits = pygame.sprite.groupcollide(bullets, boss_group, True, False)
    for bullet, bosses in hits.items():
        boss.health -= 5
        print("Boss hit!")

    hits = pygame.sprite.spritecollide(player, bullets, True)
    if hits:
        print("Player hit!")

    for bullet in bullets.copy():
        if bullet.rect.bottom < 0 or bullet.rect.top > 600 or bullet.rect.right < 0 or bullet.rect.left > 800:
            bullet.kill()

    # Draw sprites
    screen.fill(background)
    boss.draw_health_bar()
    all_sprites.draw(screen)
    boss_group.draw(screen)
    bullets.draw(screen)
    pygame.display.flip()