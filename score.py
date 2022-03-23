import pygame

class Score():
    def __init__(self, game_settings, screen, game_stats):
        self.game_settings = game_settings
        self.screen = screen
        self.game_stats = game_stats
        self.screen_rect = screen.get_rect()
        
        # font settings for the score
        self.text_color = (50, 50, 50)
        self.bg_color = (200, 200, 200)
        self.font = pygame.font.Font(None, 48)

        self.render_score()
        
    # render the score from TEXT to IMAGE
    def render_score(self):
        rounded_score = int(round(self.game_stats.score, -1))
        # score = "{:,}".format(rounded_score)
        score = self.format_score(rounded_score)
        self.rendered_score = self.font.render(score, True, self.text_color, self.bg_color)
        
        self.score_rect = self.rendered_score.get_rect()
        self.score_rect.left = self.screen_rect.left + 10
        self.score_rect.top = 10
        
    def draw(self):
        self.screen.blit(self.rendered_score, self.score_rect)
    
    def format_score(self, score):
        score_str = str(score)
        formatted_score = ''
        counter = 0
        for i in range(len(score_str) - 1, -1, -1):
            # if counter % 3 == 0:
            
                
        
        
        return formatted_score
        
        