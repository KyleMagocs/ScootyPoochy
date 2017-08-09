import copy
import math

import pygame

import colors
import vars
from sprites.PlayerCharacter import PlayerCharacter
from utils.hollow import textOutline
from utils.sprite_utils import get_conform_deltas


class World:
    def __init__(self, width, x_offset, y_offset, level):
        self.width = width
        self.x_offset = x_offset * width
        self.break_score = 0

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

    def update(self, x_vel, y_vel):
        old_player_rect = copy.deepcopy(self.player_character.rect)  # TODO:  Should really just identify the new rect beforehand and do this whole function backwards

        if self.player_character.jump_state == 0:
            self.player_character.x_speed = (self.player_character.x_speed - x_vel) / self.level.theme.friction
            self.player_character.y_speed = (self.player_character.y_speed + y_vel) / self.level.theme.friction
        self.player_character.update()
        movepoops = 0

        if self.check_victory():
            self.player_character.y -= 10
            self.finish = True
        else:
            # TODO:  REPLACE THIS WITH RECT COLLISION
            if self.player_character.x < self.level.x + 60:
                self.player_character.x = self.level.x + 60
            if self.player_character.x > self.level.x + self.width - 60:
                self.player_character.x = self.level.x + self.width - 60

            if self.level.y + self.player_character.y_speed >= 0:
                self.level.update(addtl_x=0, addtl_y=0)
                self.level.y = 0
                self.player_character.y -= self.player_character.y_speed
            else:
                self.level.update(addtl_x=0, addtl_y=self.player_character.y_speed)
                movepoops = self.player_character.y_speed

            self.player_character.eff_y += self.player_character.y_speed

        if self.player_character.jump_state == 0:
            self.player_character.distance_travelled += math.sqrt(x_vel * x_vel + y_vel * y_vel)

        # check object collisions
        col = pygame.sprite.groupcollide(self.level.objects, self.player_group, dokilla=False, dokillb=False)
        for sprite in col:
            if sprite.breakable and sprite.get_wrecked():
                self.break_score += sprite.score

        # TODO:  Combine this with passable non-breakable object colissions
        collide_objects = [x.get_collide_walls() for x in self.level.walls] + [x for x in self.level.objects if x.height > 1]
        walls = pygame.sprite.groupcollide(pygame.sprite.Group(collide_objects), self.player_group, dokilla=False, dokillb=False)
        _min_z = None
        for wall in walls:
            if wall.height <= self.player_character.z:
                if _min_z is None:
                    _min_z = wall.height
                _min_z = min(_min_z, wall.height)
            else:
                # pass
                old_rect = wall.old_rect
                new_rect = wall.rect
                char_rect = self.player_character.rect

                delta_x, delta_y = get_conform_deltas(char_rect, old_rect, new_rect)
                self.player_character.eff_y -= delta_y
                self.level.update(addtl_x=0, addtl_y=0 - delta_y)
                movepoops -= delta_y

                delta_x, delta_y = get_conform_deltas(wall.rect, old_player_rect, char_rect)

                self.player_character.x -= delta_x
                self.player_character.rect.x -= delta_x

                self.player_character.distance_travelled -= math.sqrt(delta_x*delta_x + delta_y*delta_y)


        if math.fabs(movepoops) > 1:
            for poop in self.player_character.poops:
                poop.update(0, movepoops)
                if poop.rect.y > vars.SCREEN_HEIGHT or poop.rect.y < 0:
                    self.poops.remove(poop)

        if _min_z is not None:
            self.player_character.min_z = _min_z
        else:
            self.player_character.min_z = 1

        self.player_character.update_z()

        return False

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

        for sprite in [x for x in self.level.walls]:
            sprite.draw_part_one(screen)
        for sprite in [x for x in self.level.objects]:
            sprite.draw(screen)

        self.player_character.poops.draw(screen)
        self.player_character.draw(screen)
        #
        # for sprite in [x for x in self.level.objects if x.height > self.player_character.z]:
        #     sprite.draw(screen)
        for sprite in [x for x in self.level.walls]:
            sprite.draw_part_two(screen)

        if self.finish:
            self.draw_win_text(screen)

        font = pygame.font.SysFont('Impact', 14)
        label = font.render(str(self.player_character.z), 1, (0, 255, 255))
        screen.blit(label, (self.x_offset + self.width / 4 + 2, vars.SCREEN_HEIGHT / 2 - 10 + 2))

    def draw_countdown(self, screen, text, size):
        font2 = pygame.font.SysFont('Impact', size)
        label = textOutline(font2, text, self.player_character.character.color, colors.black)
        screen.blit(label, (self.x_offset + self.width / 2 - label.get_width() / 2, vars.SCREEN_HEIGHT / 2 - label.get_height()/2))
