import pygame

class Ship():

    def __init__(self,screen):
        ###INIT the ship and set its starting posiition
        self.screen = screen

        #load the ship image and get its rectself.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the botten cent of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        #Draw thje ship at the its current location
        self.screen.blit(self.image, self.rect)
