import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initialize python, settings, and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invaders")

    #make a ship
    ship = Ship(screen)
    
    #start the loop for the game
    while True:
        gf.check_events(ship)
        ship.update()
        ship.blitme()
        gf.update_screen(ai_settings, screen, ship)
run_game()