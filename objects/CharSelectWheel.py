import math

import pygame

from objects.Characters import get_all_characters
all_chars = get_all_characters()
from sprites.CharacterSelectCharacter_old import CharacterSelectCharacter
from vars import radians_factor


class CharacterWheel:
    color = (150, 150, 150)
    inc = (0,0,0)
    final_color = (150, 150, 150)
    counter = 0

    def __init__(self, x, y, blend_frames, angle_offset, left_or_right=1):
        self.spawn_counter = 0
        self.confirmed = False
        self.x = x
        self.y = y
        self.characters = []
        self.angle_counter = 0
        self.final_angle = 0
        self.moving = 0
        self.spawning = False
        self.spawned = False
        self.blend_frames = blend_frames
        self.factor = left_or_right
        self.angle_offset = angle_offset
        self.selected_character_index = 0
        self.radius = 0
        self.color = (0, 0, 0)
        self.load_characters()
        self.final_color = self.get_selected_character().color

    def load_characters(self):
        char_indices = range(len(all_chars))
        if self.factor < 0:
            char_indices = char_indices.__reversed__()

        for i in char_indices:
            self.characters.append(
                CharacterSelectCharacter(all_chars[i](), int(360 / len(all_chars) * i + self.angle_offset), self.x, self.y))

        self.update_chars(0)  # Todo:  this is kind of hacky

    def confirm_character(self):
        self.confirmed = True

    def update_chars(self, angle_inc):
        for char in self.characters:
            char.radius = self.radius + 30
            char.angle = (char.angle + angle_inc) % 360
            char.update()

    def set_color(self, r, g, b):
        self.counter = 0
        self.final_color = (r, g, b)
        self.inc = ((r - self.color[0]) / self.blend_frames, (g - self.color[1]) / self.blend_frames, (b - self.color[2]) / self.blend_frames)

    def update_color(self):
        self.counter += 1
        if self.counter > self.blend_frames:
            self.color = self.final_color
            return
        new_r = max(min(int(self.color[0] + self.inc[0]), 255), 0)
        new_g = max(min(int(self.color[1] + self.inc[1]), 255), 0)
        new_b = max(min(int(self.color[2] + self.inc[2]), 255), 0)

        self.color = (new_r, new_g, new_b)

    def update_angle(self, direction):
        if not self.confirmed and self.spawned:
            if self.moving != direction:
                self.selected_character_index = (self.selected_character_index - (direction*self.factor)) % len(self.characters)
                new_color = self.get_selected_character().color
                self.set_color(new_color[0], new_color[1], new_color[2])
                # Todo:  set self.final_angle here
            self.moving = direction

    def get_selected_character(self):
        return self.characters[self.selected_character_index].character

    def update(self):
        self.update_color()

        self.angle_counter += self.moving

        if math.fabs(self.angle_counter) > self.blend_frames or self.moving and self.angle_counter == 0:
            self.moving = 0
            self.angle_counter = 0
            # TODO:  Fix issue 4 here

        self.update_chars(360 / len(self.characters) / self.blend_frames * self.moving)
        for char in self.characters:
            char.selected = False

    def spawn_or_confirm(self):
        if self.spawned:
            if not self.moving:
                self.confirm_character()
        else:
            self.spawning = True
            color = self.get_selected_character().color
            self.set_color(color[0], color[1], color[2])

    def display_stats(self, screen):
        if not self.moving:
            self.characters[self.selected_character_index].selected = True
            name = self.get_selected_character().name
            stats = self.get_selected_character().attributes
            font = pygame.font.SysFont('Comic Sans MS', 25)
            label = font.render(name, 1, self.get_selected_character().color)
            screen.blit(label, (self.x + (200*self.factor), 600))
            stat_y = 620
            for stat in stats:
                label = font.render(stat, 1, self.get_selected_character().color)
                screen.blit(label, (self.x + (250 * self.factor) - 100, stat_y))
                stat_y += 20

            label = font.render('PRESS BUTTON TO CONFIRM', 1, (200, 200, 200))
            screen.blit(label, (self.x + (300 * self.factor) - 175, stat_y+20))
            stat_y += 20

    def draw_circles(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 90), 9)
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 20), 4)
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 5), 1)
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 1), 1)

    def draw(self, screen):
        if not self.spawning and self.radius == 0:
            font = pygame.font.SysFont('Comic Sans MS', 15)
            label = font.render('PRESS KEY TO JOIN', 1, (200, 200, 200))
            screen.blit(label, (self.x + (200 * self.factor)-75, 200))
        if self.spawning:
            self.spawn_counter += 1
            self.radius += 300 / self.blend_frames
            if self.spawn_counter > self.blend_frames:
                self.spawning = False
                self.spawned = True

        self.update()

        self.draw_circles(screen)

        if self.radius > 0 and not self.confirmed:
            self.display_stats(screen)

        if self.confirmed:
            # TODO:  ugly
            font = pygame.font.SysFont('Comic Sans MS', 40)
            label = font.render(self.get_selected_character().name, 1, self.get_selected_character().color)
            screen.blit(label, (self.x + (200 * self.factor) - 75, 650))

        for char in self.characters:
            char.draw(screen)

