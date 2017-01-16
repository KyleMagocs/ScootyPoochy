import os

import pygame

IMAGES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'temp_images')


class CharacterBase:
    sprite_path = None
    sprite = None
    max_speed = 20
    poop_factor = .5

    def __init__(self):
        self.load_sprite()

    def load_sprite(self):
        if self.sprite_path is not None:
            self.sprite = pygame.image.load(os.path.join(IMAGES_PATH, self.sprite_path))


class TestCharacter(CharacterBase):
    sprite_path = 'player.png'
    max_speed = 20
    width = 60

    def __init__(self):
        CharacterBase.__init__(self)
        self.load_sprite()
