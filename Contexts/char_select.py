import pygame

from Objects.Characters import TestCharacter
from vars import fps
from colors import *

TOTAL_WAIT = 5




class CharacterSelectContext:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def main_loop(self):
        while True:
            self.timer += 1
            if self.timer > TOTAL_WAIT * fps:
                return [TestCharacter(), ]
            self.draw_background()

            pygame.display.flip()
            self.clock.tick(fps)
            pygame.event.get()

    def draw_background(self):
        self.screen.fill(background_fill)
        font = pygame.font.SysFont('Comic Sans MS', 15)
        label = font.render('CHOOSE YOUR CHARACTERS! {0:.2f}'.format(self.timer / fps), 1, (100, 200, 100))
        self.screen.blit(label, (200, 200))