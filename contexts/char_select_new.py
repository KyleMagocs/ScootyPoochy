import pygame

import colors
from colors import *
from objects.CharSelectWheel import CharacterWheel
from objects.CharSelectWheel_New import CharacterWheelNew
from objects.miscsprites import PawButton
from vars import fps

from objects.Characters import get_all_characters
import vars
all_chars = get_all_characters()

TOTAL_WAIT = 1
transition_frames = int(vars.fps* .75)


class CharacterSelectTrackballContext:

    def __init__(self, screen, p1, p2):
        self.left_wheel = CharacterWheelNew(-100, 200, transition_frames, 0, vars.SCREEN_WIDTH/4, 20, 35, False)
        self.right_wheel = CharacterWheelNew(vars.SCREEN_WIDTH+100, 200, transition_frames, -1 * (360 / len(all_chars) * (len(all_chars) / 2 - 1)), vars.SCREEN_WIDTH/4*3, 145, 160, True)
        self.players = (p1, p2)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def both_wheels_confirmed(self):
        return self.left_wheel.confirmed and self.right_wheel.confirmed

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    if self.left_wheel.confirmed and not self.right_wheel.spawned and not self.right_wheel.spawning:
                        self.right_wheel.confirmed = True
                    self.left_wheel.spawn_or_confirm()

                if event.key == pygame.K_j:
                    if self.right_wheel.confirmed and not self.left_wheel.spawned and not self.left_wheel.spawning:
                        self.left_wheel.confirmed = True
                    self.right_wheel.spawn_or_confirm()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    def get_trackball_input(self):
        p1_left, p1_right = self.players[0].read_input()
        p2_left, p2_right = self.players[1].read_input()
        left = int((p1_left[1] + p1_right[1])/10)
        right = int((p2_left[1] + p2_right[1])/10)

        return(left, right)

    def main_loop(self):
        start_timer = 0
        end_timer = 0
        left_ang, right_ang = 0,0
        while True:

            actual_fps = 1000 / self.clock.tick(fps)

            # if self.timer % 5 == 0:
            #     vars.selected_character_color_index = (vars.selected_character_color_index + 1) % 3

            self.timer += 1
            self.check_events()
            if self.timer % 3 == 0:
                left_ang, right_ang = self.get_trackball_input()
            self.left_wheel.update(left_ang/3)
            self.right_wheel.update(right_ang/3*-1)
            self.draw()

            # TODO:  Maybe refactor ?  Move to draw method ?  Whatever
            if start_timer < int(vars.fps / 2):
                fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                fade_overlay.fill(colors.black)
                fade_overlay.set_alpha(((int(vars.fps / 2) - start_timer) / int(vars.fps / 2)) * 255)
                self.screen.blit(fade_overlay, (0, 0))
                start_timer += 1

            if self.both_wheels_confirmed():
                if end_timer > int(vars.fps*3):
                    left = self.left_wheel.get_selected_character().character if self.left_wheel.get_selected_character() is not None else None
                    right = self.right_wheel.get_selected_character().character if self.right_wheel.get_selected_character() is not None else None
                    return [left, right]
                elif end_timer > int(vars.fps*2):
                        fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                        fade_overlay.fill(colors.black)
                        fade_overlay.set_alpha(((end_timer-vars.fps*2) / int(vars.fps)) * 255)
                        self.screen.blit(fade_overlay, (0, 0))
                end_timer += 1

            pygame.display.flip()

    def draw(self):
        self.draw_background()
        self.left_wheel.draw(self.screen)
        self.right_wheel.draw(self.screen)
        if self.left_wheel.confirmed and not self.right_wheel.spawned and not self.right_wheel.spawning and not self.both_wheels_confirmed():
            font = pygame.font.SysFont('Impact', 25)
            label = font.render('PRESS                     FOR ONE PLAYER', 1, (200, 200, 200))
            self.screen.blit(label, (self.left_wheel.align_x - label.get_width() / 2, vars.SCREEN_HEIGHT - 100))
            button = PawButton((self.left_wheel.align_x - label.get_width() / 2 + 70, vars.SCREEN_HEIGHT - 120))
            button.draw(self.screen, 0, 0)
        if self.right_wheel.confirmed and not self.left_wheel.spawned and not self.left_wheel.spawning and not self.both_wheels_confirmed():
            font = pygame.font.SysFont('Impact', 25)
            label = font.render('PRESS                     FOR ONE PLAYER', 1, (200, 200, 200))
            self.screen.blit(label, (self.right_wheel.align_x - label.get_width() / 2, vars.SCREEN_HEIGHT - 100))
            button = PawButton((self.right_wheel.align_x - label.get_width() / 2 + 70, vars.SCREEN_HEIGHT - 120))
            button.draw(self.screen, 0, 0)

    def draw_background(self):
        self.screen.fill(background_fill)
        font = pygame.font.SysFont('Impact', 50)
        if not self.both_wheels_confirmed():
            label = font.render('CHOOSE YOUR CHARACTERS!'.format(self.timer / fps), 1, (100, 200, 100))
            self.screen.blit(label, (vars.SCREEN_WIDTH/2 - label.get_width()/2, 100))



