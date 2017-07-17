import pygame

import colors
from utils.hollow import textHollow
from vars import fps

TOTAL_WAIT = 5


class TitleContext:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def display_loop(self):
        while True:
            self.timer += 1
            if self.timer > TOTAL_WAIT * fps:
                return 0
            keystate = pygame.key.get_pressed()
            if keystate:
                if self.parse_keys(keystate):
                    return 1

            self.screen.fill((0, 0, 0))
            font = pygame.font.SysFont('Comic Sans MS', 15)
            font2 = pygame.font.SysFont('Impact', 70)

            if (self.timer // 30) % 2 == 0:
                label = font.render('TITLE! {0:.2f}'.format(self.timer/fps), 1, (255, 0, 255))
            else:
                label = font.render('TITLE! {0:.2f}'.format(self.timer/fps), 1, (255, 255, 255))
            self.screen.blit(label, (200, 150))

            bigfont = pygame.font.Font(None, 90)
            title_text = textHollow(font2, 'SUPER POOCH SCOOT !!', colors.blue)
            # label = font2.render('SUPER POOCH SCOOT !!'.format(self.timer / fps), 1, (255, 0, 255))
            self.screen.blit(title_text, (300, 250))

            pygame.display.flip()

            self.clock.tick(fps)
            pygame.event.get()

    def parse_keys(self, keys):
        if keys[pygame.K_RETURN]:
            pygame.event.clear()
            return True
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        else:
            return False
