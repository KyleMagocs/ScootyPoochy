import os
import pygame

import colors
import debugcontrols
import vars
from objects.CollideObject import collide_object
from objects.LevelObjects import LevelObject
from utils.hollow import textHollow, textOutline
from utils.sprite_utils import image_to_surface
from utils.spritesheet import spritesheet


class Candle(LevelObject):
    breakable = 1
    broken = None

    width = 30
    collide_height = 70
    x_collide_offset = 74
    y_collide_offset = 10
    points = 100
    z = .5

    sheet_path = 'objects/diningroom/candle.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 110, 96, 8, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        if mirror:
            # self.x -= self.image.get_width()
            self.x_collide_offset = 7

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class DiningTable(LevelObject, collide_object):
    breakable = 0
    broken = None

    width = 169
    x_collide_offset = 0
    y_collide_offset = 0

    sheet_path = 'objects/diningroom/table.png'

    def __init__(self, init_pos, mirror=False):
        self.images = self.load_sprite_sheet(self.sheet_path, 169, 241, 1, mirror)
        self.image = self.images[0]
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])

        self.image_index = 0
        self.height = .4
        self.z = .4
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 0
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width()

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Plate(LevelObject):
    breakable = 1
    broken = None
    breaksound = 'glass.wav'
    width = 43
    x_collide_offset = 8
    y_collide_offset = 40
    collide_height = 20
    points = 50

    sheet_path = 'objects/diningroom/plate.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 118, 143, 9, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 50
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = 65

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Painting_One(LevelObject):
    breakable = 1
    broken = None
    z = .5
    width = 59
    breaksound = 'rip.wav'
    sheet_path = 'objects/diningroom/painting1.png'
    points = 400

    def __init__(self, init_pos, mirror=False):
        super().__init__()
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.images = self.load_sprite_sheet(self.sheet_path, 59, 75, 7, mirror)
        self.image = self.images[0]

        self.image_index = 0

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Painting_Two(LevelObject):
    breakable = 1
    broken = None
    z = .5
    width = 59
    breaksound = 'rip.wav'
    sheet_path = 'objects/diningroom/painting2.png'
    points = 400

    def __init__(self, init_pos, mirror=False):
        super().__init__()
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.images = self.load_sprite_sheet(self.sheet_path, 67, 136, 9, mirror)
        self.image = self.images[0]
        self.image_index = 0

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Chair(LevelObject):
    breakable = 1
    broken = None

    width = 50
    collide_height = 50
    x_collide_offset = 0
    y_collide_offset = 54
    points = 50

    sheet_path = 'objects/diningroom/chair.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 182, 171, 8, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width() - self.width - 4

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1
