import sys
from zoneinfo import available_timezones
import pygame as pg

from bullet import Bullet
from alien import Alien

# helper functions
def check_keydown_events(event, spaceShip, settings, screen, bullets):
    if event.key == pg.K_RIGHT:
        spaceShip.isMovingRight = True
    elif event.key == pg.K_LEFT:
        spaceShip.isMovingLeft = True
    elif event.key == pg.K_SPACE:
        if len(bullets) < settings.bullets_max_allowed:
            new_bullet = Bullet(settings, screen, spaceShip)
            bullets.add(new_bullet)
    elif event.key == pg.K_ESCAPE:
        sys.exit()
    
def check_keyup_events(event, spaceShip):
    if event.key == pg.K_RIGHT:
        spaceShip.isMovingRight = False
    elif event.key == pg.K_LEFT:
        spaceShip.isMovingLeft = False
    

# ------------ check for mouse and keyboard inputs --------------
def check_input_events(spaceShip, settings, screen, bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            
        if event.type == pg.KEYDOWN:
            check_keydown_events(event, spaceShip, settings, screen, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, spaceShip)
            
        

def update_screen(screen, game_settings, spaceShip, bullets, aliens):
    screen.fill(game_settings.background_color)
    
    # draw all the bullets stored in the bullet sprite group
    for bullet in bullets.sprites():
        bullet.draw()
    
    spaceShip.draw()
    aliens.draw(screen)
    
    pg.display.flip()


# Update the position of all the bullets, also remove old bullets
def update_bullets(bullets):
    bullets.update()
    # remove bullets that are out of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    # print("Bullets:", len(bullets))
    
    
def get_total_number_of_aliens_on_a_row(game_settings, alien_width):
    # print("ALien", alien_width)
    available_space = game_settings.screen_width - alien_width
    # print("Available space: ", available_space)
    total_aliens = int(available_space / alien_width)
    # print("TOTAL ALIENS ON A ROW:", total_aliens_on_a_row)
    return total_aliens


def create_new_alien(screen, game_settings, aliens, alien_width, alien_index, row_number):
    alien = Alien(screen, game_settings)
    alien.x = alien.rect.width + alien_width * alien_index
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (alien.rect.height * 2 * row_number)
    aliens.add(alien)
    
def get_total_rows(screen, ship, alien):
    available_height = screen.get_height() - ship.rect.height - (alien.rect.height * 4) 
    total_rows = int(available_height / (alien.rect.height * 2))
    # print("TOTAL ROWS:", total_rows)
    return total_rows
    

# Helper function to create a full fleet of alients
def create_fleet(screen, game_settings, aliens, ship):
    alien = Alien(screen, game_settings)
    gap = 1.7
    alien_width = alien.rect.width * gap
    total_aliens_on_row = get_total_number_of_aliens_on_a_row(game_settings, alien_width)
    
    total_rows = get_total_rows(screen, ship, alien)
    
    for row_number in range(total_rows):
        for alien_index in range(total_aliens_on_row):
            create_new_alien(screen, game_settings, aliens, alien_width, alien_index, row_number)
        print("ALIENS:", len(aliens))
    
    
    # 1. available space = sreen width - (gap * x width of 1 alien)
    # 2 total numbers of aliens that i can fit on 1 row = total space / (gap * width of 1 alien)

    
def change_fleet_direction(game_settings, aliens):
    for each_alien in aliens.sprites():
        each_alien.rect.y += game_settings.fleet_dropdown_speed
    game_settings.fleet_direction = -(game_settings.fleet_direction)
        
        
def check_fleet_collide_with_edges(game_settings, aliens):
    for each_alien in aliens.sprites():
        if each_alien.check_collide_with_edges():
            change_fleet_direction(game_settings, aliens)
        
    
def update_fleet(game_settings, aliens):
    check_fleet_collide_with_edges(game_settings, aliens)
    aliens.update()