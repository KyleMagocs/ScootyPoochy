import pygame

import debugcontrols
import vars
from utils.sprite_utils import image_to_surface


class collide_object(pygame.sprite.Sprite):
    collide_x_offset = 0
    collide_y_offset = 0
    width = 0

    def __init__(self, image, x, y):
        super().__init__()
        self.height = 100
        if image is not None:
            self.image_surface = image_to_surface(image)
        self.x = x
        self.y = y
        self.old_rect = self.get_collide_rect()

    def draw(self, screen, x_offset, y_offset, draw_points=False):
        if self.rect.bottom + y_offset < 0 or self.rect.top + y_offset > vars.SCREEN_HEIGHT:
            return
        self.old_rect = self.get_collide_rect()
        screen.blit(self.image_surface, (self.x + x_offset, self.y + y_offset))
        if debugcontrols.draw_rects:
            _rect = self.get_collide_rect()
            _rect.x += x_offset
            _rect.y += y_offset
            pygame.draw.rect(screen, (0, 255, 255), _rect, 1)

    def update(self, addtl_x, addtl_y):
        self.old_rect = self.get_collide_rect()

    def get_collide_rect(self):
        _rect = self.image_surface.subsurface((0, 0, self.image_surface.get_width(), self.image_surface.get_height())).get_rect()
        _rect.width = self.width
        _rect.x += self.x + self.collide_x_offset
        _rect.y += self.y + self.collide_y_offset
        return _rect

    @property
    def rect(self):
        _rect = self.get_collide_rect()
        return _rect