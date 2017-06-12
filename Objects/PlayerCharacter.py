import math

import pygame

from vars import show_velocity
import colors


class PlayerCharacter:
    def __init__(self, init_x=0, init_y=700):
        self.angle = 0
        self.speed = 0
        self.x = init_x
        self.y = init_y
        self.x_speed = 0
        self.y_speed = 0
        self.DUMMY_FLAG = False

        self.jump_state = 0  # 0 = not jumping, 1 = jumping
        self.character = None
        self.orig_sprite = None

    def set_character(self, character):
        self.character = character
        self.orig_sprite = character.sprite

    def update(self):
        if self.y_speed != 0:
            self.angle = -1 * math.atan(self.x_speed/self.y_speed) / 0.0174533

        self.x += self.x_speed

    def draw(self, screen):
        new_sprite = pygame.transform.rotate(self.orig_sprite, self.angle)
        screen.blit(new_sprite, (self.x - self.character.width / 2, self.y))
        if show_velocity:
            pygame.draw.line(screen, colors.debug_velocity_line, [self.x , self.y + self.character.width / 2],
                             [self.x + (self.x_speed*10), self.y - (self.y_speed*10) + self.character.width / 2], 3)
