class Stats:
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.reset_statistics()
        self.game_over = False
        self.score = 12873612836
    
    def reset_statistics(self):
        self.ship_lives = self.game_settings.space_ship_lives
        self.score = 0