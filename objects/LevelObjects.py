import os

import pygame

import vars


class LevelObject(pygame.sprite.Sprite):
    breakable = 0  # 1 for breakable objects
    broken = 0  # 1 = breaking, 2 = broken
    passable = 1 #
    image_path = None

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.rect = None

    def get_wrecked(self):
        if self.breakable and not self.broken:
            self.broken = 1
            self.image = pygame.transform.rotate(self.image, -90)

    def draw(self, screen):
        if self.rect.y + self.rect.height < 0 or self.rect.y - self.image.get_height() > vars.SCREEN_HEIGHT:
            return
        screen.blit(self.image, (self.rect.x, self.rect.y - self.image.get_height() + self.rect.height))
        if vars.draw_rects:
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 1)   #


class Lamp(LevelObject):
    breakable = 1
    broken = None
    score = 10

    image_rects = (
        (1, 2, 3, 4),
    )

    image_path = 'objects/lamp.png'
    def __init__(self, init_pos):
        super().__init__()
        self.image = self.load_sprite()
        self.rect = self.image.get_rect()
        self.rect.height = 25
        self.rect.width = 30
        self.x = init_pos[0]
        self.y = init_pos[1]
        self.images = self.load_sprite_sheet()
        self.image_index = 0

    def load_sprite_sheet(self):
        _images = []
        for x1, y1, x2, y2 in self.image_rects:
            _images.append(None)  # TODO:  Spritesheet
        return _images

    def load_sprite(self):
        _image = pygame.image.load_extended(os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
        _image.set_colorkey((255, 0, 255), pygame.RLEACCEL)
        return _image

    def update(self, addtl_x, addtl_y):
        self.x += addtl_x
        self.y += addtl_y
        self.rect.x = self.x
        self.rect.y = self.y
        if self.broken == 1:
            pass
            # self.image = self.images[self.image_index]
            # self.image_index += 1
        if self.image_index > len(self.images):
            self.broken = 2

    def get_rect(self):
        pass


class Couch(LevelObject):
    breakable = 0
    score = 10

    image_path = 'objects/couch.png'

    def __init__(self, init_pos):
        super().__init__()
        self.image = self.load_sprite()
        self.rect = self.image.get_rect()
        self.rect.height = 275
        self.rect.width = 75
        self.x = init_pos[0]
        self.y = init_pos[1]

    def load_sprite(self):
        _image = pygame.image.load_extended(os.path.join(vars.IMAGES_PATH, self.image_path)).convert()  # Todo:  need a full sprite sheet, yeah?
        _image.set_colorkey((255, 0, 255), pygame.RLEACCEL)
        return _image

    def update(self, addtl_x, addtl_y):
        self.x += addtl_x
        self.y += addtl_y
        self.rect.x = self.x
        self.rect.y = self.y

    def get_rect(self):
        pass

