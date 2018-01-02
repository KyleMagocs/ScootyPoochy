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


class Stove(LevelObject):
    breakable = 1
    broken = None

    width = 50
    x_collide_offset = 0
    y_collide_offset = 0
    collide_height = 50
    z = .3

    sheet_path = 'objects/stove.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 52, 27, 9, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 100
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width()

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Oven(LevelObject):
    breakable = 1
    broken = None

    width = 50
    x_collide_offset = 0
    y_collide_offset = 0
    collide_height = 10

    sheet_path = 'objects/oven.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 52, 52, 9, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 150
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width()

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Counter(LevelObject, collide_object):
    breakable = 0
    broken = None

    width = 50
    x_collide_offset = 0
    y_collide_offset = 0
    collide_height = 25

    sheet_path = 'objects/counter.png'

    def __init__(self, init_pos, mirror=False):
        self.images = self.load_sprite_sheet(self.sheet_path, 210, 73, 1, mirror)
        self.image = self.images[0]
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])

        self.image_index = 0
        self.height = .3
        self.z = .3
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 150
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width()

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1

class Bottle(LevelObject):
    breakable = 1
    broken = None

    width = 12
    x_collide_offset = 0
    y_collide_offset = 0
    collide_height = 25

    sheet_path = 'objects/kitchenbottle.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 65, 112, 9, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 150
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width()

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1
