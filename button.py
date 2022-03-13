import pygame as pg

class Button:
    def __init__(self, game_settings, screen, message):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.width, self.height = 200, 50
        self.bg_color = (47, 6, 158)
        self.text_color = (252, 250, 189)
        self.font = pg.font.Font(None, 40)
        
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self.display_message(message)
        
    def display_message(self, message):
        # render the text as image
        self.rendered_msg = self.font.render(
            message,
            True,
            self.text_color,
            self.bg_color
        )
        self.rendered_msg_rect = self.rendered_msg.get_rect()
        self.rendered_msg_rect.center = self.rect.center
        
    def draw(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.rendered_msg, self.rendered_msg_rect)
        
        