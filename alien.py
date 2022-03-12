import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    # just for one alien

    def __init__(self, screen, game_settings):
        super(Alien, self).__init__()      # super: takes parent constructor
        self.screen = screen
        self.game_settings = game_settings

        self.image = pg.image.load('./assets/alien.png')
        self.scale_factor = 6
        self.image = pg.transform.scale(self.image, (self.image.get_width() // self.scale_factor , self.image.get_height() // self.scale_factor))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        

    def check_collide_with_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right: # right border
            return True
        elif self.rect.left < 0: # left border
            return True

    
    def update(self):
        self.x += self.game_settings.alien_speed * self.game_settings.fleet_direction
        self.rect.x = self.x
        # print("[SELF.RECT.RIGHT]:", self.rect.right, " -- [SCREEN RECT RIGHT]:", self.screen.get_rect().right)
        

    def draw(self):
        self.screen.blit(self.sprite, self.rect)
        self.screen.blit(self.rect, self.rect)
        
        


