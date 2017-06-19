import math

import pygame

from objects.Characters import get_all_characters
all_chars = get_all_characters()
from sprites.CharacterSelectCharacter import CharacterSelectCharacter
from vars import radians_factor


class CharacterWheel:
    color = (150, 150, 150)
    inc = (0,0,0)
    final_color = (150, 150, 150)
    counter = 0

    def __init__(self, x, y, blend_frames, angle_offset, left_or_right=1):
        self.spawn_counter = 0
        self.x = x
        self.y = y
        self.characters = []
        self.angle_counter = 0
        self.final_angle = 0
        self.moving = 0
        self.spawning = False
        self.blend_frames = blend_frames
        self.factor = left_or_right
        self.angle_offset = angle_offset
        self.selected_character_index = 0
        self.load_characters()
        self.radius = 0
        self.color = (0, 0, 0)
        self.final_color = self.characters[self.selected_character_index].character.color

    def load_characters(self):
        char_indices = range(len(all_chars))
        if self.factor < 0:
            char_indices = char_indices.__reversed__()

        for i in char_indices:
            self.characters.append(
                CharacterSelectCharacter(all_chars[i](), int(360 / len(all_chars) * i + self.angle_offset), self.x, self.y))

        self.update_chars(0)  # Todo:  this is kind of hacky

    def update_chars(self, angle_inc):
        for char in self.characters:
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
        # self.angle_counter = 0
        if self.moving != direction:
            self.selected_character_index = (self.selected_character_index - (direction*self.factor)) % len(self.characters)
            new_color = self.characters[self.selected_character_index].character.color
            self.set_color(new_color[0], new_color[1], new_color[2])
            # Todo:  set self.final_angle here
        self.moving = direction

    def update(self):
        self.update_color()

        self.angle_counter += self.moving

        if math.fabs(self.angle_counter) > self.blend_frames or self.moving and self.angle_counter == 0:
            self.moving = 0
            self.angle_counter = 0

            # TODO:  Fix issue 4 here

        if self.moving:
            self.update_chars(360 / len(self.characters) / self.blend_frames * self.moving)

    def display_stats(self, screen):
        if not self.moving:
            name = self.characters[self.selected_character_index].character.name
            stats = self.characters[self.selected_character_index].character.attributes
            font = pygame.font.SysFont('Comic Sans MS', 15)
            label = font.render(name, 1, self.characters[self.selected_character_index].character.color)
            screen.blit(label, (self.x + (200*self.factor), 600))
            stat_y = 620
            for stat in stats:
                label = font.render(stat, 1, self.characters[self.selected_character_index].character.color)
                screen.blit(label, (self.x + (200 * self.factor) - 75, stat_y))
                stat_y += 20

    def draw_circles(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 90), 9)
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 20), 4)
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 5), 1)
        pygame.draw.circle(screen, self.color, (self.x, self.y), int(self.radius + 1), 1)

    def draw(self, screen):
        if self.spawning:
            self.spawn_counter += 1
            self.radius += 300 / self.blend_frames
            self.color = (self.color[0]+9, self.color[1]+9, self.color[2]+9)
            if self.spawn_counter > self.blend_frames:
                self.spawning = False
                self.set_color(self.final_color[0], self.final_color[1], self.final_color[2])

        self.draw_circles(screen)

        if not self.spawning and self.radius > 0:
            self.update()
            for char in self.characters:
                char.draw(screen)
            self.display_stats(screen)
