import pygame as pg
import sys
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import functions as funcs
from stats import Stats
from button import Button

def main():
    pg.init()
    
    game_settings = Settings() # create an object from a class
    game_stats = Stats(game_settings)
    
    screen = pg.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pg.display.set_caption("Alien Invasion")
    # print("SCREENWIDTH:" , screen.get_width())
    
    spaceShip = Ship(screen, game_settings)
    bullets = Group()
    aliens = Group()
    funcs.create_fleet(screen, game_settings, aliens, spaceShip)
    play_btn = Button(game_settings, screen, "Play!")
    
    # main game loop
    while True:
        funcs.check_input_events(spaceShip, game_settings, screen, bullets, aliens, game_stats, play_btn)
        
        if game_stats.game_over == False:
            spaceShip.update()
            funcs.update_bullets(bullets, aliens, game_settings, screen, spaceShip)
            funcs.update_fleet(game_settings, screen, game_stats, aliens, spaceShip, bullets)
            funcs.update_screen(screen, game_settings, game_stats, spaceShip, bullets, aliens, play_btn)

if __name__ == '__main__':    
    main()