import random

import pygame
import math
from Objects.Characters import get_all_characters, TestCharacter
from vars import fps
from colors import *

TOTAL_WAIT = 1
transition_frames = 40
all_chars = get_all_characters()

radians_factor = 0.0174533  # TODO:  move this out to vars, it's used everywhere


class CharacterWheel:
    color = (150, 150, 150)
    inc = (0,0,0)
    final_color = (150, 150, 150)
    counter = 0

    def __init__(self, x, y, init_color, blend_frames, angle_offset, left_or_right=1):
        self.x = x
        self.y = y
        self.characters = []
        self.color = init_color
        self.final_color = init_color
        self.final_angle = 0
        self.angle_counter = 0
        self.moving = 0
        self.blend_frames = blend_frames
        self.factor = left_or_right
        self.angle_offset = angle_offset
        self.selected_character_index = 0
        self.load_characters()

    def load_characters(self):
        for i in range(len(all_chars)):
            self.characters.append(CharacterSelectCharacter(all_chars[i]()))
            self.characters[i].angle = int(360 / len(all_chars) * i * self.factor)
        self.update_chars(0) # Todo:  this is kind of hacky

    def update_chars(self, angle_inc):
        for char in self.characters:
            char.angle = (char.angle + angle_inc) % 360
            char.update()

            char.x = math.cos(char.angle * radians_factor) * 365 + self.x - (char.current_sprite.get_width() / 2)
            char.y = math.sin(char.angle * radians_factor) * 365 + self.y - (char.current_sprite.get_height() / 2)

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
                self.selected_character_index = (self.selected_character_index + direction) % len(self.characters)
            new_color = self.characters[self.selected_character_index].character.color
            self.set_color(new_color[0], new_color[1], new_color[2])  # todo:  hacky
            self.moving = direction

    def update(self):
        self.update_color()

        self.angle_counter += self.moving

        if math.fabs(self.angle_counter) > self.blend_frames or self.moving and self.angle_counter == 0:
            self.moving = 0
            self.angle_counter = 0

        if self.moving:
            self.update_chars(360 / len(self.characters) / self.blend_frames * self.moving)


    def draw(self, screen):
        self.update()
        try:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 400, 8)
            pygame.draw.circle(screen, self.color, (self.x, self.y), 330, 4)
            for char in self.characters:
                char.draw(screen)
        except Exception as e:
            print(e)


class CharacterSelectCharacter:
    def __init__(self, character):
        self.character = character
        self.character.load_portrait()
        self.orig_sprite = self.character.portrait
        self.current_sprite = self.orig_sprite
        self.angle = 0
        self.scale = 0.25
        self.x = 0
        self.y = 0

    def update(self):
        if self.angle < 30 or self.angle > 330 or (self.angle > 150 and self.angle < 210):
            self.scale = max(math.fabs(math.cos(self.angle * 3 % 180 * radians_factor)), 0.25)
        self.current_sprite = pygame.transform.scale(self.orig_sprite, (int(self.scale * self.orig_sprite.get_width()), int(self.scale * self.orig_sprite.get_height())))

    def draw(self, screen):
        screen.blit(self.current_sprite, (self.x, self.y))


class CharacterSelectContext:
    def __init__(self, screen):
        self.left_wheel = CharacterWheel(-100, 200, (250, 100, 50), transition_frames, 0)
        self.right_wheel = CharacterWheel(1300, 200, (50, 200, 100), transition_frames, -60)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def check_keys(self):
        pass

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    color = rand_colors[random.randint(0, len(rand_colors) - 1)]
                    if event.key == pygame.K_w:
                        self.left_wheel.update_angle(-1)
                        #self.left_wheel.set_color(color[0], color[1], color[2])
                    if event.key == pygame.K_s:
                        self.left_wheel.update_angle(1)
                        #self.left_wheel.set_color(color[0], color[1], color[2])
                    if event.key == pygame.K_UP:
                        self.right_wheel.update_angle(1)
                        #self.right_wheel.set_color(color[0], color[1], color[2])
                    if event.key == pygame.K_DOWN:
                        self.right_wheel.update_angle(-1)
                        #self.right_wheel.set_color(color[0], color[1], color[2])
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            self.timer += 1
            self.check_keys()
            if self.timer > TOTAL_WAIT * fps:
                self.timer = 0
            self.draw_background()
            self.left_wheel.draw(self.screen)
            self.right_wheel.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(fps)

    def draw_characters(self):
        pass

    def draw_background(self):
        self.screen.fill(background_fill)
        font = pygame.font.SysFont('Comic Sans MS', 15)
        label = font.render('CHOOSE YOUR CHARACTERS! {0:.2f}'.format(self.timer / fps), 1, (100, 200, 100))
        self.screen.blit(label, (450, 100))



