import pygame

from Contexts.glob import GlobalContext
from Contexts.startup import StartupContext
from vars import SCREEN_WIDTH, SCREEN_HEIGHT

size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(size)
    startup = StartupContext(screen)
    startup_result = startup.display_startup()
    if not startup_result:
        quit()
    global_context = GlobalContext(screen)
    global_context.main_loop()