import math

import pygame

import colors
from vars import radians_factor
import vars
from colors import selected_character_colors



class CharacterSelectCharacter(pygame.sprite.Sprite):
    def __init__(self, character, init_angle, offset_x, offset_y, min_angle, max_angle ):
        self.flash_factor = 3

        super().__init__()
        self.character = character
        self.character.load_portrait()
        self.orig_sprite = self.character.portrait
        self.current_sprite = self.orig_sprite
        self.init_angle = init_angle
        self.angle = init_angle
        self.scale = 0.4
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.transparency = 0
        self.radius = 1
        self.x = 0
        self.y = 0
        self.selected = False
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.selected_color_flag = 0

    def update(self, angle_offset):
        self.angle = (self.init_angle + angle_offset) % 360
        if self.min_angle < self.angle < self.max_angle:
            self.selected = True
            if self.angle < int((self.min_angle + self.max_angle)/2):
                ratio = (self.angle - self.min_angle) / ((self.min_angle + self.max_angle)/2)
            elif self.angle >= int((self.min_angle + self.max_angle)/2):
                ratio = math.fabs(self.angle - self.max_angle) / ((self.min_angle + self.max_angle) / 2)

            self.scale = 0.4 + (ratio)
        else:
            self.selected = False
            self.scale = 0.4
        self.current_sprite = pygame.transform.scale(self.orig_sprite, (int(self.scale * self.orig_sprite.get_width()),
                                                                        int(self.scale * self.orig_sprite.get_height())))

        self.x = math.cos(self.angle * radians_factor) * self.radius + self.offset_x - (self.current_sprite.get_width() / 2)
        self.y = math.sin(self.angle * radians_factor) * self.radius + self.offset_y - (self.current_sprite.get_height() / 2)

    def draw(self, screen):
        _rect = self.current_sprite.get_rect()
        _rect.x = self.x
        _rect.y = self.y
        pygame.draw.rect(screen, colors.black, _rect, 0)
        screen.blit(self.current_sprite, (self.x, self.y))

        if self.selected and int(self.selected_color_flag / self.flash_factor) == 0:
            pygame.draw.rect(screen, self.character.color, (self.x, self.y, self.current_sprite.get_width(), self.current_sprite.get_height()), 6)

        else:
            pygame.draw.rect(screen, (150, 150, 150), (self.x, self.y, self.current_sprite.get_width(), self.current_sprite.get_height()), 4)

        self.selected_color_flag = (self.selected_color_flag + 1) % (self.flash_factor * 2)

    @property
    def width(self):
        return self.current_sprite.get_width()

    @property
    def height(self):
        return self.current_sprite.get_height()