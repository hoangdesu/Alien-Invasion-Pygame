import json

class Stats:
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.game_over = False
        self.score = 0
        self.high_score = 0 # (read from the json file)
        
        self.reset_statistics()
        self.read_high_score()
    
    def reset_statistics(self):
        self.ship_lives = self.game_settings.space_ship_lives
        self.score = 0
        
    def read_high_score(self):
        with open('./data.json') as file:
            data = json.load(file)
            print(data["high_score"])
        

        