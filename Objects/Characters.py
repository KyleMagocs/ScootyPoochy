import os

import pygame

IMAGES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'images', 'characters')


class CharacterBase:
    sprite_path = None
    portrait_path = None
    sprite = None
    handling = 20
    max_speed = 20
    poop_factor = .5

    attributes = None

    def __init__(self):
        self.load_sprite()

    def load_sprite(self):
        if self.sprite_path is not None:
            self.sprite = pygame.image.load(os.path.join(IMAGES_PATH, self.sprite_path))


class TestCharacter(CharacterBase):
    sprite_path = 'TEMPDOG_sprite_temp.png'
    portrait_path = 'TEMPDOG_PORTRAIT.png'
    max_speed = 20
    handling = 20
    acceleration = 10
    width = 60

    attributes = {
        '+ test character',
        '- test character'
    }

    def __init__(self):
        CharacterBase.__init__(self)


class Doge(CharacterBase):
    sprite_path = 'TEMPDOG_sprite_temp.png'  # TODO: MAKE ACTUAL ART FOR DOGE
    portrait_path = 'TEMPDOG_PORTRAIT.png'
    max_speed = 20
    acceleration = 10
    width = 60
    handling = 20
    attributes = {
        '+ very meme',
        '- much average'
        '      wow'
    }

    def __init__(self):
        CharacterBase.__init__(self)


class Carlos(CharacterBase):
    sprite_path = 'carlos_sprite_temp.png' # TODO: MAKE ACTUAL ART FOR CARLOS
    portrait_path = 'carlos_portrait_temp.png'
    max_speed = 10
    acceleration = 20
    width = 30
    handling = 40
    attributes = {
        '- lower top speed',
        '+ high acceleration',
        '+ handles great !'
    }

    def __init__(self):
        CharacterBase.__init__(self)