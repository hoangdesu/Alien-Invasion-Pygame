import pygame as pg
import sys

from settings import Settings
from ship import Ship
import functions as funcs
from pygame.sprite import Group

def main():
    pg.init()
    
    game_settings = Settings() # create an object from a class
    
    screen = pg.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pg.display.set_caption("Alien Invader")
    # print("SCREENWIDTH:" , screen.get_width())
    
    spaceShip = Ship(screen, game_settings)
    bullets = Group()

    aliens = Group()
    funcs.create_fleet(screen, game_settings, aliens, spaceShip)
    
    # main game loop
    while True:
        funcs.check_input_events(spaceShip, game_settings, screen, bullets)
        spaceShip.update()
        funcs.update_bullets(bullets, aliens, game_settings, screen, spaceShip)
        funcs.update_fleet(game_settings, aliens)
        funcs.update_screen(screen, game_settings, spaceShip, bullets, aliens)


if __name__ == '__main__':    
    main()