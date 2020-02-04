import pygame
class Ship():

    def __init__(self, screen):
        #initialize the ship and set its starting position
        self.screen = screen
        #load ship image
        self.image = pygame.image.load('Images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
    
    #update ship's position based on the movement flag
    def update(self):
        if self.moving_right:
            self.rect.centerx +=1
        if self.moving_left:
            self.rect.centerx -=1
     

        #start each ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #Draw ship at its current location
        self.screen.blit(self.image, self.rect)
