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


class PaintCans(LevelObject):
    breakable = 1
    broken = None

    width = 90
    x_collide_offset = 0
    y_collide_offset = 50
    collide_height = 50
    z = .5

    sheet_path = 'objects/garage/paintcans.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 90, 146, 9, mirror)
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


class Workbench(LevelObject, collide_object):
    breakable = 0
    broken = None

    width = 142
    x_collide_offset = 0
    y_collide_offset = 0
    z = .5

    sheet_path = 'objects/garage/workbench.png'

    def __init__(self, init_pos, mirror=False):
        self.images = self.load_sprite_sheet(self.sheet_path, 142, 98, 1, mirror)
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


class ScootPooch(LevelObject, collide_object):
    breakable = 1
    broken = None

    width = 104
    x_collide_offset = 0
    y_collide_offset = 0
    collide_height = 0
    points = 250
    z = 1

    sheet_path = 'objects/garage/pooch.png'

    def __init__(self, init_pos, mirror=False):
        self.images = self.load_sprite_sheet(self.sheet_path, 104, 189, 9, mirror)
        self.image = self.images[0]
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])

        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 250
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width()

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class WaterHeater(LevelObject, collide_object):
    breakable = 1
    broken = None
    breaksound = 'explode.wav'
    width = 46
    x_collide_offset = 62
    y_collide_offset = 45
    collide_height = 120
    points = 200
    z = 1

    sheet_path = 'objects/garage/waterheater.png'

    def __init__(self, init_pos, mirror=False):
        self.images = self.load_sprite_sheet(self.sheet_path, 143, 173, 10, mirror)
        self.image = self.images[0]
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])

        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 1000
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width()

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1

    def draw(self, screen, x_offset, y_offset, draw_points=False):
        LevelObject.draw(self, screen, x_offset, y_offset, draw_points)

class Saw(LevelObject):
    breakable = 1
    broken = None

    width = 20
    x_collide_offset = 10
    y_collide_offset = 0
    collide_height = 0

    sheet_path = 'objects/garage/saw.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 87, 62, 7, mirror)
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
