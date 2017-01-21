import math

import pygame


class Player:
    def __init__(self, init_x=0, init_y=700):
        self.angle = 0
        self.speed = 0
        self.x = init_x
        self.y = init_y

        self.jump_state = 0  # 0 = not jumping, 1 = jumping
        self.character = None
        self.orig_sprite = None

    def set_character(self, character):
        self.character = character
        self.orig_sprite = character.sprite

    def update(self):
        if self.angle > 30:
            self.angle = 30
        if self.angle < -30:
            self.angle = -30
        self.x += math.sin(self.angle) * self.speed

    def draw(self, screen):
        new_sprite = pygame.transform.rotate(self.orig_sprite, self.angle)
        screen.blit(new_sprite, (self.x-self.character.width/2, self.y))
