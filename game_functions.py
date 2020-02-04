import sys
import pygame
from settings import Settings
from ship import Ship


def check_events(ship):
    #respond to key presses and mouse clicks
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
               # if d key is pressed
                if event.key == pygame.K_RIGHT:
                    #move ship to the right
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    #move ship to the right
                    ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    #redraw the screen with each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #make the most recently drawn screen visible
        pygame.display.flip()

