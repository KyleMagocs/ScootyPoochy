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

    def update(self, x_vel, y_vel):
        # HANDLE PLAYER X DIRECTION

        self.player_character.x_speed = (self.player_character.x_speed - x_vel) / self.level.theme.friction
        self.player_character.y_speed = (self.player_character.y_speed + y_vel) / self.level.theme.friction

        self.player_character.update()

        # HANDLE WORLD Y DIRECTION
        if self.player_character.x < self.level.x + 60:
            self.player_character.x = self.level.x + 60
        if self.player_character.x > self.level.x + self.width - 60:
            self.player_character.x = self.level.x + self.width - 60
        if self.level.y + self.player_character.y_speed >= 0:
            #self.y = 0
            self.level.update(addtl_x=0, addtl_y=0)
            self.player_character.y -= self.player_character.y_speed
        else:
            #self.y += self.player_character.y_speed
            self.level.update(addtl_x=0, addtl_y=self.player_character.y_speed)
        #
        # self.y += self.player_character.y_speed
        # self.level.update(addtl_x=0, addtl_y=self.player_character.y_speed)


        # HANDLE COLLISIONS

        col = pygame.sprite.groupcollide(self.level.objects, self.player_group, dokilla=False, dokillb=False)

        for sprite in col:
            if sprite.breakable and sprite.get_wrecked():
                self.score += sprite.score

        if self.check_victory():
            return True

        return False

    def check_victory(self):
        return False

    def draw(self, screen):
        self.level.draw(screen)
        self.player_character.draw(screen)
