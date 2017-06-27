import math

import pygame

from utils.sprite_utils import rot_center
from vars import show_velocity, draw_rects
import colors


class PlayerCharacter(pygame.sprite.Sprite):
    def __init__(self, init_x=0, init_y=700):
        super().__init__()
        self.angle = 0
        self.speed = 0
        self.x = init_x
        self.y = init_y
        self.eff_y = 0  # used for tracking effective y (because real y is static)
        self.x_speed = 0
        self.y_speed = 0
        self.DUMMY_FLAG = False

        self.jump_state = 0  # 0 = not jumping, 1 = jumping
        self.character = None
        self.orig_sprite = None

    def set_character(self, character):
        self.character = character
        self.orig_sprite = character.sprite
        self.rect = self.orig_sprite.get_rect()

    def update(self):
        if self.y_speed != 0:
            self.angle = -1 * math.atan(self.x_speed/self.y_speed) / 0.0174533
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        _image = rot_center(self.orig_sprite, self.angle)
        screen.blit(_image, (self.rect.x, self.rect.y))
        if show_velocity:
            pygame.draw.line(screen, colors.debug_velocity_line, [self.x + self.character.width / 2, self.y + self.character.height / 2],
                             [self.x + (self.x_speed*15) + self.character.width / 2,
                              self.y - (self.y_speed*15) + self.character.height / 2], 3)
        if draw_rects:
            pygame.draw.rect(screen, self.character.color, self.rect, 1)   #
