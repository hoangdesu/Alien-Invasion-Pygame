import json
import sys
import pygame as pg
from time import sleep

from bullet import Bullet
from alien import Alien
from constants import *

# ------------ check for mouse and keyboard inputs --------------
def check_input_events(spaceShip, settings, screen, bullets, aliens, game_stats, play_btn, score, sound):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
            
        if event.type == pg.KEYDOWN:
            check_keydown_events(event, spaceShip, settings, screen, bullets, game_stats, aliens, spaceShip, score, sound)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, spaceShip)
        
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            play_btn_click_handler(settings, screen, game_stats, aliens, bullets, spaceShip, play_btn, mouse_x, mouse_y, score)

        check_mouse_hover(screen, settings, game_stats, play_btn, spaceShip, bullets, aliens, score)
    
            
# helper functions
def check_keydown_events(event, spaceShip, settings, screen, bullets, game_stats, aliens, ship, score, sound):
    if event.key == pg.K_RIGHT:
        spaceShip.isMovingRight = True
    elif event.key == pg.K_LEFT:
        spaceShip.isMovingLeft = True
    elif event.key == pg.K_SPACE:
        if len(bullets) < settings.bullets_max_allowed:
            new_bullet = Bullet(settings, screen, spaceShip)
            bullets.add(new_bullet)
            sound.pewpew.play()
            # pg.mixer.Channel(1).play(sound.pewpew, maxtime=600)
    elif event.key == pg.K_ESCAPE and game_stats.game_state == GAME_STATE_MENU:
        sys.exit()
    elif event.key == pg.K_RETURN and game_stats.game_over:
        start_a_new_game(settings, screen, game_stats, aliens, bullets, ship, score)
    elif event.key == pg.K_m:
        vol = sound.bgm.get_volume()
        if vol > 0: # sound playing
            sound.bgm.set_volume(0)
        else:
            sound.bgm.set_volume(0.08)
    
    # event triggering state transition
    elif event.key == pg.K_RETURN:
        if game_stats.game_state == GAME_STATE_MENU:
           game_stats.game_state = GAME_STATE_PLAY
    elif event.key == pg.K_ESCAPE and game_stats.game_state == GAME_STATE_PLAY:
        game_stats.game_state = GAME_STATE_MENU
        
    
    # For testing only
    elif event.key == pg.K_1:   # test for starting a new game
        start_a_new_game(settings, screen, game_stats, aliens, bullets, ship, score)
    elif event.key == pg.K_2:   # test for speed increase
        settings.increase_speed()
        # print("INCREASED:", settings.alien_speed)
    elif event.key == pg.K_3:   # test for level up
        aliens.empty()


        
    
def check_keyup_events(event, spaceShip):
    if event.key == pg.K_RIGHT:
        spaceShip.isMovingRight = False
    elif event.key == pg.K_LEFT:
        spaceShip.isMovingLeft = False
        
        
def check_mouse_hover(screen, game_settings, game_stats, play_btn, ship, bullets, aliens, score):
    if game_stats.game_over:
        mouse_x, mouse_y = pg.mouse.get_pos()
        if play_btn.rect.collidepoint(mouse_x, mouse_y):
            play_btn.bg_color = (17, 34, 128)
            play_btn.text_color = (250, 250, 87)
            play_btn.prep_msg("Play!")
            pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_HAND)
        else:
            play_btn.bg_color = (30, 52, 166)
            play_btn.text_color = (255, 255, 161)
            play_btn.prep_msg("Play!")
            pg.mouse.set_system_cursor(pg.SYSTEM_CURSOR_ARROW)
        update_screen(screen, game_settings, game_stats, ship, bullets, aliens, play_btn, score)
                
    
        
        
# ----------- RESET THE GAME IF THE PLAY BUTTON IS CLICKED!
def play_btn_click_handler(game_settings, screen, game_stats, aliens, bullets, ship, play_btn, mouse_x, mouse_y, score):
    if play_btn.rect.collidepoint(mouse_x, mouse_y) and game_stats.game_over:
        start_a_new_game(game_settings, screen, game_stats, aliens, bullets, ship, score)

def start_a_new_game(game_settings, screen, game_stats, aliens, bullets, ship, score):
    game_stats.reset_statistics()
    game_stats.game_over = False
    
    aliens.empty()
    bullets.empty()
    
    # re-render the stat images
    score.render_score(SCORE_TYPES_NORMAL)
    score.render_score(SCORE_TYPES_HIGHSCORE)
    score.render_level()

    create_fleet(screen, game_settings, aliens, ship)
    ship.center_ship()
    
    score.render_level()
    score.render_score(SCORE_TYPES_NORMAL)
    score.render_score(SCORE_TYPES_HIGHSCORE)
    score.render_lives()
    
    # print("Game reset!")
    pg.mouse.set_visible(False)
    game_settings.reset_dynamic_settings()
    overwrite_highscore_to_file(game_stats)


# ----------- update screen function --------------
def update_screen(screen, game_settings, game_stats, ship, bullets, aliens, play_btn, score):
    # screen.fill(game_settings.background_color)
    screen.blit(game_settings.background, (0, 0))
    
    score.draw()
    
    # draw all the bullets stored in the bullet sprite group
    for bullet in bullets.sprites():
        bullet.draw()
    
    ship.draw()
    aliens.draw(screen)

    if game_stats.game_over:
        play_btn.draw()

    pg.display.flip()

    
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
            break
        
    
def update_fleet(game_settings, screen, game_stats, aliens, ship, bullets, score):
    check_fleet_collide_with_edges(game_settings, aliens)
    aliens.update()

    # check collision between ship vs any alien sprite
    if pg.sprite.spritecollideany(ship, aliens):
        reset_game(game_settings, screen, game_stats, ship, aliens, bullets, score)
        
    aliens_hit_screen_bottom(game_settings, screen, game_stats, ship, aliens, bullets, score)
    

# Update the position of all the bullets, also remove old bullets
def update_bullets(bullets, aliens, game_settings, screen, ship, game_stats, score, sound):
    bullets.update()
    # remove bullets that are out of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    # print("Bullets:", len(bullets))
    
    # if bullets hit aliens, kill both of the sprite groups
    collisions = pg.sprite.groupcollide(aliens, bullets, True, True)
    if collisions:
        for aliens in collisions.values():
            game_stats.score += game_settings.alien_points * len(aliens)
            # game_stats.score += 100
            # print('[SCORE]:', game_stats.score)
            score.render_score(SCORE_TYPES_NORMAL)
            sound.boom.play()
        replace_highscore(game_stats, score)
    
    # spawn a new fleet when all the aliens are cleared! + LEVEL UP! + Increase speed
    if (len(aliens) == 0):
        bullets.empty()
        ship.center_ship()
        game_settings.increase_speed()
        # print(game_settings.alien_speed)
        
        # level cleared
        game_stats.level += 1
        score.render_level()

        create_fleet(screen, game_settings, aliens, ship)
        
        
        
        
def reset_game(game_settings, screen, game_stats, ship, aliens, bullets, score):
    if game_stats.ship_lives > 1:
        # take away one live
        game_stats.ship_lives -= 1
    
        # clear all the sprites on screen
        bullets.empty()
        aliens.empty()
        
        # spawn a new fleet again
        create_fleet(screen, game_settings, aliens, ship)
        
        # pause for 1s before the replay
        sleep(1)
    else:
        # set the game state to be over
        game_stats.ship_lives -= 1
        score.render_lives()
        game_stats.game_over = True

        pg.mouse.set_visible(True)
        
    
    
def aliens_hit_screen_bottom(game_settings, screen, game_stats, ship, aliens, bullets, score):
    for alien in aliens.sprites():
        if alien.rect.bottom > screen.get_rect().bottom:
            reset_game(game_settings, screen, game_stats, ship, aliens, bullets, score)
            break


def replace_highscore(game_stats, score):
    if game_stats.score > game_stats.high_score:
        game_stats.high_score = game_stats.score
        score.render_score(SCORE_TYPES_HIGHSCORE)


def overwrite_highscore_to_file(game_stats):
    # DICTIONARY in Python
    # player = input("Enter your name: ")
    with open('./data.json', 'r') as file:
        data = json.load(file)
        data["high_score"] = game_stats.high_score
        # data["player"] = player
        with open('./data.json', 'w') as file_w:
            json.dump(data, file_w, indent=4)
            file_w.close()
        file.close()