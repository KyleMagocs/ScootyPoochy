import math

import pygame

from vars import radians_factor
import vars
from colors import selected_character_colors

class CharacterSelectCharacter(pygame.sprite.Sprite):
    def __init__(self, character, init_angle, offset_x, offset_y):
        super().__init__()
        self.character = character
        self.character.load_portrait()
        self.orig_sprite = self.character.portrait
        self.current_sprite = self.orig_sprite
        self.angle = init_angle
        self.scale = 0.25
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.transparency = 0
        self.radius = 1
        self.x = 0
        self.y = 0
        self.selected = False

    def update(self):
        if self.angle < 30 or self.angle > 330 or (150 < self.angle < 210):
            self.scale = max(math.fabs(math.cos(self.angle * 3 % 180 * radians_factor)), 0.25)
            self.scale = min(self.scale, self.radius / 342)  # TODO:  Scary magic numbers ~
        self.current_sprite = pygame.transform.scale(self.orig_sprite, (int(self.scale * self.orig_sprite.get_width()), int(self.scale * self.orig_sprite.get_height())))

        self.x = math.cos(self.angle * radians_factor) * self.radius + self.offset_x - (self.current_sprite.get_width() / 2)
        self.y = math.sin(self.angle * radians_factor) * self.radius + self.offset_y - (self.current_sprite.get_height() / 2)

    def draw(self, screen):
        screen.blit(self.current_sprite, (self.x, self.y))

        if self.selected:
            # draw rectangle
            pygame.draw.rect(screen, selected_character_colors[vars.selected_character_color_index],
                             (self.x, self.y, self.current_sprite.get_width(), self.current_sprite.get_height()), 6)  # TODO:  This is terrible

        else:
            pygame.draw.rect(screen, (150, 150, 150),
                             (self.x, self.y, self.current_sprite.get_width(), self.current_sprite.get_height()),
                             4)  # TODO:  This is terrible