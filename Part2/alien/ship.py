import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        ###INIT the ship and set its starting posiition
        self.screen = screen
        self.ai_settings = ai_settings

        #load the ship image and get its rectself.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the botten cent of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ships's center
        self.center = float(self.rect.centerx)

        #Movment flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        #update the ship's position based on the movment flag
        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #Update rect obkject from self.center
        self.rect.centerx = self.center

    def blitme(self):
        #Draw thje ship at the its current location
        self.screen.blit(self.image, self.rect)
