import pygame

from objects.LevelObjects import Lamp, Couch
from objects.Theme import TempTheme


class Level:
    friction = 0

    height = 0
    width = 0

    def __init__(self):
        self.theme = None
        self.objects = pygame.sprite.Group()
        self.y = 0
        self.x = 0

    def update(self, addtl_x, addtl_y):
        self.objects.update(addtl_x, addtl_y)
        self.x += addtl_x
        self.y += addtl_y

    def update_objects(self, x_offset):
        for object in self.objects.sprites():
            object.x += x_offset

    def draw(self, screen):
        screen.blit(self.theme.background_sprite, (self.x, self.y))

        for sprite in self.objects.sprites():
            sprite.draw(screen)

        # self.objects.draw(screen)

        # draw background at x, y
        # iterate through my_objects and draw each (pass camera x and camera y so they don't draw if they don't need to)


class TempLevel(Level):
    def __init__(self):
        super().__init__()
        self.theme = TempTheme()
        self.height = self.theme.background_sprite.get_height()
        self.width = self.theme.background_sprite.get_width()

        lamp_coords = [
            (200,200),
            (400,-100),
            (150,-250),
            (300,-400),
            (200,-550),
            (75,-700),
            (375,-900),
            (200,-1100),
        ]
        for x,y in lamp_coords:
            _lamp = Lamp((x, y,))
            self.objects.add(_lamp)  # TODO:  Yank later


        _couch = Couch((480, -50))
        self.objects.add(_couch)  # TODO:  Yank later
