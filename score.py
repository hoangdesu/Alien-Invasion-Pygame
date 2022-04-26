import pygame as pg
from constants import *
from pygame.sprite import Group
from ship import Ship

class Score():
    def __init__(self, game_settings, screen, game_stats):
        self.game_settings = game_settings
        self.screen = screen
        self.game_stats = game_stats
        self.screen_rect = screen.get_rect()
        self.gap = 10
        self.heart = pg.image.load('./assets/heart.png')
        self.heart_scale_down_factor = 45
        self.heart = pg.transform.scale(
            self.heart,
            (self.heart.get_width() // self.heart_scale_down_factor, self.heart.get_height() // self.heart_scale_down_factor)
        )
        # font settings for the score
        self.text_color = (50, 50, 50)
        self.bg_color = (200, 200, 200)
        self.font = pg.font.Font(None, 40)

        self.render_score(SCORE_TYPES_NORMAL)
        self.render_score(SCORE_TYPES_HIGHSCORE)
        self.render_level()
        self.render_lives()
        
        
    # render the score from TEXT to IMAGE
    def render_score(self, score_type):
        # rounded_score = int(round(self.game_stats.score, -1)) round the number to the nearest ten-th (123 -> 120)
                        
        if score_type == SCORE_TYPES_NORMAL:
            rounded_score = int(self.game_stats.score)
            score = "Score: " + self.format_number(rounded_score)
            self.normal_score = self.font.render(score, True, self.text_color, self.bg_color)
            self.normal_score_rect = self.normal_score.get_rect()
            self.normal_score_rect.top = self.gap
            self.normal_score_rect.left = self.screen_rect.left + self.gap
            
        elif score_type == SCORE_TYPES_HIGHSCORE:
            rounded_score = int(self.game_stats.high_score)
            score = "High score: " + self.format_number(rounded_score)
            self.high_score = self.font.render(score, True, self.text_color, self.bg_color)
            self.high_score_rect = self.high_score.get_rect()
            self.high_score_rect.top = self.gap
            self.high_score_rect.right = self.screen_rect.right - self.gap
            
        
    def draw(self):
        self.screen.blit(self.normal_score, self.normal_score_rect)
        self.screen.blit(self.high_score, self.high_score_rect)
        self.screen.blit(self.rendered_level, self.level_rect)
        # self.ships.draw(self.screen)
        self.render_lives()
    
    
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
        msg = "Level: " + str(self.game_stats.level)
        self.rendered_level = self.font.render(msg, True, self.text_color, self.bg_color)
        self.rendered_level_rect = self.rendered_level.get_rect()
        self.rendered_level_rect.left = self.gap
        self.rendered_level_rect.top = self.gap


    def render_level(self):
        msg = f"Level: {self.game_stats.level}"
        self.rendered_level = self.font.render(msg, True, self.text_color, self.bg_color)
        self.level_rect = self.rendered_level.get_rect()
        self.level_rect.left = self.gap
        self.level_rect.top = self.normal_score_rect.bottom + self.gap
        

    def render_lives(self):
        # // use this to render ship sprite 
        # self.ships = Group()
        # for i in range(self.game_stats.ship_lives):
        #     ship = Ship(self.screen, self.game_settings)
        #     ship.rect.x = self.gap + (ship.rect.width * i)
        #     ship.rect.y = self.gap
        #     self.ships.add(ship)
        
        for i in range(1, self.game_stats.ship_lives + 1):
            heart_rect = self.heart.get_rect()
            heart_rect.x = self.screen_rect.right - ((heart_rect.width + self.gap) * i)
            heart_rect.y = self.high_score_rect.bottom + self.gap
            self.screen.blit(self.heart, heart_rect)
        