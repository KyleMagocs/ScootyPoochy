import pygame
from vars import fps
TOTAL_WAIT = 3


class AttractContext:
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
            label = font.render('EYECATCH! {0:.2f}'.format(self.timer / fps), 1, (0, 255, 255))
            self.screen.blit(label, (200, 150))
            font = pygame.font.SysFont('Comic Sans', 60)
            label = font.render('PUT A VIDEO HERE'.format(self.timer / fps), 1, (0, 255, 255))
            self.screen.blit(label, (300, 450))
            pygame.display.update()

            self.clock.tick(fps)
            pygame.event.get()

    def parse_keys(self, keys):
        if len([x for x in keys if x == 1]):
            pygame.event.clear()
            return True
        else:
            return False
