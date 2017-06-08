from Objects.Level import Level
from Objects.PlayerCharacter import PlayerCharacter


class World:
    def __init__(self, width, x_offset):
        self.width = width
        self.x_offset = x_offset * width
        self.level = Level()  # TODO:  GENERATE / LOAD LEVEL INSTEAD OF THIS
        self.level.x = self.x_offset
        self.level.y = 0 - 1600 + 700
        self.player_character = PlayerCharacter(init_x=self.x_offset + self.width / 2, init_y=700) # TODO:  This math is bad
        self.player_character.set_controls(x_offset * 2, x_offset * 2 + 1)
        self.y = 0

    def load_level(self):
        pass
        # TODO:  PARSE OUT LEVEL OBJECTS INTO LOCAL STORAGE

    def update(self):
        # HANDLE PLAYER X DIRECTION
        self.player_character.update()

        # HANDLE WORLD Y DIRECTION
        if self.player_character.x < self.level.x:
            self.player_character.x = 0
        if self.player_character.x > self.level.x + self.width:
            self.player_character.x = self.level.x + self.width
        self.y += self.player_character.y_speed
        self.level.update(addtl_x=0, addtl_y=self.player_character.y_speed)

        # HANDLE COLLISIONS
        # TODO:  HANDLE COLLISIONS AND STUFF

    def draw(self, screen):
        self.level.draw(screen)
        self.player_character.draw(screen)
        # TODO:  DRAW STUFF?
