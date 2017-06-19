import os

IMAGES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'images', 'level_objects')


class LevelObject:
    breakable = 0  # 1 for breakable objects
    broken = 0  # 1 to trigger broken state

    image_path = None

    def __init__(self):
        pass

    def get_wrecked(self):
        if self.breakable:
            self.broken = 1

    def draw(self, screen):
        pass


class Lamp(LevelObject):
    breakable = 1
    broken = None

    image_path = 'lamp.png'

    def __init__(self):
        LevelObject.__init__(self)


class Couch(LevelObject):
    breakable = 0

    image_path = 'couch.png'

    def __init__(self):
        LevelObject.__init__(self)

