import sys

import pygame

from settings import Settings
from ship import Ship

def run_game():
    # Init game and create a screen object settings.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a Ship
    ship = Ship(screen)

    #background color
    #bg_color = (230, 230, 230)


    #Start the main loop for the game
    while True:

        #Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redraw bg everyloop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        #make the most recently drawn screen visible
        pygame.display.flip()


run_game()
