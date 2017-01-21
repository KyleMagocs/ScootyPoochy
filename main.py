from Contexts.game_context import GameContext
from Objects.Characters import *
import pygame


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPRITE_WIDTH = 60

size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(size)
    # THIS WOULD BE CALLED FROM A PLAYER SELECT CONTEXT, WHEREIN IT WOULD MAKE A SHITLOAD MORE SENSE
    game = GameContext(screen, (TestCharacter(), Carlos()))
    game.run_game()