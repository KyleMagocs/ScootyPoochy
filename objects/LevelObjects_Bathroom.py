import os
import pygame

import colors
import vars
from objects.CollideObject import collide_object
from objects.LevelObjects import LevelObject
from utils.hollow import textHollow, textOutline
from utils.spritesheet import spritesheet


class Shower(LevelObject, collide_object):
    breakable = 0
    score = 10
    image_path = 'objects/bathroom/shower.png'
    width = 15
    x_collide_offset = 150

    def __init__(self, init_pos, mirror=False):
        self.image = self.load_sprite(mirror)
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])
        self.height = .2
        self.z = .2

    def load_sprite(self, mirror=False):
        _image = pygame.image.load_extended(
            os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
        _image.set_colorkey(colors.TRANSPARENT, pygame.RLEACCEL)
        return _image

    def draw(self, screen, x_offset, y_offset, draw_points=False):
        collide_object.draw(self, screen, x_offset, y_offset)


class BathroomSink(LevelObject, collide_object):
    breakable = 0
    score = 0
    image_path = 'objects/bathroom/bathroomsink.png'
    width = 112
    x_collide_offset = 2

    def __init__(self, init_pos, mirror=False):
        self.image = self.load_sprite(mirror)
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])
        self.height = .5
        self.z = .5

    def load_sprite(self, mirror=False):
        _image = pygame.image.load_extended(
            os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
        _image.set_colorkey(colors.TRANSPARENT, pygame.RLEACCEL)
        return _image

    def draw(self, screen, x_offset, y_offset, draw_points=False):
        collide_object.draw(self, screen, x_offset, y_offset)

    def get_rect(self):
        _rect = self.image.subsurface((0, 0, self.image.get_width(), self.image.get_height() - 40)).get_rect()
        return _rect


class SinkStuff(LevelObject):
    breakable = 1
    broken = None

    width = 23
    x_collide_offset = 6

    sheet_path = 'objects/bathroom/bathroomstuff_sheet.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 70, 136, 9, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]

        self.height = .2
        self.z = .2

        self.points = 15

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1

    def get_collide_rect(self):
        _rect = self.image.get_rect()
        _rect.width = self.width
        _rect.height = 50
        _rect.x += self.x + self.x_collide_offset
        _rect.y += self.y + self.y_collide_offset
        return _rect


class Toilet(LevelObject, collide_object):
    breakable = 1
    score = 50
    sheet_path = 'objects/bathroom/toilet_sheet.png'
    breaksound = 'flush.wav'
    width = 45
    points = 50
    x_collide_offset = 18

    def __init__(self, init_pos, mirror=False):
        self.images = self.load_sprite_sheet(self.sheet_path, 87, 111, 9, mirror)
        self.image = self.images[0]
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])
        self.height = .3
        self.z = .3
        self.image_index = 0
        self.points = 50

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1

    def draw(self, screen, x_offset, y_offset, draw_points=False):
        LevelObject.draw(self, screen, x_offset, y_offset, draw_points)


class BathMat(LevelObject):
    breakable = 0
    score = 0
    width = 100
    image_path = 'objects/bathroom/bathmat.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()
        self.image = self.load_sprite(mirror)
        self.x = init_pos[0]
        self.y = init_pos[1]
