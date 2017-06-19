import pygame

from objects.Characters import TestCharacter
from vars import fps

TOTAL_WAIT = 5

class LevelSelectContext:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def main_loop(self):
        while True:
            self.timer += 1
            if self.timer > TOTAL_WAIT * fps:
                return [None, ]
            self.screen.fill((0, 0, 0))
            font = pygame.font.SysFont('Comic Sans MS', 15)
            label = font.render('CHOOSE A LEVEL ! {0:.2f}'.format(self.timer/fps), 1, (255, 255, 0))
            self.screen.blit(label, (200, 200))
            pygame.display.flip()
            self.clock.tick(fps)
            pygame.event.get()
