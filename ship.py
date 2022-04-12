import pygame as pg
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen, settings):
        super(Ship, self).__init__()
        self.screen = screen
        self.settings = settings
        
        self.sprite = pg.image.load('./assets/spaceship.png')
        self.scale_factor = 10
        self.sprite = pg.transform.scale(self.sprite, (self.sprite.get_width() // self.scale_factor , self.sprite.get_height() // self.scale_factor))
        self.rect = self.sprite.get_rect()
        self.screen_rect = self.screen.get_rect()
        
        self.isMovingRight = False
        self.isMovingLeft = False
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 5
        
        
    def update(self):
        if self.isMovingRight and (self.rect.right < self.screen_rect.right):
            self.rect.centerx += self.settings.space_ship_speed
        if self.isMovingLeft and (self.rect.left > self.screen_rect.left):
            self.rect.centerx -= self.settings.space_ship_speed
        
    
    def draw(self):
        self.screen.blit(self.sprite, self.rect)

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx