import pygame as pg
import sys
from pygame.sprite import Group
from constants import *

from settings import Settings
from ship import Ship
import functions as funcs
from stats import Stats
from button import Button
from score import Score
from sound import Sound

def main():
    sound = Sound()
    pg.init()
    
    clock = pg.time.Clock()
    game_settings = Settings() # create an object from a class
    game_stats = Stats(game_settings)
    
    screen = pg.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pg.display.set_caption("Alien Invasion")
    
    spaceShip = Ship(screen, game_settings)
    bullets = Group()
    aliens = Group()
    
    funcs.create_fleet(screen, game_settings, aliens, spaceShip)
    play_btn = Button(game_settings, screen, "Play!")
    score = Score(game_settings, screen, game_stats)
    
    pg.mouse.set_visible(False)
    
    # sound.bgm.play(loops=-1)
    pg.mixer.Channel(0).play(sound.bgm, -1)
    
    
    
    font = pg.font.Font(None, 40)
    font_img = font.render("WELCOME", True, (50, 50, 50), (200, 200, 200))
    
    # main game loop
    while True:
        funcs.check_input_events(spaceShip, game_settings, screen, bullets, aliens, game_stats, play_btn, score, sound)
        
        if game_stats.game_state == GAME_STATE_MENU:
            screen.fill((100, 100, 100))
            screen.blit(font_img, (200, 200))
            pg.display.flip()
        
        elif game_stats.game_state == GAME_STATE_PLAY:
            if game_stats.game_over == False:
                spaceShip.update()
                funcs.update_bullets(bullets, aliens, game_settings, screen, spaceShip, game_stats, score, sound)
                funcs.update_fleet(game_settings, screen, game_stats, aliens, spaceShip, bullets, score)
                funcs.update_screen(screen, game_settings, game_stats, spaceShip, bullets, aliens, play_btn, score)
            
        clock.tick(60)
        

if __name__ == '__main__':    
    main()

    