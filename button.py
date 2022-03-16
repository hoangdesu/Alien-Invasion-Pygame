import pygame.font

class Button():
    def __init__(self, game_settings, screen, message):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.width, self.height = 200, 50
        self.bg_color = (30, 52, 166)
        self.text_color = (255, 255, 161)
        self.font = pygame.font.Font(None, 50)
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self.prep_msg(message)
        
    def prep_msg(self, msg):
        self.rendered_msg = self.font.render(msg, True, self.text_color, self.bg_color)
        self.rendered_msg_rect = self.rendered_msg.get_rect()
        self.rendered_msg_rect.center = self.rect.center
        
    def draw(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.rendered_msg, self.rendered_msg_rect)
