import pygame

from objects.LevelObjects import Lamp, Couch, Table, Vase
from objects.Theme import TempTheme
from objects.Wall import Wall, SideWall


class Level:
    friction = 0

    height = 0
    width = 0

    def __init__(self):
        self.theme = None
        self.objects = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.y = 0
        self.x = 0

    def update(self, addtl_x, addtl_y):
        self.objects.update(addtl_x, addtl_y)
        self.walls.update(addtl_x, addtl_y)
        self.x += addtl_x
        self.y += addtl_y

    def update_objects(self, x_offset):
        for object in self.objects.sprites():
            object.x += x_offset
        for wall in self.walls.sprites():
            wall.update(x_offset, 0)

    def draw(self, screen, x_offset, y_offset):
        screen.blit(self.theme.background_sprite, (self.x + x_offset, self.y + y_offset))

class TempLevel(Level):
    def __init__(self):
        super().__init__()
        self.theme = TempTheme()
        self.height = self.theme.background_sprite.get_height()
        self.width = self.theme.background_sprite.get_width()

        lamp_coords = [
            (200,150),
            (510,-100),
            (150,-300),
            (300,-450),
            (200,-600),
            (75,-750),
            (375,-900),
            (200,-1100),
        ]
        for x,y in lamp_coords:
            _lamp = Lamp((x, y,))
            self.objects.add(_lamp)  # TODO:  Yank later

        _wall = Wall(0, 2400, 75)
        self.walls.add(_wall)

        _wall = Wall(0, 1400, 300)
        self.walls.add(_wall)

        _wall = Wall(0, 900, 150)
        self.walls.add(_wall)

        _leftside = SideWall(0, 55, self.height)
        _rightside = SideWall(self.width - 55, 55, self.height)
        self.walls.add(_leftside, _rightside)

        _couch = Couch((475, 2570))
        self.objects.add(_couch)  # TODO:  Yank later

        _table = Table((100, 2600))
        self.objects.add(_table)  # TODO:  Yank later

        _vase = Vase((300, 2900,))
        self.objects.add(_vase)

        _vase2 = Vase((175, 2775,))
        self.objects.add(_vase2)
