import os

import pygame

ASSETS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'images', 'level_assets')


def get_all_themes():
    return [TempTheme, TempTheme2, TempTheme3, TempTheme4, TempTheme5, TempTheme, TempTheme3]


class Theme:
    background_image = None
    background_sprite = None
    thumbnail_image = None
    thumbnail_sprite = None
    friction = 0

    def __init__(self):
        self.load_thumb_sprite()
        self.load_bg_sprite()

    def load_thumb_sprite(self):
        if self.thumbnail_image is not None:
            sprite = pygame.image.load_extended(os.path.join(ASSETS_PATH, self.thumbnail_image)).convert()
            scaled_sprite = pygame.transform.scale(sprite, (int(200), int(150)))
            return scaled_sprite

    def load_bg_sprite(self):
        if self.background_image is not None:
            self.background_sprite = pygame.image.load_extended(os.path.join(ASSETS_PATH, self.background_image)).convert()


class TempTheme(Theme):
    background_image = 'house_bg_temp.png'
    thumbnail_image = 'test_theme_thumbnail.png'
    friction = 2.5

    def __init__(self):
        Theme.__init__(self)


class TempTheme2(Theme):
    background_image = 'level_bg_temp.png'
    thumbnail_image = 'test_theme_thumbnail_2.png'
    friction = 2.5

    def __init__(self):
        Theme.__init__(self)


class TempTheme3(Theme):
    background_image = 'level_bg_temp.png'
    thumbnail_image = 'test_theme_thumbnail_3.png'
    friction = 2.5

    def __init__(self):
        Theme.__init__(self)


class TempTheme4(Theme):
    background_image = 'level_bg_temp.png'
    thumbnail_image = 'test_theme_thumbnail_4.png'
    friction = 2.5

    def __init__(self):
        Theme.__init__(self)


class TempTheme5(Theme):
    background_image = 'level_bg_temp.png'
    thumbnail_image = 'test_theme_thumbnail_5.png'
    friction = 2.5

    def __init__(self):
        Theme.__init__(self)
