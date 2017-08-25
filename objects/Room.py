import os

import pygame

from objects.LevelObjects import Lamp, Table, Couch, Vase, Cuckoo, HDTV, BookShelf, Shower
from objects.Wall import Wall, BathroomWall

ASSETS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'images', 'level_assets')

def load_wall():
    # todo: better
    return Wall(0, 0, 50)

class Room:
    objects = None
    height = 400

    top_entrance_valid = 0b000
    bottom_entrance_valid = 0b000

    floor_image = os.path.join(ASSETS_PATH, 'room_bg_temp.png')

    top_wall = None

    def __init__(self, y_position):
        self.y_position = y_position
        for obj in self.objects:
            obj.y += y_position

    def load_wall(self, door_x):
        self.top_wall = Wall(0, self.y_position, door_x)


class Room_One(Room):
    height = 400

    def __init__(self, y_position):
        self.objects = pygame.sprite.Group(
            Lamp((65, 70)),
            Lamp((535, 70)),
            Table((100, 100)),
            Cuckoo((200, 150)),
            Vase((175, 170))
        )
        super().__init__(y_position)

class Room_Two(Room):
    height = 400

    def __init__(self, y_position):
        self.objects = pygame.sprite.Group(
            Lamp((65, 70)),
            Lamp((515, 70), True),
            Couch((475, 180)),
            HDTV((100, 30)),
        )
        super().__init__(y_position)

class Room_Three(Room):
    height = 400

    def __init__(self, y_position):
        self.objects = pygame.sprite.Group(
            Lamp((65, 70)),
            BookShelf((150, 65)),
            Cuckoo((475, 50)),
        )
        super().__init__(y_position)

class Bathroom(Room):
    height = 350

    floor_image = os.path.join(ASSETS_PATH, 'bathroom_bg.png')
    objects = pygame.sprite.Group(
        Shower((0, 32)),
    )

    def load_wall(self, door_x):
        self.top_wall = BathroomWall(0, self.y_position, door_x)

class Room_Start(Room):
    objects = pygame.sprite.Group()
    height = 800


class Room_Finish(Room):
    height = 400
    floor_image = os.path.join(ASSETS_PATH, 'finish_bg_temp.png')
    objects = pygame.sprite.Group()

    def load_wall(self, door_x):
        self.top_wall = None