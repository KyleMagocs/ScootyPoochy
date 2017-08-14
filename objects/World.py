import copy
import math

import pygame

import colors
import vars
from sprites.PlayerCharacter import PlayerCharacter
from utils.hollow import textOutline
from utils.sprite_utils import get_conform_deltas


class World:
    def __init__(self, width, y_offset, level):
        self.width = width
        self.break_score = 0

        self.finish = False

        # self.level.update_objects(self.x_offset)

        self.player_one = PlayerCharacter(init_x=self.width / 2 - 40,
                                          init_y=y_offset)  # TODO:  This math is bad
        self.player_two = PlayerCharacter(init_x=self.width / 2 + 40,
                                          init_y=y_offset)
        self.player_group = pygame.sprite.Group(self.player_one, self.player_two)

        self.level = level

        self.timer_enabled = 0
        self.timer = 0

    def get_progress(self):
        p1_progress = math.fabs(max((self.player_one.y + vars.PLAYER_START_Y), 0) / (self.level.height))
        p2_progress = math.fabs(max((self.player_two.y + vars.PLAYER_START_Y), 0) / (self.level.height))
        return p1_progress, p2_progress

    def update(self, p1_vel, p2_vel):
        if self.player_one.jump_state == 0:
            self.player_one.x_speed = (self.player_one.x_speed - p1_vel[0]) / self.level.theme.friction
            self.player_one.y_speed = (self.player_one.y_speed - p1_vel[1]) / self.level.theme.friction
            # TODO:  this should be part of the player, not the world
            self.player_one.distance_travelled += math.sqrt(p1_vel[0] * p1_vel[0] + p1_vel[1] * p1_vel[1])

        if self.player_two.jump_state == 0:
            self.player_two.x_speed = (self.player_two.x_speed - p2_vel[0]) / self.level.theme.friction
            self.player_two.y_speed = (self.player_two.y_speed - p2_vel[1]) / self.level.theme.friction
            # TODO:  this should be part of the player, not the world
            self.player_two.distance_travelled += math.sqrt(p2_vel[0] * p2_vel[0] + p2_vel[1] * p2_vel[1])
        self.player_one.update()
        self.player_two.update()

        # check object collisions
        col = pygame.sprite.groupcollide(self.player_group, self.level.objects, dokilla=False, dokillb=False)
        for p_sprite, obj_sprites in col.items():
            for obj in obj_sprites:
                if obj.breakable and obj.get_wrecked():
                    p_sprite.break_score += obj.points

        # TODO:  Combine this with passable non-breakable object colissions
        collide_objects = [x.get_collide_walls() for x in self.level.walls] + [x for x in self.level.objects if
                                                                               x.height > 1]
        walls = pygame.sprite.groupcollide(self.player_group, pygame.sprite.Group(collide_objects), dokilla=False,
                                           dokillb=False)

        for p_sprite, wall_sprites in walls.items():
            _min_z = None
            for wall in wall_sprites:
                if wall.height <= p_sprite.z:
                    if _min_z is None:
                        _min_z = wall.height
                    _min_z = min(_min_z, wall.height)
                else:
                    delta_x, delta_y = get_conform_deltas(wall.rect, p_sprite.old_rect, p_sprite.rect)

                    p_sprite.x -= delta_x
                    p_sprite.y -= delta_y

                    p_sprite.distance_travelled -= math.sqrt(delta_x * delta_x + delta_y * delta_y)

            if _min_z is not None:
                p_sprite.min_z = _min_z
            else:
                p_sprite.min_z = 1

        for obj in self.level.objects:
            obj.update(0, 0)

        for player in self.player_group:
            player.update_z()

        return False

    def draw_win_text(self, screen):
        return
        # todo:  fix this somehow
        font = pygame.font.SysFont('Impact', 70)
        text = textOutline(font, 'FINISH !', self.player_character.character.color,
                           colors.black)
        text.get_width()
        screen.blit(text, (self.x_offset + self.width / 2 - text.get_width() / 2, vars.SCREEN_HEIGHT / 2 - 10))

    def draw(self, screen):
        self.draw_a_player(screen, self.player_one, self.player_two, 0)
        self.draw_a_player(screen, self.player_two, self.player_one, vars.SCREEN_WIDTH / 2)

    def draw_a_player(self, screen, player, other_player, x_offset):
        if player.y > vars.SCREEN_HEIGHT - vars.PLAYER_START_Y:
            y_offset = (0 - player.y) + (vars.SCREEN_HEIGHT - vars.PLAYER_START_Y)
            player_y_offset = 0
        else:
            y_offset = 0
            player_y_offset = player.y - (vars.SCREEN_HEIGHT - vars.PLAYER_START_Y)
        self.level.draw(screen, x_offset, y_offset)

        for sprite in [x for x in self.level.walls]:
            sprite.draw_part_one(screen, x_offset, y_offset)
        for sprite in [x for x in self.level.objects]:
            sprite.draw(screen, x_offset, y_offset)

        for poop in player.poops:
            poop.draw(screen, x_offset, y_offset)

        for poop in other_player.poops:
            poop.draw(screen, x_offset, y_offset)

        # todo:  this will only draw one player, need to do something to draw both
        player.draw_as_player(screen, x_offset, player_y_offset)
        other_player.draw_normal(screen, x_offset, y_offset)

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
        return  # TODO:  fix this
        font2 = pygame.font.SysFont('Impact', size)
        label = textOutline(font2, text, self.player_character.character.color, colors.black)
        screen.blit(label, (
        self.x_offset + self.width / 2 - label.get_width() / 2, vars.SCREEN_HEIGHT / 2 - label.get_height() / 2))

    def get_scores(self):
        return None # TODO: fix this
        return {'time': max(2000 - self.final_timer, 0),
                'break': self.break_score,
                # todo:  maybe return a list of objects instead and then you can do something neat there?
                'poop': self.player_character.poop_score,
                'color': self.player_character.character.color}
