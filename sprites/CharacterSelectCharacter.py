import math

import pygame

from vars import radians_factor


class CharacterSelectCharacter(pygame.sprite.Sprite):
    def __init__(self, character, init_angle):
        super().__init__()
        self.character = character
        self.character.load_portrait()
        self.orig_sprite = self.character.portrait
        self.current_sprite = self.orig_sprite
        self.angle = init_angle
        self.scale = 0.25
        self.x = 0
        self.y = 0

    def update(self):
        if self.angle < 30 or self.angle > 330 or (self.angle > 150 and self.angle < 210):
            self.scale = max(math.fabs(math.cos(self.angle * 3 % 180 * radians_factor)), 0.25)
        self.current_sprite = pygame.transform.scale(self.orig_sprite, (int(self.scale * self.orig_sprite.get_width()), int(self.scale * self.orig_sprite.get_height())))

    def draw(self, screen):
        screen.blit(self.current_sprite, (self.x, self.y))