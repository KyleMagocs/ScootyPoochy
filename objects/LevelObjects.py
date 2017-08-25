import os
import pygame

import colors
import vars
from objects.CollideObject import collide_object
from utils.hollow import textHollow, textOutline
from utils.spritesheet import spritesheet


class LevelObject(pygame.sprite.Sprite):
    breakable = 0  # 1 for breakable objects
    broken = 0  # 1 = breaking, 2 = broken
    passable = 1  #
    image_path = None
    height = 0
    z = 0
    width = 15
    x_collide_offset = 0
    y_collide_offset = 0

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.points = 0
        self.points_delta = 0
        self.image = None

    def get_wrecked(self):
        if self.breakable and not self.broken:
            self.broken = 1
            self.points_delta = 5
            # TODO: PLAY BROKEN NOISE
            return True

    def draw(self, screen, x_offset, y_offset, draw_points=False):
        if self.get_draw_rect().bottom + y_offset < 0 or self.get_draw_rect().top + y_offset > vars.SCREEN_HEIGHT:
            return
        screen.blit(self.image, (self.x + x_offset, self.y + y_offset))
        if vars.draw_rects:
            _rect = self.get_collide_rect()
            _rect.x += x_offset
            _rect.y += y_offset
            pygame.draw.rect(screen, (255, 255, 255), _rect, 1)

    def draw_score(self, screen, x_offset, y_offset, draw_points=False):
        if draw_points and 0 < self.points_delta < 100:
            font = pygame.font.SysFont('Impact', 16)
            text = textOutline(font, str(self.points), colors.white, colors.black)
            screen.blit(text, (self.rect.x + x_offset, self.rect.y - self.points_delta + y_offset))
            self.points_delta += 5

    def load_sprite_sheet(self, sheet_path, width, height, num, mirror=False):
        _images = []
        sheet = spritesheet(os.path.join(vars.IMAGES_PATH, sheet_path))
        for x in range(0, width * num, width):
            _image = sheet.image_at((x, 0, width, height), (255, 0, 255))
            _image = pygame.transform.flip(_image, mirror, False)
            for x in range(0, int(vars.fps/10)):
                _images.append(_image)
        return _images

    def get_draw_rect(self):
        _rect = self.image.get_rect()
        _rect.x += self.x
        _rect.y += self.y
        return _rect

    def get_collide_rect(self):
        _rect = self.image.get_rect()
        _rect.width = self.width
        _rect.x += self.x + self.x_collide_offset
        _rect.y += self.y + self.y_collide_offset
        return _rect

    @property
    def rect(self):
        return self.get_collide_rect()
        #
        # def get_rect(self):
        #     _rect = self.image.subsurface((0, 0, self.image.get_width(), self.image.get_height())).get_rect()
        #     _rect.x += self.x
        #     _rect.y += self.y
        #     return _rect


class Lamp(LevelObject):
    breakable = 1
    broken = None

    width = 30
    x_collide_offset = 6

    image_path = 'objects/lamp.png'
    sheet_path = 'objects/lamp_sheet.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()

        self.images = self.load_sprite_sheet(self.sheet_path, 130, 100, 10, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.points = 100
        if mirror:
            self.x -= self.image.get_width()
            self.x_collide_offset = self.image.get_width()-self.width-4

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Vase(LevelObject):
    breakable = 1
    broken = None

    width = 32

    sheet_path = 'objects/vase_sheet.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.images = self.load_sprite_sheet(self.sheet_path, 32, 32, 8, mirror)
        self.image = self.images[0]
        self.points = 400
        self.image_index = 0

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Cuckoo(LevelObject):
    breakable = 1
    broken = None
    z = .5
    width = 30

    sheet_path = 'objects/clock_sheet.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.images = self.load_sprite_sheet(self.sheet_path, 60, 90, 9, mirror)
        self.image = self.images[0]
        self.points = 800
        self.image_index = 0

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class HDTV(LevelObject):
    breakable = 1
    broken = None
    z = .5
    width = 100

    sheet_path = 'objects/hdtv_sheet.png'

    def __init__(self, init_pos, mirror=False):
        super().__init__()
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.images = self.load_sprite_sheet(self.sheet_path, 100, 160, 11, mirror)
        self.image = self.images[0]
        self.points = 800
        self.image_index = 0

    def update(self, addtl_x, addtl_y):
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1


class Couch(LevelObject, collide_object):
    breakable = 0
    score = 10
    image_path = 'objects/couch.png'
    width = 100

    def __init__(self, init_pos, mirror=False):
        self.image = self.load_sprite(mirror)
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])
        self.height = .2
        self.z = .2

    def load_sprite(self, mirror=False):
        _image = pygame.image.load_extended(
            os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
        _image.set_colorkey((255, 0, 255), pygame.RLEACCEL)
        return _image

    def draw(self, screen, x_offset, y_offset, draw_points=False):
        collide_object.draw(self, screen, x_offset, y_offset)

    def get_rect(self):
        _rect = self.image.subsurface((0, 0, self.image.get_width(), self.image.get_height() - 10)).get_rect()
        _rect.x += self.x
        _rect.y += self.y
        return _rect


class Table(LevelObject, collide_object):
    breakable = 0
    score = 10
    image_path = 'objects/table.png'
    width = 150

    def __init__(self, init_pos, mirror=False):
        self.image = self.load_sprite(mirror)
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])
        self.height = .2
        self.z = .2

    def load_sprite(self, mirror=False):
        _image = pygame.image.load_extended(
            os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
        _image.set_colorkey((255, 0, 255), pygame.RLEACCEL)
        return _image

    def draw(self, screen, x_offset, y_offset, draw_points=False):
        collide_object.draw(self, screen, x_offset, y_offset)

    def get_rect(self):
        _rect = self.image.subsurface((0, 0, self.image.get_width(), self.image.get_height() - 10)).get_rect()
        _rect.x += self.x
        _rect.y += self.y
        return _rect


class BookShelf(LevelObject, collide_object):
    breakable = 0
    score = 10
    image_path = 'objects/bookshelf.png'
    width = 106

    def __init__(self, init_pos, mirror=False):
        self.image = self.load_sprite(mirror)
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])
        self.height = .4
        self.z = .4

    def load_sprite(self, mirror=False):
        _image = pygame.image.load_extended(
            os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
        _image.set_colorkey((255, 0, 255), pygame.RLEACCEL)
        return _image

    def draw(self, screen, x_offset, y_offset, draw_points=False):
        collide_object.draw(self, screen, x_offset, y_offset)

    def get_rect(self):
        _rect = self.image.subsurface((0, 0, self.image.get_width(), self.image.get_height() - 40)).get_rect()
        _rect.x += self.x
        _rect.y += self.y + 30
        return _rect


class Shower(LevelObject, collide_object):
    breakable = 0
    score = 10
    image_path = 'objects/shower.png'
    width = 15
    x_collide_offset = 175

    def __init__(self, init_pos, mirror=False):
        self.image = self.load_sprite(mirror)
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])
        self.height = .4
        self.z = .4

    def load_sprite(self, mirror=False):
        _image = pygame.image.load_extended(
            os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
        _image.set_colorkey((255, 0, 255), pygame.RLEACCEL)
        return _image

    def draw(self, screen, x_offset, y_offset, draw_points=False):
        collide_object.draw(self, screen, x_offset, y_offset)
