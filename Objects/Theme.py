import os

import pygame

ASSETS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'images', 'level_assets')


class Theme:
    background_image = None
    background_sprite = None
    friction = 0

    def __init__(self):
        self.load_bg_sprite()

    def load_bg_sprite(self):
        if self.background_image is not None:
            self.background_sprite = pygame.image.load_extended(os.path.join(ASSETS_PATH, self.background_image)).convert()


class TempTheme(Theme):
    background_image = 'level_bg_temp.png'
    friction = 1.1

    def __init__(self):
        Theme.__init__(self)
