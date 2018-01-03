import os

import pygame

from objects.LevelObjects import Lamp, Table, Couch, Vase, Cuckoo, HDTV, BookShelf
from objects.LevelObjects_Backyard import Gnome, BirdBath, Grill, Flower1, Flower2, Flower3, Flower4
from objects.LevelObjects_Bathroom import BathroomSink, Shower, Toilet, SinkStuff, BathMat
from objects.LevelObjects_Garage import ScootPooch, Workbench, WaterHeater, PaintCans, Saw
from objects.Wall import Wall, BathroomWall, BackyardWall, KitchenWall, GarageWall

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
            Lamp((535, 70), True),
            Table((100, 100)),
            Cuckoo((200, 50)),
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
            Cuckoo((275, 50)),
        )
        super().__init__(y_position)


class Bathroom(Room):
    height = 350
    floor_image = os.path.join(ASSETS_PATH, 'bathroom_bg.png')

    def __init__(self, y_position):
        self.objects = pygame.sprite.Group(
            Shower((0, 32)),
            BathroomSink((170, 80)),
            SinkStuff((170, 73)),
            Toilet((295, 90)),
            BathMat((200, 230))
        )
        super().__init__(y_position)

    def load_wall(self, door_x):
        self.top_wall = BathroomWall(0, self.y_position, door_x)


class Kitchen(Room):
    height = 400
    floor_image = os.path.join(ASSETS_PATH, 'kitchen_bg.png')

    def __init__(self, y_position):
        from objects.LevelObjects_Kitchen import Stove
        from objects.LevelObjects_Kitchen import Oven
        from objects.LevelObjects_Kitchen import Counter
        from objects.LevelObjects_Kitchen import Bottle
        self.objects = pygame.sprite.Group(
            Counter((55, 110,)),
            Bottle((60, 90)),
            Stove((160, 105)),
            Oven((160, 132)),

        )
        super().__init__(y_position)

    def load_wall(self, door_x):
        self.top_wall = KitchenWall(0, self.y_position, door_x)

class DiningRoom(Room):
    height = 500
    floor_image = os.path.join(ASSETS_PATH, 'dining_bg.png')

    def __init__(self, y_position):
        from objects.LevelObjects_DiningRoom import DiningTable, Chair, Candle, Painting_One, Painting_Two, Plate
        self.objects = pygame.sprite.Group(
            Chair((370, 180),),
            Chair((240, 180), mirror = True),
            Chair((370, 300),),
            Chair((240, 300), mirror = True),
            DiningTable((300-DiningTable.width/2, 200,)),
            Candle((210, 150)),
            Candle((275, 250), mirror=True),
            Plate((325, 180)),
            Plate((325, 300)),
            Plate((275, 180), mirror = True),
            Plate((275, 300), mirror = True),

            Painting_Two((300, 40)),
            Painting_One((450, 40)),
        )
        super().__init__(y_position)

    def load_wall(self, door_x):
        self.top_wall = KitchenWall(0, self.y_position, door_x)


class Backyard(Room):
    height = 500

    floor_image = os.path.join(ASSETS_PATH, 'backyard_bg.png')

    def __init__(self, y_position):
        self.objects = pygame.sprite.Group(
            Grill((100, 260)),
            Flower2((355, 75)),
            Flower1((400, 80)),
            Flower3((465, 115)),
            Flower4((425, 60)),
            Gnome((300, 230)),
            Gnome((280, 270)),
            BirdBath((430, 300)),
        )
        super().__init__(y_position)

    def load_wall(self, door_x):
        self.top_wall = BackyardWall(0, self.y_position, door_x)


class Garage(Room):
    height = 600
    floor_image = os.path.join(ASSETS_PATH, 'garage_bg.png')

    def __init__(self, y_position):

        self.objects = pygame.sprite.Group(
            WaterHeater((10, 20)),
            Workbench((225, 115)),
            ScootPooch((385, 25)),
            PaintCans((234, 20)),
            Saw((240, 80)),

        )
        super().__init__(y_position)

    def load_wall(self, door_x):
        self.top_wall = GarageWall(0, self.y_position, door_x)


class Room_Start(Room):
    objects = pygame.sprite.Group()
    height = 800


class Room_Finish(Room):
    height = 400
    floor_image = os.path.join(ASSETS_PATH, 'finish_bg_temp.png')
    objects = pygame.sprite.Group()

    def load_wall(self, door_x):
        self.top_wall = None
