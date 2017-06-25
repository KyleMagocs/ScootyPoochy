import pygame

from sprites.PlayerCharacter import PlayerCharacter


class World:
    def __init__(self, width, x_offset, y_offset, level):
        self.width = width
        self.x_offset = x_offset * width
        self.score = 0
        self.level = level
        self.level.x = self.x_offset
        self.level.update_objects(self.x_offset)
        self.level.y = 0 - self.level.height + y_offset
        self.player_character = PlayerCharacter(init_x=self.x_offset + self.width / 2, init_y=y_offset) # TODO:  This math is bad
        self.player_group = pygame.sprite.Group(self.player_character)
        self.y = 0

    def load_level(self):
        pass
        # TODO:  PARSE OUT LEVEL OBJECTS INTO LOCAL STORAGE

    def update(self):
        # HANDLE PLAYER X DIRECTION
        self.player_character.update()

        # HANDLE WORLD Y DIRECTION
        if self.player_character.x < self.level.x:
            self.player_character.x = self.level.x
        if self.player_character.x > self.level.x + self.width:
            self.player_character.x = self.level.x + self.width
        self.y += self.player_character.y_speed
        self.level.update(addtl_x=0, addtl_y=self.player_character.y_speed)

        # HANDLE COLLISIONS

        col = pygame.sprite.groupcollide(self.level.objects, self.player_group, dokilla=False, dokillb=True)

        for sprite in col:
            if sprite.get_wrecked():
                self.score += 1

        if self.check_victory():
            return True

        return False

    def check_victory(self):
        return False

    def draw(self, screen):
        self.level.draw(screen)
        self.player_character.draw(screen)
