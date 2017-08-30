import copy
import math

import pygame

import colors
from objects.Characters import get_all_characters

all_chars = get_all_characters()
from sprites.CharacterSelectCharacter import CharacterSelectCharacter
from vars import radians_factor


class CharacterWheelNew:
    color = (150, 150, 150)
    inc = (0, 0, 0)
    final_color = (150, 150, 150)
    counter = 0

    def __init__(self, x, y, blend_frames, angle_offset, left_or_right=1, min_selected_angle=0, max_selected_angle=0):
        self.spawn_counter = 0
        self.confirmed = False
        self.x = x
        self.y = y
        self.characters = []
        self.angle_counter = 0
        self.final_angle = 0
        self.angle = 0
        self.moving = 0
        self.spawning = False
        self.spawned = False
        self.despawning = False
        self.despawned = False
        self.despawn_counter = 0
        self.blend_frames = blend_frames
        self.factor = left_or_right
        self.flash_timer = 0
        self.angle_offset = angle_offset
        self.selected_character_index = 0
        self.radius = 0
        self.color = (0, 0, 0)
        self.all_colors = list()
        self.min_selected_angle = min_selected_angle
        self.max_selected_angle = max_selected_angle
        self.load_characters()

    def load_characters(self):
        char_indices = range(len(all_chars))
        # if self.factor < 0:
        #     char_indices = char_indices.__reversed__()

        angle_divis = int(360 / len(all_chars))

        for i in char_indices:
            self.characters.append(
                CharacterSelectCharacter(all_chars[i](), int(angle_divis * i), self.x, self.y, self.min_selected_angle, self.max_selected_angle))

        temp_stupid_array = self.characters
        temp_stupid_array[-1].angle += (360 if temp_stupid_array[-1].angle <= 0 else 0)
        for i in range(-1, len(temp_stupid_array) - 1):
            start_color = temp_stupid_array[i].character.color
            end_color = temp_stupid_array[i + 1].character.color
            r_diff = end_color[0] - start_color[0]
            g_diff = end_color[1] - start_color[1]
            b_diff = end_color[2] - start_color[2]

            start_angle = temp_stupid_array[i].angle
            end_angle = temp_stupid_array[i + 1].angle
            if start_angle > end_angle:
                end_angle += 360
            for j in range(start_angle, end_angle):
                # if j - start_angle < 10:
                #     self.all_colors.append(start_color)
                #     continue
                # if end_angle - j - 10 < 10:
                #     self.all_colors.append(end_color)
                #     continue
                ratio = (j - temp_stupid_array[i].angle + 10) / max((angle_divis - 10), 0)

                if r_diff >= 0:
                    new_r = int(r_diff * ratio + end_color[0])
                else:
                    new_r = int(r_diff * ratio + start_color[0])
                if g_diff >= 0:
                    new_g = int(g_diff * ratio + end_color[1])
                else:
                    new_g = int(g_diff * ratio + start_color[1])
                if b_diff >= 0:
                    new_b = int(b_diff * ratio + end_color[2])
                else:
                    new_b = int(b_diff * ratio + start_color[2])

                new_color = (new_r, new_g, new_b)

                # todo: from buzzed kyle:  you probably just introduced a bug by doing this
                # self.all_colors.append(new_color)
                self.all_colors.append((255, 255, 255))

        self.update_chars(0)  # Todo:  this is kind of hacky

    def confirm_character(self):
        self.get_selected_character().flash_factor = 2
        self.flash_timer = 15
        self.confirmed = True

    def update_chars(self, angle_inc):
        if self.confirmed:
            angle_inc = 0
        for char in self.characters:
            if (self.despawning or self.despawned) and char.selected:
                continue
            char.radius = self.radius + 30
            char.update(angle_inc)

    def get_selected_character(self):
        if self.spawning:
            return None
        try:
            return [x for x in self.characters if x.selected][0]
        except:
            return None


    def update(self, angle):
        if self.spawning:
            self.spawn_counter += 1
            self.radius += 300 / self.blend_frames
            if self.spawn_counter > self.blend_frames:
                self.spawning = False
                self.spawned = True
        if self.despawning:
            self.despawn_counter += 1
            self.radius -= 300 / self.blend_frames
            if self.despawn_counter > self.blend_frames:
                self.despawning = False
                self.despawned = True

        self.flash_timer = max(self.flash_timer-1, 0)
        if self.flash_timer == 1:
            self.get_selected_character().flash_factor = 1000
        self.angle = (self.angle + angle) % 360
        self.update_chars(self.angle)
        self.color = self.all_colors[(self.angle) % 360]

    def spawn_or_confirm(self):
        if self.spawned:
            if not self.moving:
                self.confirm_character()
                self.despawning = True
        else:
            self.spawning = True

    def draw_stats(self, screen):
        char = self.get_selected_character()
        if char is not None:
            if not self.moving:
                name = char.character.name
                stats = char.character.attributes
                font = pygame.font.SysFont('Comic Sans MS', 25)
                label = font.render(name, 1, char.character.color)
                screen.blit(label, (char.x + char.width + 10, char.y))
                stat_y = char.y + 20
                for stat in stats:
                    label = font.render(stat, 1, colors.white)
                    screen.blit(label, (char.x + char.width + 10, stat_y))
                    stat_y += 20

                label = font.render('PRESS BUTTON TO CONFIRM', 1, (200, 200, 200))
                screen.blit(label, (self.x + (300 * self.factor) - 175, stat_y + 20))
                stat_y += 20

    def draw_circles(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 90), 9)
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 20), 4)
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 5), 1)
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 1), 1)

    def draw(self, screen):
        if not self.spawned and not self.spawning:
            font = pygame.font.SysFont('Comic Sans MS', 15)
            label = font.render('PRESS KEY TO JOIN', 1, (200, 200, 200))
            screen.blit(label, (self.x + (200 * self.factor) - 75, 200))

        self.draw_circles(screen)

        if self.radius > 0 and not self.confirmed:
            self.draw_stats(screen)

        if self.confirmed:
            # TODO:  ugly
            font = pygame.font.SysFont('Comic Sans MS', 40)
            label = font.render(self.get_selected_character().character.name, 1, self.get_selected_character().character.color)
            screen.blit(label, (self.x + (200 * self.factor) - 75, 650))

        if self.spawning or self.spawned:
            if not self.confirmed:
                for char in sorted(self.characters, key=lambda c: c.scale):
                    char.draw(screen)

            else:
                self.get_selected_character().draw(screen)