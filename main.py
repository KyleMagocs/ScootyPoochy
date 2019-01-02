import os

import pygame

from contexts.char_select import CharacterSelectContext
from contexts.glob import GlobalContext
from contexts.level_select import LevelSelectContext
from contexts.startup import StartupContext
from vars import SCREEN_WIDTH, SCREEN_HEIGHT, LAUNCH_OPTIONS
import datetime
import sys, traceback

size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT

if __name__ == "__main__":
    # Windows: windib, directx
    # Unix: x11, dga, fbcon, directfb, ggi, vgl, svgalib, aalib
    # os.environ["SDL_VIDEODRIVER"] = "x11"
    pygame.init()
    screen = pygame.display.set_mode(size, LAUNCH_OPTIONS)
    pygame.mouse.set_visible(False)

    # character_select = CharacterSelectContext(screen)
    # selected_characters = character_select.main_loop()
    #
    # level_select = LevelSelectContext(screen)
    # level = level_select.main_loop()
    try:

        startup = StartupContext(screen)
        startup_result = startup.display_startup()
        if not startup_result:
            quit()
        global_context = GlobalContext(screen)
        global_context.main_loop()
    except Exception as e:
        with open('error_logs/Crash - ' + str(datetime.datetime.now().strftime('%y-%b-%d_%H-%M-%S')) + '.txt', 'w+') as f:
            f.write(str(e))
            f.write('\n\n\nTRACEBACK:\n\n')
            f.write(repr(traceback.extract_tb(sys.exc_info()[2])))

