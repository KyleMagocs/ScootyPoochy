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

    sheet_path = 'objects/kitchen/stove.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 52, 27, 9, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 50
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
    collide_height = 60

    sheet_path = 'objects/kitchen/oven.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()
        self.images = self.load_sprite_sheet(self.sheet_path, 52, 53, 9, mirror)
        self.image = self.images[0]


        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 75
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

    width = 210
    x_collide_offset = 0
    y_collide_offset = 0
    collide_height = 92

    sheet_path = 'objects/kitchen/counter.png'

    def __init__(self, init_pos, mirror=False):
        self.images = self.load_sprite_sheet(self.sheet_path, 210, 92, 1, mirror)
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

class Counter2(LevelObject, collide_object):
    breakable = 0
    broken = None

    width = 160
    x_collide_offset = 0
    y_collide_offset = 0
    collide_height = 92

    sheet_path = 'objects/kitchen/counter2.png'

    def __init__(self, init_pos, mirror=False):
        self.images = self.load_sprite_sheet(self.sheet_path, 160, 92, 1, mirror)
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

    sheet_path = 'objects/kitchen/kitchenbottle.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 65, 112, 9, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 50
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width()

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1

class Mixer(LevelObject):
    breakable = 1
    broken = None
    breaksound = 'blender.wav'
    width = 50
    x_collide_offset = 16
    y_collide_offset = 50
    collide_height = 45

    sheet_path = 'objects/kitchen/kitchenmixer.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 95, 99, 9, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 300
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width()

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1

class Cabinet(LevelObject):
    breakable = 1
    broken = None
    breaksound='glass.wav'
    width = 50
    x_collide_offset = 16
    y_collide_offset = 5
    collide_height = 43
    z = .5

    sheet_path = 'objects/kitchen/kitchencabinet1.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 93, 99, 9, mirror)
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

class KitchenSink(LevelObject):
    breakable = 1
    broken = None
    breaksound = 'water.wav'
    width = 50
    x_collide_offset = 30
    y_collide_offset = 10
    collide_height = 32

    sheet_path = 'objects/kitchen/sink.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 110, 111, 9, mirror)
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
