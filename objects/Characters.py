import os

import pygame

import colors
from utils.sprite_utils import rot_center
from utils.spritesheet import spritesheet
from vars import IMAGES_PATH
import random
import vars

ACCEL_COEF = 1


def get_all_characters():
    return [Daisy, Doge, Cooper, Nort, Beef]


# TODO:  THIS IS TRASH

class PoopTrail(pygame.sprite.Sprite):
    def __init__(self, character, x, y, z, angle):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        _sprite = pygame.image.load_extended(os.path.join(IMAGES_PATH, 'characters',
                                                          character.poop_paths[random.randint(0, len(
                                                              character.poop_paths) - 1)])).convert()
        _sprite.set_colorkey(colors.TRANSPARENT, pygame.RLEACCEL)

        self.image = _sprite
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image = self.rotate_image(angle)

    def rotate_image(self, angle):
        # angle = random.randint(0, 360)
        return rot_center(self.image, angle)


class NortPoop(pygame.sprite.Sprite):
    def __init__(self, character, x, y, z, angle):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        _sprite = pygame.image.load_extended(os.path.join(IMAGES_PATH, 'characters',
                                                          character.poop_paths[random.randint(0, len(
                                                              character.poop_paths) - 1)])).convert()
        _sprite.set_colorkey(colors.TRANSPARENT, pygame.RLEACCEL)

        self.image = _sprite
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image = self.rotate_image(angle)

    def rotate_image(self, angle=random.randint(0, 360)):
        return rot_center(self.image, angle)


class CharacterBase:
    sprite_path = None
    portrait_path = None
    sprite = None
    portrait = None
    poop_paths = []
    handling = .5
    acceleration = .5
    max_speed = 1
    poop_factor = 15
    max_poop_factor = 75
    color = (200, 200, 200)
    width = 0
    height = 0
    attributes = None
    name = None
    finish_text = 'FINISH !'

    def __init__(self):
        self.load_sprite()
        self.load_portrait()
        self.current_poop_factor = 1
        self.poop_angle = 0

    def load_sprite(self):
        if self.sprite_path is not None:
            _sprite = pygame.image.load_extended(os.path.join(IMAGES_PATH, 'characters', self.sprite_path)).convert()
            _sprite.set_colorkey(colors.TRANSPARENT, pygame.RLEACCEL)
            self.sprite = _sprite

    def load_portrait(self):
        if self.portrait_path is not None:
            _portrait = pygame.image.load_extended(
                os.path.join(IMAGES_PATH, 'characters', self.portrait_path)).convert()
            _portrait.set_colorkey(colors.TRANSPARENT, pygame.RLEACCEL)
            self.portrait = _portrait

    def get_a_poop(self, x, y, z, angle):
        new_poop = PoopTrail(self, x + self.width / 2 + random.randint(-5, 5), y + self.width / 2 + random.randint(-10, 10), z, self.poop_angle)
        return new_poop


class Cooper(CharacterBase):
    sprite_path = 'TEMPDOG_sprite_temp.png'
    portrait_path = 'TEMPDOG_PORTRAIT.png'
    winsound = 'cooldogwin.wav'
    head_path = 'cooper/head.png'
    larm_path = 'cooper/leftarm.png'
    rarm_path = 'cooper/rightarm.png'
    tail_path = 'cooper/tail.png'
    body_path = 'cooper/body.png'
    poop_paths = ['cooper/poop1.png', 'cooper/poop2.png']
    max_speed = .75 * 6
    handling = .9
    acceleration = .4
    max_poop_factor = 25
    width = 60
    height = 60
    radius = 30
    color = colors.red
    colorcode = b'r'
    name = 'Cooper'
    wintext = 'CANFIELD SUCKS.'
    attributes = (
        '+ not as in Anderson',
        '+ it\'s Xylon\'s Dog!',
        '- who the hell is Xylon?'
    )

    def __init__(self):
        CharacterBase.__init__(self)


class Doge(CharacterBase):
    #sprite_path = 'DOGE_sprite_temp.png'  # TODO: MAKE ACTUAL ART FOR DOGE
    portrait_path = 'DOGE_portrait_temp.png'
    winsound = 'dogewin.wav'
    head_path = 'doge/head.png'
    larm_path = 'doge/leftarm.png'
    rarm_path = 'doge/rightarm.png'
    tail_path = 'doge/tail.png'
    body_path = 'doge/body.png'

    finish_text = 'MUCH FINISH'

    poop_paths = ['doge/poop1.png', 'doge/poop2.png']
    max_speed = .7 * 6
    acceleration = .35
    width = 60
    height = 60
    radius = 30
    handling = .95
    max_poop_factor = 75
    color = colors.light_blue
    colorcode = b'b'
    name = 'DOGE'
    wintext = 'WOW'
    attributes = (
        '+ very meme',
        '- much average'
        '      wow'
     )

    def __init__(self):
        CharacterBase.__init__(self)

class Beef(CharacterBase):
    #sprite_path = 'DOGE_sprite_temp.png'  # TODO: MAKE ACTUAL ART FOR DOGE
    portrait_path = 'beef_portrait_temp.png'
    winsound = 'beefwin.wav'
    head_path = 'beef/head.png'
    larm_path = 'beef/leftarm.png'
    rarm_path = 'beef/rightarm.png'
    tail_path = 'beef/tail.png'
    body_path = 'beef/body.png'

    finish_text = 'finish (｡-人-｡)'

    poop_paths = ['beef/poop1.png', 'beef/poop2.png']
    max_speed = .7 * 6
    acceleration = .35
    width = 60
    height = 60
    radius = 30
    handling = .95
    max_poop_factor = 75
    color = colors.light_grey
    colorcode = b'w'
    name = 'Roast Beef'
    wintext = 'Oh dang, I did it'
    attributes = (
        '+ is a cat',
        '- is a sad cat',
        '+ pretty cute tho',

    )

    def __init__(self):
        CharacterBase.__init__(self)


class Nort(CharacterBase):
    sprite_path = 'nort_sprite_temp.png'  # TODO: MAKE ACTUAL ART FOR DOGE
    portrait_path = 'nort_portrait_temp.png'
    winsound = 'trondogwin.wav'
    poop_paths = ['nort/nort_poop_temp.png', ]
    max_speed = .7 * 6
    acceleration = .35
    poop_factor = 1
    max_poop_factor = 75
    width = 60
    height = 60
    radius = 30
    handling = .95
    color = colors.aqua
    colorcode = b'a'
    name = 'NORT'
    wintext = '1982 was a good year'
    attributes = (
        '+ Laser poops',
        '+ Futuristic',
        '- bad handling'
    )

    def __init__(self):
        CharacterBase.__init__(self)

    def get_a_poop(self, x, y, z, angle):
        new_poop = NortPoop(self, x + self.width / 2, y + self.width / 2, z, angle)
        return new_poop


class Daisy(CharacterBase):
    sprite_path = 'carlos_sprite_temp.png'  # TODO: MAKE ACTUAL ART FOR CARLOS
    portrait_path = 'carlos_portrait_temp.png'
    winsound = 'clownwin.wav'
    poop_paths = ['daisy/poop1.png', 'daisy/poop2.png']
    max_speed = .6 * 6
    acceleration = .5
    width = 30
    height = 30
    radius = 15
    handling = .8
    max_poop_factor = 75
    color = colors.green
    colorcode = b'g'
    name = 'Chichi'
    wintext = 'I AM A BAD DOG AND I SHOULD BE REMOVED FROM THIS GAME'
    attributes = (
        '- lower top speed',
        '+ high acceleration',
        '+ handles great !'
     )

    def __init__(self):
        CharacterBase.__init__(self)
