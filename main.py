import pygame

from Contexts.game_context import GameContext
from Contexts.global_context import GlobalContext
from Objects.Characters import TestCharacter, Carlos

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPRITE_WIDTH = 60

size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(size)
    global_context = GlobalContext(screen)
    global_context.main_loop()