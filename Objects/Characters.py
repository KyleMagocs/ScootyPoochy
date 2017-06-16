import os
import pygame

from colors import *

IMAGES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'images', 'characters')

ACCEL_COEF = 1


def get_all_characters():
    return [Carlos, Doge, TestCharacter, Carlos,]


class CharacterBase:
    sprite_path = None
    portrait_path = None
    sprite = None
    portrait = None
    handling = .5
    acceleration = .5
    max_speed = 1
    poop_factor = .5
    color = (200,200,200)
    attributes = None

    def __init__(self):
        self.load_sprite()
        self.load_portrait()

    def load_sprite(self):
        if self.sprite_path is not None:
            _sprite = pygame.image.load_extended(os.path.join(IMAGES_PATH, self.sprite_path)).convert()
            _sprite.set_colorkey((255, 0, 255), pygame.RLEACCEL)
            self.sprite = _sprite

    def load_portrait(self):
        if self.portrait_path is not None:
            _portrait = pygame.image.load_extended(os.path.join(IMAGES_PATH, self.portrait_path)).convert()
            _portrait.set_colorkey((255, 0, 255), pygame.RLEACCEL)
            self.portrait = _portrait


class TestCharacter(CharacterBase):
    sprite_path = 'TEMPDOG_sprite_temp.png'
    portrait_path = 'TEMPDOG_PORTRAIT.png'
    max_speed = .75 * 6
    handling = .9
    acceleration = .4
    width = 60
    color = red

    attributes = {
        '+ test character',
        '- test character'
    }

    def __init__(self):
        CharacterBase.__init__(self)


class Doge(CharacterBase):
    sprite_path = 'DOGE_sprite_temp.png'  # TODO: MAKE ACTUAL ART FOR DOGE
    portrait_path = 'DOGE_portrait_temp.png'
    max_speed = .7 * 6
    acceleration = .35
    width = 60
    handling = .95
    color = blue
    attributes = {
        '+ very meme',
        '- much average'
        '      wow'
    }

    def __init__(self):
        CharacterBase.__init__(self)


class Carlos(CharacterBase):
    sprite_path = 'carlos_sprite_temp.png'  # TODO: MAKE ACTUAL ART FOR CARLOS
    portrait_path = 'carlos_portrait_temp.png'
    max_speed = .6 * 6
    acceleration = .5
    width = 30
    handling = .8
    color = green
    attributes = {
        '- lower top speed',
        '+ high acceleration',
        '+ handles great !'
    }

    def __init__(self):
        CharacterBase.__init__(self)
