import sys

import pygame

def run_game():
    # Init game and create a screen objectself.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    #Start the main loop for the game
    while True:

        #Watch for keyboard and mouse events.
        for event.type == pygame.QUIT
            sys.exit()


        #make the most recently drawn screen visible
        pygame.display.flip()

run_game()
