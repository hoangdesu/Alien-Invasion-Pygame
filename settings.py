# Store all settings for the game in a separate file

class Settings():
    def __init__(self):
        
        # Settings for the screen
        self.screen_width = 900
        self.screen_height = 600
        self.background_color = (200, 200, 200) # gray-ish color
    
        # Spaceship settings
        self.space_ship_speed = 5
        self.space_ship_lives = 2
        
        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 80, 80, 80
        self.bullets_max_allowed = 10
        
        # Alien settings
        self.alien_speed = 1
        self.fleet_direction = 1  # 1 = right,  -1 = left
        self.fleet_dropdown_speed = 30

