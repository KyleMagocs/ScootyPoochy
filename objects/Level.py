import datetime

import pygame

from objects.LevelObjects import Lamp, Couch, Table, Vase
from objects.Room import Kitchen, DiningRoom, Garage, Backyard2
from objects.Theme import TempTheme
from objects.Wall import Wall, SideWall


class Level:
    friction = 0

    height = 0
    width = 0

    def __init__(self):
        self.theme = None
        self.objects = pygame.sprite.Group()
        self.broken_objects = pygame.sprite.Group()
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

    # def draw(self, screen, x_offset, y_offset):
    #     from timeit import default_timer as timer
    #     start = timer()
    #     screen.blit(self.theme.background_sprite, (self.x + x_offset, self.y + y_offset))
    #     end = timer()
    #     elapsed = end-start

    def build_level(self, my_doors, my_rooms):
        from objects.Room import Room_Start
        height = 0
        _im = pygame.Surface((self.width, sum([x.height for x in my_rooms])), pygame.SRCALPHA)

        floor_image = pygame.image.load_extended(Room_Start.floor_image).convert()
        _im.blit(floor_image, (0, 0))
        bglist = list()
        bglist.append((floor_image, (0, 0)))

        for room, door_x in zip(my_rooms, my_doors):
            _room = room(height)
            _room.load_wall(door_x)
            if _room.top_wall is not None:
                self.walls.add(_room.top_wall)
            self.objects.add(_room.objects)
            floor_image = pygame.image.load_extended(_room.floor_image).convert()
            for y in range(height + 136, height + _room.height + 125, floor_image.get_height()):
                _im.blit(floor_image, (0, y))
                bglist.append((floor_image, (0, y)))
            height += _room.height
        self.height = height
        self.bg = _im
        self.bglist = bglist
        _leftside = SideWall(0, 55, self.height)
        _rightside = SideWall(self.width - 55, 55, self.height)
        self.walls.add(_leftside, _rightside)

    def draw(self, screen, x_offset, y_offset):

        for bg, position in self.bglist:
            if self.y + position[1] + y_offset + bg.get_height() < 0:
                continue
            else:
                screen.blit(bg, (self.x + x_offset + position[0], self.y + y_offset + position[1]))


class TempLevel(Level):
    def __init__(self):
        super().__init__()
        self.theme = TempTheme()
        self.height = self.theme.background_sprite.get_height()
        self.width = self.theme.background_sprite.get_width()

        lamp_coords = [
            (200, 150),
            (510, -100),
            (150, -300),
            (300, -450),
            (200, -600),
            (75, -750),
            (375, -900),
            (200, -1100),
        ]
        for x, y in lamp_coords:
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


class ButtLevel(Level):
    def __init__(self):
        from objects.Room import Room_Finish, Room_One, Room_Start, Room_Two, Room_Three, Bathroom, Backyard
        super().__init__()
        self.theme = TempTheme()
        self.width = self.theme.background_sprite.get_width()

        my_rooms = Room_Finish, Room_Three, Room_One, Room_Two, Bathroom, Room_Three, Backyard, DiningRoom, Kitchen,
        my_doors = 0, 75, 75, 150, 75, 150, 350, 400, 225,

        self.build_level(my_doors, my_rooms)


class DecentLevel(Level):
    def __init__(self):
        from objects.Room import Room_Finish, Room_One, Room_Start, Room_Two, Room_Three, Bathroom, Backyard
        super().__init__()
        self.theme = TempTheme()
        self.width = self.theme.background_sprite.get_width()

        my_rooms = Room_Finish, Backyard2, Garage, Room_Two, Bathroom, Room_Three, Kitchen, DiningRoom, Room_Start
        my_doors = 0, 75, 365, 150, 75, 100, 222, 350, 225

        self.build_level(my_doors, my_rooms)


class ShortLevel(Level):
    def __init__(self):
        from objects.Room import Room_Finish, Room_One, Room_Start, Room_Two, Room_Three, Bathroom, Backyard
        super().__init__()
        self.theme = TempTheme()
        self.width = self.theme.background_sprite.get_width()

        my_rooms = Room_Finish, Room_Start
        my_doors = 0, 400

        self.build_level(my_doors, my_rooms)
