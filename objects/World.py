import copy
import pygame

import colors
import vars
from objects.Characters import PoopTrail
from sprites.PlayerCharacter import PlayerCharacter
import math

from utils.hollow import textOutline


class World:
    def __init__(self, width, x_offset, y_offset, level):
        self.width = width
        self.x_offset = x_offset * width
        self.score = 0

        self.finish = False

        self.level = level
        self.level.x = self.x_offset
        self.level.y = 0 - self.level.height + y_offset
        self.level.update_objects(self.x_offset)

        self.player_character = PlayerCharacter(init_x=self.x_offset + self.width / 2,
                                                init_y=y_offset)  # TODO:  This math is bad
        self.player_group = pygame.sprite.Group(self.player_character)
        self.player_character.eff_y = 0 - self.level.height

        self.poops = pygame.sprite.Group()

        # self.y = 0

    def load_level(self):
        pass
        # TODO:  PARSE OUT LEVEL OBJECTS INTO LOCAL STORAGE

    def update(self, x_vel, y_vel):
        # HANDLE PLAYER X DIRECTION

        old_player_rect = copy.deepcopy(self.player_character.rect)  # TODO:  Should really just identify the new rect beforehand and do this whole function backwards

        self.player_character.x_speed = (self.player_character.x_speed - x_vel) / self.level.theme.friction
        self.player_character.y_speed = (self.player_character.y_speed + y_vel) / self.level.theme.friction
        self.player_character.update()

        if self.check_victory():
            self.player_character.y -= 10
            self.finish = True
        else:
            # HANDLE WORLD Y DIRECTION
            # TODO:  REPLACE THIS WITH RECT COLLISION
            if self.player_character.x < self.level.x + 60:
                self.player_character.x = self.level.x + 60
            if self.player_character.x > self.level.x + self.width - 60:
                self.player_character.x = self.level.x + self.width - 60
            #######

            if self.level.y + self.player_character.y_speed >= 0:
                # self.y = 0
                self.level.update(addtl_x=0, addtl_y=0)
                self.level.y = 0
                self.player_character.y -= self.player_character.y_speed
            else:
                # self.y += self.player_character.y_speed
                self.level.update(addtl_x=0, addtl_y=self.player_character.y_speed)
                for poop in self.player_character.poops:
                    poop.update(0, self.player_character.y_speed)
                    if poop.rect.y > vars.SCREEN_HEIGHT or poop.rect.y < 0:
                        self.poops.remove(poop)
            self.player_character.eff_y += self.player_character.y_speed
        self.player_character.distance_travelled += math.sqrt(x_vel * x_vel + y_vel * y_vel)

        # check object collisions
        col = pygame.sprite.groupcollide(self.level.objects, self.player_group, dokilla=False, dokillb=False)
        for sprite in col:
            if sprite.breakable and sprite.get_wrecked():
                self.score += sprite.score

                # check object collisions

        walls = pygame.sprite.groupcollide(pygame.sprite.Group([x.get_collide_walls() for x in self.level.walls]), self.player_group, dokilla=False, dokillb=False)
        for wall in walls:
            old_rect = wall.old_rect
            new_rect = wall.rect
            char_rect = self.player_character.rect
            delta_x, delta_y = self.get_conform_deltas(char_rect, old_rect, new_rect)
            self.player_character.eff_y -= delta_y
            self.level.update(addtl_x=0, addtl_y=0 - delta_y)
            for poop in self.player_character.poops:
                poop.update(0, 0 - delta_y)  # todo:  the poop kinda vibrates when you walk it back ...

            delta_x, delta_y = self.get_conform_deltas(wall.rect, old_player_rect, char_rect)
            self.player_character.x -= delta_x
            self.player_character.rect.x -= delta_x

        return False

    def get_conform_deltas(self, obstacle, old, new):
        delta_x = 0
        delta_y = 0
        if old.right <= obstacle.left < new.right:
            delta_x = new.right - obstacle.left
        if old.left >= obstacle.right > new.left:
            delta_x = new.left - obstacle.right
        if old.bottom <= obstacle.top < new.bottom:
            delta_y = new.bottom - obstacle.top
        if old.top >= obstacle.bottom > new.top:
            delta_y = new.top - obstacle.bottom

        return delta_x, delta_y

    def check_victory(self):
        if self.player_character.eff_y > -230:
            return True

    def draw_win_text(self, screen):
        font = pygame.font.SysFont('Impact', 70)
        text = textOutline(font, 'FINISH !', self.player_character.character.color,
                           colors.black)
        text.get_width()
        screen.blit(text, (self.x_offset + self.width / 2 - text.get_width() / 2, vars.SCREEN_HEIGHT / 2 - 10))

    def draw(self, screen):
        self.level.draw(screen)
        self.player_character.poops.draw(screen)

        for sprite in [x for x in self.level.walls]:
            sprite.draw_part_one(screen)
        for sprite in [x for x in self.level.objects if x.y < self.player_character.y]:
            sprite.draw(screen)

        self.player_character.draw(screen)

        for sprite in [x for x in self.level.objects if x.y >= self.player_character.y]:
            sprite.draw(screen)
        for sprite in [x for x in self.level.walls]:
            sprite.draw_part_two(screen)

        if self.finish:
            self.draw_win_text(screen)

        font = pygame.font.SysFont('Impact', 14)
        # label = font.render(str(self.player_character.distance_travelled), 1, (255, 255, 255))
        # screen.blit(label, (self.x_offset + self.width / 4 + 2, vars.SCREEN_HEIGHT / 2 - 10 + 2))

    def draw_countdown(self, screen, text, size):
        font2 = pygame.font.SysFont('Impact', size)
        label = textOutline(font2, text, self.player_character.character.color, colors.black)
        screen.blit(label, (self.x_offset + self.width / 2 - label.get_width() / 2, vars.SCREEN_HEIGHT / 2 - label.get_height()/2))
