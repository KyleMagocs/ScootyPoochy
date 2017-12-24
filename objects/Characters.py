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
    victory_portrait_path = None
    sprite = None
    portrait = None
    victory_portrait = None
    poop_paths = []
    poop_factor = 15
    max_poop_factor = 75
    radius = 30
    color = (200, 200, 200)
    width = 60
    height = 60
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
        if self.victory_portrait_path is not None:
            _portrait = pygame.image.load_extended(
                os.path.join(IMAGES_PATH, 'characters', self.victory_portrait_path)).convert()
            _portrait.set_colorkey(colors.TRANSPARENT, pygame.RLEACCEL)
            self.victory_portrait = _portrait
        else:
            self.victory_portrait = self.portrait

    def get_a_poop(self, x, y, z, angle):
        new_poop = PoopTrail(self, x + self.width / 2 + random.randint(-5, 5), y + self.width / 2 + random.randint(-10, 10), z, self.poop_angle)
        return new_poop


class Cooper(CharacterBase):
    sprite_path = 'TEMPDOG_sprite_temp.png'
    portrait_path = 'cooper/portrait.png'
    victory_portrait_path = 'cooper/victory.png'
    winsound = 'cooldogwin.wav'
    head_path = 'cooper/head.png'
    larm_path = 'cooper/leftarm.png'
    rarm_path = 'cooper/rightarm.png'
    tail_path = 'cooper/tail.png'
    body_path = 'cooper/body.png'
    poop_paths = ['cooper/poop1.png', 'cooper/poop2.png']

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
    portrait_path = 'doge/portrait.png'
    winsound = 'dogewin.wav'
    head_path = 'doge/head.png'
    larm_path = 'doge/leftarm.png'
    rarm_path = 'doge/rightarm.png'
    tail_path = 'doge/tail.png'
    body_path = 'doge/body.png'

    finish_text = 'MUCH FINISH'

    poop_paths = ['doge/poop1.png', 'doge/poop2.png']

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
    portrait_path = 'beef/portrait.png'
    victory_portrait_path = 'beef/victory.png'
    winsound = 'beefwin.wav'
    head_path = 'beef/head.png'
    larm_path = 'beef/leftarm.png'
    rarm_path = 'beef/rightarm.png'
    tail_path = 'beef/tail.png'
    body_path = 'beef/body.png'

    finish_text = 'finish (´;ω;`)'

    poop_paths = ['beef/poop1.png', 'beef/poop2.png']

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
    sprite_path = 'nort_sprite_temp.png'
    portrait_path = 'nort/portrait.png'
    victory_portrait_path = 'nort/victory.png'
    winsound = 'trondogwin.wav'
    poop_paths = ['nort/nort_poop_temp.png', ]

    poop_factor = 5
    max_poop_factor = 5

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
    sprite_path = 'carlos_sprite_temp.png'
    portrait_path = 'daisy/portrait.png'
    victory_portrait_path = 'daisy/victory.png'
    winsound = 'clownwin.wav'
    poop_paths = ['daisy/poop1.png', 'daisy/poop2.png']
    head_path = 'daisy/head.png'
    larm_path = 'daisy/leftarm.png'
    rarm_path = 'daisy/rightarm.png'
    tail_path = 'daisy/tail.png'
    body_path = 'daisy/body.png'
    color = colors.green
    colorcode = b'g'
    name = 'Daisy'
    wintext = 'I\'ve earned this'
    attributes = (
        '- smol',
        '+ easily agitated'
        '- YAP YAP YAP YAP YIP YAP'
     )

    def __init__(self):
        CharacterBase.__init__(self)
