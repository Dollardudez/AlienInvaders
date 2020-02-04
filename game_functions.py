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
               # if key is pressed
                check_keydown_events(event, ship)
            elif event.type == pygame.KEYUP:
               #if key is released
                check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    #redraw the screen with each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #make the most recently drawn screen visible
        pygame.display.flip()

"""Respond to key-presses"""
def check_keydown_events(event, ship):
    if event.key == pygame.K_d:
        #move ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_a:
        #move ship to the left
        ship.moving_left = True

"""Respond to key-releases"""
def check_keyup_events(event, ship):
    if event.key == pygame.K_d:
        #move ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_a:
        #move ship to the left
        ship.moving_left = True

