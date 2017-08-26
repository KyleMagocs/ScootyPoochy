import copy
import math

import pygame

import colors
import vars
from sprites.PlayerCharacter import PlayerCharacter
from utils.hollow import textOutline
from utils.sprite_utils import get_conform_deltas, get_velocity


class World:
    def __init__(self, width, y_offset, level):
        self.countdown = ['3', '2', '1', 'GO!']

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

        self.countdown_timer = 0
        self.timer_enabled = 0
        self.timer = 0

    def get_progress(self):
        p1_progress = math.fabs(max((self.player_one.y + vars.PLAYER_START_Y), 0) / (self.level.height))
        p2_progress = math.fabs(max((self.player_two.y + vars.PLAYER_START_Y), 0) / (self.level.height))
        return p1_progress, p2_progress

    def update(self, p1_left, p1_right, p2_left, p2_right):
        if not vars.skip_countdown and len(self.countdown) > 0:
            self.player_one.update_limbs((0,0), (0,0))
            self.player_two.update_limbs((0,0), (0,0))
            if self.countdown_timer < int(vars.fps*.75) and len(self.countdown) > 0:
                self.countdown_timer += 1
            else:
                if len(self.countdown) > 0:
                    self.countdown.remove(self.countdown[0])

                self.countdown_timer = 0
        if len(self.countdown) > 1:
            return

        self.player_one.update_limbs(p1_left, p1_right)
        self.player_two.update_limbs(p2_left, p2_right)

        self.handle_player_vel(p1_left, p1_right, p2_left, p2_right)

        self.player_one.update()
        self.player_two.update()

        self.handle_player_collisions()

        self.handle_breakable_collisions()

        self.handle_wall_collisions()

        for obj in self.level.objects:
            obj.update(0, 0)
        for obj in self.level.broken_objects:
            obj.update(0, 0)

        for player in self.player_group:
            player.update_z()

        return self.game_finished()

    def game_finished(self):
        if self.player_one.y < 50 and self.player_two.y < 50:
            return self.get_scores()
        else:
            return None

    def handle_player_vel(self, p1_left, p1_right, p2_left, p2_right):
        p1_vel = get_velocity(p1_left, p1_right)
        p2_vel = get_velocity(p2_left, p2_right)
        if self.player_one.jump_state == 0 and self.player_one.bounce_count == 0:
            self.player_one.x_speed = (self.player_one.x_speed - p1_vel[0]) / self.level.theme.friction
            self.player_one.y_speed = (self.player_one.y_speed - p1_vel[1]) / self.level.theme.friction
            # TODO:  this should be part of the player, not the world
            self.player_one.distance_travelled += math.sqrt(p1_vel[0] * p1_vel[0] + p1_vel[1] * p1_vel[1])
        if self.player_two.jump_state == 0 and self.player_two.bounce_count == 0:
            self.player_two.x_speed = (self.player_two.x_speed - p2_vel[0]) / self.level.theme.friction
            self.player_two.y_speed = (self.player_two.y_speed - p2_vel[1]) / self.level.theme.friction
            # TODO:  this should be part of the player, not the world
            self.player_two.distance_travelled += math.sqrt(p2_vel[0] ** 2 + p2_vel[1] ** 2)

    def handle_player_collisions(self):
        for player in self.player_group:
            for player2 in self.player_group:
                if player != player2:
                    if math.sqrt(((player.x - player2.x) ** 2) + ((player.y - player2.y) ** 2)) <= (player.radius + player2.radius):
                        self.bounce_player(player, player2)

    def bounce_player(self, bouncee, bouncer):
        C1Speed = math.sqrt((bouncee.x_speed ** 2) + (bouncee.y_speed ** 2))
        XDiff = -(bouncee.x - bouncer.x)
        YDiff = -(bouncee.y - bouncer.y)
        if XDiff > 0:
            if YDiff > 0:
                Angle = math.degrees(math.atan(YDiff / XDiff))
                XSpeed = -C1Speed * math.cos(math.radians(Angle))
                YSpeed = -C1Speed * math.sin(math.radians(Angle))
            elif YDiff <= 0:
                Angle = math.degrees(math.atan(YDiff / XDiff))
                XSpeed = -C1Speed * math.cos(math.radians(Angle))
                YSpeed = -C1Speed * math.sin(math.radians(Angle))
        elif XDiff < 0:
            if YDiff > 0:
                Angle = 180 + math.degrees(math.atan(YDiff / XDiff))
                XSpeed = -C1Speed * math.cos(math.radians(Angle))
                YSpeed = -C1Speed * math.sin(math.radians(Angle))
            elif YDiff <= 0:
                Angle = -180 + math.degrees(math.atan(YDiff / XDiff))
                XSpeed = -C1Speed * math.cos(math.radians(Angle))
                YSpeed = -C1Speed * math.sin(math.radians(Angle))
        elif XDiff == 0:
            if YDiff > 0:
                Angle = -90
            else:
                Angle = 90
            XSpeed = C1Speed * math.cos(math.radians(Angle))
            YSpeed = C1Speed * math.sin(math.radians(Angle))
        elif YDiff == 0:
            if XDiff < 0:
                Angle = 0
            else:
                Angle = 180
            XSpeed = C1Speed * math.cos(math.radians(Angle))
            YSpeed = C1Speed * math.sin(math.radians(Angle))
        bouncee.x_speed = XSpeed*0.8
        bouncee.y_speed = YSpeed*0.8
        bouncee.bounce_count = 5

    def handle_breakable_collisions(self):
        # check object collisions
        col = pygame.sprite.groupcollide(self.player_group, self.level.objects, dokilla=False, dokillb=False)
        for p_sprite, obj_sprites in col.items():
            for obj in obj_sprites:
                if p_sprite.z >= obj.z and obj.breakable and obj.get_wrecked():
                    p_sprite.break_score += obj.points
                    p_sprite.broken_objects.add(obj)
                    self.level.objects.remove(obj)
                    self.level.broken_objects.add(obj)

    def handle_wall_collisions(self):
        collide_objects = [x.get_collide_walls() for x in self.level.walls] + [x for x in self.level.objects if
                                                                               x.height > 0]
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

                    # p_sprite.distance_travelled -= math.sqrt(delta_x * delta_x + delta_y * delta_y)

            if _min_z is not None:
                p_sprite.min_z = _min_z
            else:
                p_sprite.min_z = 0

    def draw(self, screen):
        self.draw_a_player(screen, self.player_one, self.player_two, 0)
        self.draw_a_player(screen, self.player_two, self.player_one, vars.SCREEN_WIDTH - self.width)

    def draw_a_player(self, screen, player, other_player, x_offset):
        if player.y > vars.SCREEN_HEIGHT - vars.PLAYER_START_Y:
            y_offset = (0 - player.y) + (vars.SCREEN_HEIGHT - vars.PLAYER_START_Y)
            player_y_offset = 0
        else:
            y_offset = 0
            player_y_offset = player.y - (vars.SCREEN_HEIGHT - vars.PLAYER_START_Y)
        self.level.draw(screen, x_offset, y_offset)

        for sprite in self.level.walls:
            sprite.draw_part_one(screen, x_offset, y_offset)
        for sprite in self.level.objects:
            sprite.draw(screen, x_offset, y_offset)
        for sprite in self.level.broken_objects:
            sprite.draw(screen, x_offset, y_offset)
        for poop in player.poops:
            poop.draw(screen, x_offset, y_offset)

        for poop in other_player.poops:
            poop.draw(screen, x_offset, y_offset)

        for sprite in [x for x in self.level.walls if x.y + 32 < player.y]:
            sprite.draw_part_two(screen, x_offset, y_offset)

        player.draw_as_player(screen, x_offset, player_y_offset)

        for sprite in [x for x in self.level.walls if x.y+32>=player.y]:
            sprite.draw_part_two(screen, x_offset, y_offset)

        for sprite in [x for x in self.level.walls if x.y + 32 < other_player.y]:
            sprite.draw_part_two(screen, x_offset, y_offset)

        other_player.draw_normal(screen, x_offset, y_offset)

        for sprite in [x for x in self.level.walls if x.y+32>=other_player.y]:
            sprite.draw_part_two(screen, x_offset, y_offset)




        for sprite in self.level.broken_objects:
            sprite.draw_score(screen, x_offset, y_offset, draw_points=(sprite in player.broken_objects))

        if player.y < 50:
            self.draw_win_text(screen, x_offset, player.character.color)

        if len(self.countdown) > 0:
            self.draw_countdown(screen, x_offset, player.character.color, self.countdown[0], self.countdown_timer * 3)
            font = pygame.font.SysFont('Impact', 18)
            label = font.render('YOU!', 1, player.character.color)
            screen.blit(label, (x_offset + player.x + label.get_width()/2, (vars.SCREEN_HEIGHT - vars.PLAYER_START_Y + 75)))

            # TODO:  Should put a real debug in here
            # # IF YOU'RE LOOKING FOR A GOOD PLACE TO LOG SOME CRAP TO THE SCREEN, THIS WOULD BE A PRETTY GOOD SPOT # #
            # font = pygame.font.SysFont('Impact', 14)
            # label = font.render('Player z: ' + str(self.player_one.z), 1, (0, 255, 255))
            # screen.blit(label, (x_offset + self.width / 4 + 2, vars.SCREEN_HEIGHT / 2 - 10 + 2))
            ############################################################################################################

    def start_timer(self):
        self.timer_enabled = 1

    def draw_countdown(self, screen, x_offset, color, text, size):
        font2 = pygame.font.SysFont('Impact', size)
        label = textOutline(font2, text, color, colors.black)
        screen.blit(label, (
            x_offset + self.width / 2 - label.get_width() / 2, vars.SCREEN_HEIGHT / 2 - label.get_height() / 2))

    def draw_win_text(self, screen, x_offset, color):
        font = pygame.font.SysFont('Impact', 70)
        text = textOutline(font, 'FINISH !', color,
                           colors.black)
        text.get_width()
        screen.blit(text, (x_offset + self.width / 2 - text.get_width() / 2, vars.SCREEN_HEIGHT / 2 - 10))

    def get_scores(self):
        return ({'time': max(2000 - self.player_one.final_timer, 0),
                 'break': self.player_one.break_score,
                 # todo:  maybe return a list of objects instead and then you can do something neat there?
                 'poop': self.player_one.poop_score,
                 'char': self.player_one.character, },
                {'time': max(2000 - self.player_two.final_timer, 0),
                 'break': self.player_two.break_score,
                 # todo:  maybe return a list of objects instead and then you can do something neat there?
                 'poop': self.player_two.poop_score,
                 'char': self.player_two.character},)
