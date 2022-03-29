class Stats:
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.game_over = False
        self.score = 0
        self.high_score = 9999999
        
        self.reset_statistics()
    
    def reset_statistics(self):
        self.ship_lives = self.game_settings.space_ship_lives
        self.score = 3218

        