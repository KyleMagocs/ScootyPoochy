import os
import pygame
import vars
from objects.CollideObject import collide_object
from utils.spritesheet import spritesheet


class LevelObject(pygame.sprite.Sprite):
    breakable = 0  # 1 for breakable objects
    broken = 0  # 1 = breaking, 2 = broken
    passable = 1 #
    image_path = None
    height = 1

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
            # self.image = pygame.transform.rotate(self.image, -90)
            return True

    def draw(self, screen, x_offset, y_offset):
        if self.rect.bottom + y_offset < 0 or self.rect.top + y_offset > vars.SCREEN_HEIGHT:
            return
        screen.blit(self.image, (self.rect.x + x_offset, self.rect.y - self.image.get_height() + self.rect.height + y_offset))
        if vars.draw_rects:
            _rect = self.rect
            _rect.x += x_offset
            _rect.y += y_offset
            pygame.draw.rect(screen, (255, 255, 255), _rect, 1)

        if 0 < self.points_delta < 100:
            font = pygame.font.SysFont('Impact', 16)
            label = font.render(str(self.points), 1, (255, 255, 255))
            screen.blit(label, (self.rect.x + x_offset, self.rect.y - self.points_delta + y_offset))
            self.points_delta += 5

    @property
    def rect(self):
        _rect = self.image.get_rect()
        _rect.x += self.x
        _rect.y += self.y
        return _rect

class Lamp(LevelObject):
    breakable = 1
    broken = None

    image_rects = (
        (0, 0, 30, 100),
        (31, 0, 58, 100),
        (90, 0, 88, 100),
        (179, 0, 100, 100),
    )

    image_path = 'objects/lamp.png'
    sheet_path = 'objects/lampsheet.png'

    def __init__(self, init_pos):
        super().__init__()
        self.image = self.load_sprite()
        self.rect.height = 25
        self.rect.width = 30
        self.x = init_pos[0]
        self.rect.x = init_pos[0]
        self.y = init_pos[1]
        self.rect.y = init_pos[1]
        self.points = 100

        self.images = self.load_sprite_sheet()
        self.image_index = 0

    def load_sprite_sheet(self):
        _images = []
        sheet = spritesheet(os.path.join(vars.IMAGES_PATH, self.sheet_path))
        for x1, y1, x2, y2 in self.image_rects:
            _images.append(sheet.image_at((x1, y1, x2, y2), (255, 0, 255)))
            _images.append(sheet.image_at((x1, y1, x2, y2), (255, 0, 255)))
            _images.append(sheet.image_at((x1, y1, x2, y2), (255, 0, 255)))
        return _images

    def load_sprite(self):
        _image = pygame.image.load_extended(os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
        _image.set_colorkey((255, 0, 255), pygame.RLEACCEL)
        return _image

    def update(self, addtl_x, addtl_y):
        # self.x += addtl_x
        # self.y += addtl_y
        # self.rect.x = self.x
        # self.rect.y = self.y
        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1

    @property
    def rect(self):
        _rect = self.image.get_rect()
        _rect.x += self.x
        _rect.y += self.y
        return _rect

class Vase(LevelObject):
    breakable = 1
    broken = None

    sheet_path = 'objects/vase_sheet.png'

    def __init__(self, init_pos):
        super().__init__()
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.images = self.load_sprite_sheet(self.sheet_path, 32, 32, 8)
        self.image = self.images[0]
        self.points = 400
        self.image_index = 0

    def load_sprite_sheet(self, sheet_path, width, height, num):
        _images = []
        sheet = spritesheet(os.path.join(vars.IMAGES_PATH, sheet_path))
        for x in range(0,width*num,width):
            _images.append(sheet.image_at((x, 0, width, height), (255, 0, 255)))
            _images.append(sheet.image_at((x, 0, width, height), (255, 0, 255)))
            _images.append(sheet.image_at((x, 0, width, height), (255, 0, 255)))
        return _images

    # def load_sprite(self):
    #     _image = pygame.image.load_extended(os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
    #     _image.set_colorkey((255, 0, 255), pygame.RLEACCEL)
    #     return _image

    def update(self, addtl_x, addtl_y):
        # self.x += addtl_x
        # self.y += addtl_y

        if self.image_index >= len(self.images):
            self.broken = 2
        if self.broken == 1:
            self.image = self.images[self.image_index]
            self.image_index += 1

    @property
    def rect(self):
        _rect = self.image.get_rect()
        _rect.x += self.x
        _rect.y += self.y
        return _rect


    def get_rect(self):
        pass

class Couch(LevelObject, collide_object):
    breakable = 0
    score = 10
    image_path = 'objects/couch.png'

    def __init__(self, init_pos):
        self.image = self.load_sprite()
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])
        self.height = 1.2
        self.z = 1.2

    def load_sprite(self):
        _image = pygame.image.load_extended(os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
        _image.set_colorkey((255, 0, 255), pygame.RLEACCEL)
        return _image

    def draw(self, screen, x_offset, y_offset):
        collide_object.draw(self, screen, x_offset, y_offset)

    def get_rect(self):
        _rect = self.image.subsurface((0, 0, self.image.get_width(), self.image.get_height()-10)).get_rect()
        _rect.x += self.x
        _rect.y += self.y
        return _rect

class Table(LevelObject, collide_object):
    breakable = 0
    score = 10
    image_path = 'objects/table.png'

    def __init__(self, init_pos):
        self.image = self.load_sprite()
        LevelObject().__init__()
        collide_object.__init__(self, self.image, init_pos[0], init_pos[1])
        self.height = 1.2
        self.z = 1.2

    def load_sprite(self):
        _image = pygame.image.load_extended(os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
        _image.set_colorkey((255, 0, 255), pygame.RLEACCEL)
        return _image

    def draw(self, screen, x_offset, y_offset):
        collide_object.draw(self, screen, x_offset, y_offset)

    def get_rect(self):
        _rect = self.image.subsurface((0, 0, self.image.get_width(), self.image.get_height()-10)).get_rect()
        _rect.x += self.x
        _rect.y += self.y
        return _rect
