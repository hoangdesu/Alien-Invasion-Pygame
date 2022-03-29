import pygame
from constants import *

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

        self.normal_score, self.normal_score_rect = self.render_score(SCORE_TYPES_NORMAL)
        self.high_score, self.high_score_rect = self.render_score(SCORE_TYPES_HIGHSCORE)
        
    # render the score from TEXT to IMAGE
    def render_score(self, score_type):
        # rounded_score = int(round(self.game_stats.score, -1)) round the number to the nearest ten-th (123 -> 120)

        rounded_score = int(self.game_stats.score)
        if score_type == SCORE_TYPES_HIGHSCORE:
            rounded_score = int(self.game_stats.high_score)
            
        # score = "{:,}".format(rounded_score)
        score = self.format_number(rounded_score)
        rendered_score = self.font.render(score, True, self.text_color, self.bg_color)
        
        score_rect = rendered_score.get_rect()
        score_rect.top = 10
        
        if score_type == SCORE_TYPES_NORMAL:
            score_rect.left = self.screen_rect.left + 10
        elif score_type == SCORE_TYPES_HIGHSCORE:
            score_rect.right = self.screen_rect.right - 10
        
        print("[RENDERED SCORE]", score)
        return rendered_score, score_rect
        
    def draw(self):
        self.screen.blit(self.normal_score, self.normal_score_rect)
        self.screen.blit(self.high_score, self.high_score_rect)
    
    def format_number(self, num):
        num_str = str(num)
        result = ""
        ctr = 1
        for i in range(len(num_str) - 1, -1, -1):
            result = num_str[i] + result
            if ctr % 3 == 0 and i != 0:
                result = "," + result
            ctr += 1
            
        return result


        

        