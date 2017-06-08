import pygame

from Contexts.game_context import GameContext
from Objects.Characters import TestCharacter
from vars import fps


class CharacterSelectContext:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()

    def main_loop(self):
        for i in range(0, 5*fps):
            self.screen.fill((0, 0, 0))
            font = pygame.font.SysFont('Comic Sans MS', 15)
            label = font.render('SELECT YOUR CHARACTER!', 1, (100, 200, 100))
            self.screen.blit(label, (200, 200))
            pygame.display.flip()
            self.clock.tick(fps)
            pygame.event.get()
        return [TestCharacter(), ]