from Objects.Player import Player


class World:
    def __init__(self, x_offset):
        self.Player = None
        self.x_offset = x_offset
        self.y = 0

    def load_level(self):
        pass
        # TODO:  PARSE OUT LEVEL OBJECTS INTO LOCAL STORAGE

    def update(self):
        pass
        # TODO:  HANDLE COLLISIONS AND STUFF

    def draw(self):
        pass
        # TODO:  DRAW WORLD?