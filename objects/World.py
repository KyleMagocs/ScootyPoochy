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
        self.level.x = 0
        self.level.y = 0
        self.level.update_objects(self.x_offset)

        self.player_character = PlayerCharacter(init_x=self.x_offset + self.width / 2,
                                                init_y=y_offset)  # TODO:  This math is bad
        self.player_group = pygame.sprite.Group(self.player_character)

        self.poops = pygame.sprite.Group()

        self.timer_enabled = 0
        self.timer = 0
        self.final_timer = float('inf')

    def update(self, x_vel, y_vel):
        if self.timer_enabled:
            self.timer += 1

        old_player_rect = copy.deepcopy(
            self.player_character.rect)  # TODO:  Should really just identify the new rect beforehand and do this whole function backwards

        # todo: remove this line vvvvvvvvvv
        # x_vel = 0
        # y_vel = 0

        if self.player_character.jump_state == 0:
            self.player_character.x_speed = (self.player_character.x_speed - x_vel) / self.level.theme.friction
            self.player_character.y_speed = (self.player_character.y_speed - y_vel) / self.level.theme.friction
        self.player_character.update()
        # movepoops = 0

        if self.check_victory():
            self.final_timer = min(self.final_timer, self.timer)
            # self.player_character.y -= 10
            self.finish = True
        else:
            pass
            # TODO:  REPLACE THIS WITH RECT COLLISION
            # if self.player_character.x < self.level.x + 60:
            #     self.player_character.x = self.level.x + 60
            # if self.player_character.x > self.level.x + self.width - 60:
            #     self.player_character.x = self.level.x + self.width - 60
            #
            # if self.level.y + self.player_character.y_speed >= 0:
            #     self.level.update(addtl_x=0, addtl_y=0)
            #     self.level.y = 0
            #     self.player_character.y -= self.player_character.y_speed
            # else:
            #     self.level.update(addtl_x=0, addtl_y=0)
            #
            #     movepoops = self.player_character.y_speed
            # self.player_character.y -= self.player_character.y_speed
            # self.player_character.eff_y += self.player_character.y_speed

        if self.player_character.jump_state == 0:
            # TODO:  this should be part of the player, not the world
            self.player_character.distance_travelled += math.sqrt(x_vel * x_vel + y_vel * y_vel)

        # check object collisions
        col = pygame.sprite.groupcollide(self.level.objects, self.player_group, dokilla=False, dokillb=False)
        for sprite in col:
            if sprite.breakable and sprite.get_wrecked():
                self.break_score += sprite.points

        # TODO:  Combine this with passable non-breakable object colissions
        collide_objects = [x.get_collide_walls() for x in self.level.walls] + [x for x in self.level.objects if
                                                                               x.height > 1]
        walls = pygame.sprite.groupcollide(pygame.sprite.Group(collide_objects), self.player_group, dokilla=False,
                                           dokillb=False)

        _min_z = None
        self.level.update(addtl_x=0, addtl_y=0)

        # todo:  this is all collision, leave it alone for now
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
                self.level.update(addtl_x=0, addtl_y=0)
                # movepoops -= delta_y

                delta_x, delta_y = get_conform_deltas(wall.rect, old_player_rect, char_rect)

                self.player_character.x -= delta_x
                self.player_character.y -= delta_y

                self.player_character.distance_travelled -= math.sqrt(delta_x * delta_x + delta_y * delta_y)

        # if math.fabs(movepoops) > 1:
        #     for poop in self.player_character.poops:
        #         poop.update(0, movepoops)
        #         if poop.rect.y > vars.SCREEN_HEIGHT or poop.rect.y < 0:
        #             self.poops.remove(poop)

        if _min_z is not None:
            self.player_character.min_z = _min_z
        else:
            self.player_character.min_z = 1

        self.player_character.update_z()

        return False

    def check_victory(self):
        return False
        # if self.player_character.eff_y > -230:
        #     return True

    def draw_win_text(self, screen):
        font = pygame.font.SysFont('Impact', 70)
        text = textOutline(font, 'FINISH !', self.player_character.character.color,
                           colors.black)
        text.get_width()
        screen.blit(text, (self.x_offset + self.width / 2 - text.get_width() / 2, vars.SCREEN_HEIGHT / 2 - 10))

    def draw(self, screen):
        x_offset = self.x_offset
        y_offset = (self.level.height - self.player_character.y) - self.level.height + (vars.SCREEN_HEIGHT - vars.PLAYER_START_Y)
        self.level.draw(screen, x_offset, y_offset)

        for sprite in [x for x in self.level.walls]:
            sprite.draw_part_one(screen, x_offset, y_offset)
        for sprite in [x for x in self.level.objects]:
            sprite.draw(screen, x_offset, y_offset)

        for poop in self.player_character.poops:
            poop.draw(screen, x_offset, y_offset)
        self.player_character.draw(screen, x_offset, 0)

        for sprite in [x for x in self.level.walls]:
            sprite.draw_part_two(screen, x_offset, y_offset)

        if self.finish:
            self.draw_win_text(screen)

            # font = pygame.font.SysFont('Impact', 14)
            # label = font.render(str(self.player_character.z), 1, (0, 255, 255))
            # screen.blit(label, (self.x_offset + self.width / 4 + 2, vars.SCREEN_HEIGHT / 2 - 10 + 2))

    def start_timer(self):
        self.timer_enabled = 1

    def draw_countdown(self, screen, text, size):
        font2 = pygame.font.SysFont('Impact', size)
        label = textOutline(font2, text, self.player_character.character.color, colors.black)
        screen.blit(label, (self.x_offset + self.width / 2 - label.get_width() / 2, vars.SCREEN_HEIGHT / 2 - label.get_height() / 2))

    def get_score(self):
        return {'time': max(2000-self.final_timer, 0),
                'break': self.break_score, # todo:  maybe return a list of objects instead and then you can do something neat there?
                'poop': self.player_character.poop_score,
                'color': self.player_character.character.color}
