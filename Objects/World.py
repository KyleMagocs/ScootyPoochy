import math

from Objects.Level import Level
from Objects.Player import Player


class World:
    def __init__(self, width, x_offset):
        self.width = width
        self.x_offset = x_offset * width
        self.level = Level()  # TODO:  GENERATE / LOAD LEVEL INSTEAD OF THIS
        self.level.x = self.x_offset
        self.level.y = 0 - 1600 + 700
        self.player = Player(init_x=self.x_offset + self.width/2, init_y=700)
        self.player.set_controls(x_offset*2, x_offset*2 + 1)
        self.y = 0

    def load_level(self):
        pass
        # TODO:  PARSE OUT LEVEL OBJECTS INTO LOCAL STORAGE

    def update(self):
        # HANDLE PLAYER X DIRECTION
        self.player.update()

        # HANDLE WORLD Y DIRECTION
        #_update_y = max(0, math.cos(self.player.angle * 0.0174533) * self.player.speed)  # 0.0174533 = rad convert
        if self.player.x < self.level.x:
            self.player.x = 0
        if self.player.x > self.level.x + self.width:
            self.player.x = self.level.x + self.width
        self.y += self.player.y_speed
        self.level.update(addtl_x=0, addtl_y=self.player.y_speed)

        # HANDLE COLLISIONS
        # TODO:  HANDLE COLLISIONS AND STUFF

    def draw(self, screen):
        self.level.draw(screen)
        self.player.draw(screen)
        # TODO:  DRAW WORLD?
