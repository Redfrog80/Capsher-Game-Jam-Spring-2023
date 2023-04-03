import random
import pygame

class SoundEffects:
    def __init__(self):
        self.player_damaged = [pygame.mixer.Sound('sounds/LaserShot1.wav'),
                             pygame.mixer.Sound('sounds/LaserShot3.wav')]
        self.enemy_shot = [pygame.mixer.Sound('sounds/Zap1.wav'),
                           pygame.mixer.Sound('sounds/Zap2.wav'),
                           pygame.mixer.Sound('sounds/Zap3.wav'),
                           pygame.mixer.Sound('sounds/Zap4.wav')]
        self.player_shot = [pygame.mixer.Sound('sounds/boom1.wav'),
                            pygame.mixer.Sound('sounds/boom2.wav'),
                            pygame.mixer.Sound('sounds/boom3.wav'),
                            pygame.mixer.Sound('sounds/boom4.wav')]
        self.glitch_sound = pygame.mixer.Sound('sounds/Glitch_downshifter.wav')
        self.player_death_sounds = [pygame.mixer.Sound('sounds/Death1.wav'),
                                    pygame.mixer.Sound('sounds/Death2.wav')]
        self.enemy_death_sounds = [pygame.mixer.Sound('sounds/enemy_death1.wav'),
                                   pygame.mixer.Sound('sounds/enemy_death2.wav'),
                                   pygame.mixer.Sound('sounds/enemy_death3.wav'),
                                   pygame.mixer.Sound('sounds/enemy_death4.wav')]
        self.alert_sound = pygame.mixer.Sound('sounds/SynthAlert.wav')
        self.UI_sound = pygame.mixer.Sound('sounds/UIClick.wav')
        self.queen_spawn_sound = pygame.mixer.Sound('sounds/Tension2.wav')
        self.emperor_spawn_sound = pygame.mixer.Sound('sounds/Tension3.wav')
        
        self.player_damaged.set_volume(1) # not sure
        self.enemy_shot.set_volume(1) # enemy shots
        self.player_shot.set_volume(1) # player shots
        self.glitch_sound.set_volume(1) 
        self.player_death_sounds.set_volume(1)
        self.enemy_death_sounds.set_volume(1)
        self.alert_sound.set_volume(1)
        self.UI_sound.set_volume(1)

    def play_laser_sound(self):
        sound = random.choice(self.laser_sounds)
        sound.play()

    def play_zap_sound(self):
        sound = random.choice(self.zap_sounds)
        sound.play()

    def play_boom_sound(self):
        sound = random.choice(self.boom_sounds)
        sound.play()

    def play_glitch_sound(self):
        self.glitch_sound.play()

    def play_player_death_sound(self):
        sound = random.choice(self.player_death_sounds)
        sound.play()

    def play_enemy_death_sound(self):
        sound = random.choice(self.enemy_death_sounds)
        sound.play()

    def play_alert_sound(self):
        self.alert_sound.play()

    def play_UI_sound(self):
        self.UI_sound.play()

    def dissonant_music():
        pygame.mixer.music.load("sounds/loading_screen.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1)
        
    def Battle_Music():
        pygame.mixer.music.load("sounds/battle_music.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1)
    
    def pauseMusic():
        pygame.mixer.music.pause()
        
"""
        
TO PLAY SOUNDS: 

from sound_class import SoundEffects
pygame.mixer.init
sound_effects = SoundEffects()

sound_effects.play_laser_sound()


"""