import pygame

from contexts.char_select import CharacterSelectContext
from contexts.glob import GlobalContext
from contexts.startup import StartupContext
from vars import SCREEN_WIDTH, SCREEN_HEIGHT

size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode(size)

    # character_select = CharacterSelectContext(screen)
    # selected_characters = character_select.main_loop()

    startup = StartupContext(screen)
    startup_result = startup.display_startup()
    if not startup_result:
        quit()
    global_context = GlobalContext(screen)
    global_context.main_loop()
