import pygame as pg
from pygame.sprite import Sprite

# manages all the bullets fired from the ship
class Bullet(Sprite): # inheritance
    def __init__(self, settings, screen, spaceShip):
        super(Bullet, self).__init__() # create a bullet at the ship's current position
        self.screen = screen
        
        self.rect = pg.Rect(0, 0, settings.bullet_width, settings.bullet_height)
        self.rect.centerx = spaceShip.rect.centerx # bullet's x == ship's x
        self.rect.top = spaceShip.rect.top
        
        self.y = float(self.rect.y)
        self.speed = settings.bullet_speed
        self.color = settings.bullet_color
    
    def update(self):
        # bullet will keep flying up the screen at a constant speed
        self.y -= self.speed
        self.rect.y = self.y
        
    def draw(self):
        pg.draw.rect(self.screen, self.color, self.rect)
        