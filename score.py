import pygame
from constants import *

class Score():
    def __init__(self, game_settings, screen, game_stats):
        self.game_settings = game_settings
        self.screen = screen
        self.game_stats = game_stats
        self.screen_rect = screen.get_rect()
        self.gap = 10
        
        # font settings for the score
        self.text_color = (50, 50, 50)
        self.bg_color = (200, 200, 200)
        self.font = pygame.font.Font(None, 40)

        self.render_level()
        self.render_score(SCORE_TYPES_NORMAL)
        self.render_score(SCORE_TYPES_HIGHSCORE)
        
        
    # render the score from TEXT to IMAGE
    def render_score(self, score_type):
        # rounded_score = int(round(self.game_stats.score, -1)) round the number to the nearest ten-th (123 -> 120)
                        
        if score_type == SCORE_TYPES_NORMAL:
            rounded_score = int(self.game_stats.score)
            score = self.format_number(rounded_score)
            self.normal_score = self.font.render(score, True, self.text_color, self.bg_color)
            self.normal_score_rect = self.normal_score.get_rect()
            self.normal_score_rect.top = self.gap
            self.normal_score_rect.left = self.screen_rect.left + self.gap
            
        elif score_type == SCORE_TYPES_HIGHSCORE:
            rounded_score = int(self.game_stats.high_score)
            score = self.format_number(rounded_score)
            self.high_score = self.font.render(score, True, self.text_color, self.bg_color)
            self.high_score_rect = self.high_score.get_rect()
            self.high_score_rect.top = self.gap
            self.high_score_rect.right = self.screen_rect.right - self.gap
            
        
    def draw(self):
        self.screen.blit(self.normal_score, self.normal_score_rect)
        self.screen.blit(self.high_score, self.high_score_rect)
        self.screen.blit(self.rendered_level, self.level_rect)
    
    
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


    def render_level(self):
        msg = f"Level: {self.game_stats.level}"
        self.rendered_level = self.font.render(msg, True, self.text_color, self.bg_color)
        self.level_rect = self.rendered_level.get_rect()
        self.level_rect.left = self.gap
        self.level_rect.top = self.gap + 50
        

        

        