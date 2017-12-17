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


class Gnome(LevelObject):
    breakable = 1
    broken = None

    width = 25
    x_collide_offset = 50
    y_collide_offset = 0
    collide_height = 50

    sheet_path = 'objects/gnome_sheet.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 76, 59, 9, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 50
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width() - self.width - 4

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class BirdBath(LevelObject):
    breakable = 1
    broken = None

    width = 32
    x_collide_offset = 60
    y_collide_offset = 60
    collide_height = 60

    sheet_path = 'objects/birdbath_sheet.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 182, 133, 9, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 200
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width() - self.width - 4

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Flower1(LevelObject):
    breakable = 1
    broken = None

    width = 15
    x_collide_offset = 60

    sheet_path = 'objects/flower1.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 82, 73, 7, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 15
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width() - self.width - 4

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Flower2(LevelObject):
    breakable = 1
    broken = None

    width = 15
    x_collide_offset = 60

    sheet_path = 'objects/flower2.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 82, 77, 7, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 15
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width() - self.width - 4

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Flower3(LevelObject):
    breakable = 1
    broken = None

    width = 15
    x_collide_offset = 55

    sheet_path = 'objects/flower3.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 82, 77, 7, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 15
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width() - self.width - 4

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Flower4(LevelObject):
    breakable = 1
    broken = None

    width = 15
    x_collide_offset = 17

    sheet_path = 'objects/flower4.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 47, 92, 7, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 15
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width() - self.width - 4

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Grill(LevelObject):
    breakable = 1
    broken = None

    width = 45
    collide_height = 80
    x_collide_offset = 37
    y_collide_offset = 35

    sheet_path = 'objects/grill.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 251, 150, 7, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 200
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width() - self.width - 4

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1
