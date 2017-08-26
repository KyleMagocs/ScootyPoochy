import pygame

import colors
from colors import *
from objects.CharSelectWheel import CharacterWheel
from vars import fps

from objects.Characters import get_all_characters
import vars
all_chars = get_all_characters()

TOTAL_WAIT = 1
transition_frames = 25


class CharacterSelectContext:

    def __init__(self, screen, p1, p2):
        self.left_wheel = CharacterWheel(-100, 200, transition_frames, 0, 1)
        self.right_wheel = CharacterWheel(vars.SCREEN_WIDTH+100, 200, transition_frames, -1 * (360 / len(all_chars) * (len(all_chars) / 2 - 1)), -1)
        self.players = (p1, p2)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def both_wheels_confirmed(self):
        return self.left_wheel.confirmed and self.right_wheel.confirmed

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.left_wheel.update_angle(-1)
                if event.key == pygame.K_s:
                    self.left_wheel.update_angle(1)
                if event.key == pygame.K_SPACE:
                    self.left_wheel.spawn_or_confirm()
                if event.key == pygame.K_UP:
                    self.right_wheel.update_angle(1)
                if event.key == pygame.K_DOWN:
                    self.right_wheel.update_angle(-1)
                if event.key == pygame.K_RETURN:
                    self.right_wheel.spawn_or_confirm()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    def main_loop(self):
        start_timer = 0
        end_timer = 0
        while True:

            if self.timer % 5 == 0:
                vars.selected_character_color_index = (vars.selected_character_color_index + 1) % 3

            self.timer += 1
            self.draw()

            if start_timer < int(vars.fps / 2):
                fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                fade_overlay.fill(colors.black)
                fade_overlay.set_alpha(((int(vars.fps / 2) - start_timer) / int(vars.fps / 2)) * 255)
                self.screen.blit(fade_overlay, (0, 0))
                start_timer += 1

            self.check_events()


            self.clock.tick(fps)
            if self.both_wheels_confirmed():
                if end_timer > int(vars.fps / 2):
                    return [self.left_wheel.get_selected_character(), self.right_wheel.get_selected_character(),]
                else:
                    fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                    fade_overlay.fill(colors.black)
                    fade_overlay.set_alpha((end_timer / int(vars.fps / 2)) * 255)
                    self.screen.blit(fade_overlay, (0, 0))
                    end_timer += 1

            pygame.display.flip()



    def draw(self):
        self.draw_background()
        self.left_wheel.draw(self.screen)
        self.right_wheel.draw(self.screen)

    def draw_background(self):
        self.screen.fill(background_fill)
        font = pygame.font.SysFont('Impact', 20)
        label = font.render('CHOOSE YOUR CHARACTERS!'.format(self.timer / fps), 1, (100, 200, 100))
        self.screen.blit(label, (450, 100))



