import pygame

from colors import *
from objects.CharSelectWheel import CharacterWheel
from vars import fps

from objects.Characters import get_all_characters
all_chars = get_all_characters()

TOTAL_WAIT = 1
transition_frames = 25


class CharacterSelectContext:
    def __init__(self, screen):
        self.left_wheel = CharacterWheel(-100, 200, transition_frames, 0, 1)
        self.right_wheel = CharacterWheel(1300, 200, transition_frames, -1 * (360 / len(all_chars) * (len(all_chars) / 2 - 1)), -1)
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.left_wheel.update_angle(-1)
                if event.key == pygame.K_s:
                    self.left_wheel.update_angle(1)
                if event.key == pygame.K_UP:
                    self.right_wheel.update_angle(1)
                if event.key == pygame.K_DOWN:
                    self.right_wheel.update_angle(-1)
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    def main_loop(self):
        while True:
            self.check_events()

            # self.timer += 1
            # if self.timer > TOTAL_WAIT * fps:
            #     self.timer = 0

            self.draw()

            pygame.display.flip()
            self.clock.tick(fps)

    def draw(self):
        self.draw_background()
        self.left_wheel.draw(self.screen)
        self.right_wheel.draw(self.screen)

    def draw_characters(self):
        pass

    def draw_background(self):
        self.screen.fill(background_fill)
        font = pygame.font.SysFont('Impact', 20)
        label = font.render('CHOOSE YOUR CHARACTERS!'.format(self.timer / fps), 1, (100, 200, 100))
        self.screen.blit(label, (450, 100))



