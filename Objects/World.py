from Objects.Player import Player


class World:
    def __init__(self, width, x_offset):
        self.width = width
        self.x_offset = x_offset * width
        self.player = Player(init_x=self.x_offset + self.width/2, init_y=700)
        self.y = 0

    def load_level(self):
        pass
        # TODO:  PARSE OUT LEVEL OBJECTS INTO LOCAL STORAGE

    def update(self):
        pass
        # TODO:  HANDLE COLLISIONS AND STUFF

    def draw(self, screen):
        self.draw_player(screen)
        # TODO:  DRAW WORLD?

    def draw_player(self, screen):
        self.player.draw(screen)
        # TODO: DRAW MY PLAYER
