import pygame

from Contexts.glob import GlobalContext
from Contexts.startup import StartupContext

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPRITE_WIDTH = 60

size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(size)
    global_context = GlobalContext(screen)
    startup = StartupContext(screen)
    if not startup.display_startup():
        quit()
    global_context.main_loop()