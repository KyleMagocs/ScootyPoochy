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

    width = 30
    x_collide_offset = 6

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
            self.x_collide_offset = self.image.get_width()-self.width-4

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
            self.x_collide_offset = self.image.get_width()-self.width-4

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1