# Store all settings for the game in a separate file

import pygame as pg
class Settings():
    def __init__(self):
        
        # Settings for the screen
        self.screen_width = 900
        self.screen_height = 600
        self.background_color = (200, 200, 200) # gray-ish color
        self.background = pg.image.load('./assets/background.jpeg')
    
        # Spaceship settings
        self.space_ship_speed = 0
        self.space_ship_lives = 3
        
        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 80, 80, 80
        self.bullets_max_allowed = 10
        
        # Alien settings
        self.alien_speed = 0
        self.fleet_direction = 1  # 1 = right,  -1 = left
        self.fleet_dropdown_speed = 10

        # Score
        self.alien_points = 5

        # How much the game speeds up (20%)
        self.speedup_factor = 1.2
        
        self.reset_dynamic_settings()
        
        
    def reset_dynamic_settings(self):
        self.space_ship_speed = 10
        self.bullet_speed = 5
        self.alien_speed = 1.5
        self.fleet_direction = 1
        
        
    def increase_speed(self):
        self.space_ship_speed *= self.speedup_factor
        self.bullet_speed *= self.speedup_factor
        self.alien_speed *= self.speedup_factor # == self.alien_speed = self.alien_speed * self.speedup_factor
