import json

class Stats:
    def __init__(self, game_settings):
        self.game_settings = game_settings
        self.game_over = False
        self.score = 0
        self.high_score = 0
        self.level = 1
        
        self.reset_statistics()
        self.read_high_score()
    
    def reset_statistics(self):
        self.ship_lives = self.game_settings.space_ship_lives
<<<<<<< HEAD
=======
        self.score = 0
        self.level = 1
>>>>>>> fa5ffa80
        
    def read_high_score(self):
        try:
            with open('./data.json') as file:
                data = json.load(file) # dictionary!!!
                self.high_score = int(data["high_score"])
                file.close()
            
            # same stuff
            # big_str = file.read()
            # data = json.loads(big_str)
            # print('[player name]:',data["player"])    
        except FileNotFoundError:
            print("File not found")
        except:
            print("Error")
        