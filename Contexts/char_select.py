import random

import pygame

from Objects.Characters import get_all_characters, TestCharacter
from vars import fps
from colors import *

TOTAL_WAIT = 3

all_chars = get_all_characters()


class CharacterWheel:
    color = (150, 150, 150)
    inc = (0,0,0)
    final_color = (150, 150, 150)
    counter = 0

    def __init__(self, x, y, init_color, blend_frames):
        self.x = x
        self.y = y
        self.color = init_color
        self.final_color = init_color
        self.blend_frames = blend_frames

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

    def draw(self, screen):
        self.update_color()
        try:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 400, 0)
            pygame.draw.circle(screen, self.color, (self.x, self.y), 330, 0)
        except Exception as e:
            print(e)


class CharacterSelectContext:
    left_wheel = CharacterWheel(-100, 200, (250, 100, 50), 40)
    right_wheel = CharacterWheel(1300, 200, (50, 200, 100), 40)

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def main_loop(self):
        while True:
            self.timer += 1
            if self.timer > TOTAL_WAIT * fps:
                self.timer = 0
                color = rand_colors[random.randint(0, len(rand_colors)-1)]
                self.left_wheel.set_color(color[0], color[1], color[2])
                color = rand_colors[random.randint(0, len(rand_colors) - 1)]
                self.right_wheel.set_color(color[0], color[1], color[2])
            self.draw_background()
            self.left_wheel.draw(self.screen)
            self.right_wheel.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(fps)
            pygame.event.get()

    def draw_background(self):
        self.screen.fill(background_fill)
        font = pygame.font.SysFont('Comic Sans MS', 15)
        label = font.render('CHOOSE YOUR CHARACTERS! {0:.2f}'.format(self.timer / fps), 1, (100, 200, 100))
        self.screen.blit(label, (450, 100))



