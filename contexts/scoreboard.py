import pygame

from vars import fps

TOTAL_WAIT = 5


class ScoreboardContext:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def main_loop(self, game_data):
        while True:
            self.timer += 1
            # if self.timer > TOTAL_WAIT * fps:
            #     return [None, ]
            self.screen.fill((0, 0, 0))
            font = pygame.font.SysFont('Arial', 15)
            label = font.render('SCOOOOOOOOORE BOOOOOOOOOARD ! {0:.2f}'.format(self.timer/fps), 1, (100, 150, 200))
            self.screen.blit(label, (200, 200))
            if self.timer > 40:
                self.show_time(font, game_data)
            if self.timer > 80:
                self.show_break(font, game_data)
            if self.timer > 120:
                self.show_poop(font, game_data)
            if self.timer > 175:
                self.show_total(font, game_data)
            if self.timer > 300:
                return

            pygame.display.flip()
            self.clock.tick(fps)
            pygame.event.get()

    def show_total(self, font, game_data):
        label = font.render('Total', 1, (255, 255, 255))
        self.screen.blit(label, (260, 330))
        label = font.render(str(game_data[0]['total']), 1, game_data[0]['color'])
        self.screen.blit(label, (200, 330))
        label = font.render(str(game_data[1]['total']), 1, game_data[1]['color'])
        self.screen.blit(label, (500, 330))

    def show_poop(self, font, game_data):
        label = font.render('Poop', 1, (255, 255, 255))
        self.screen.blit(label, (260, 290))
        label = font.render(str(game_data[0]['poop']), 1, game_data[0]['color'])
        self.screen.blit(label, (200, 290))
        label = font.render(str(game_data[1]['poop']), 1, game_data[1]['color'])
        self.screen.blit(label, (500, 290))

    def show_break(self, font, game_data):
        label = font.render('Items broken', 1, (255, 255, 255))
        self.screen.blit(label, (260, 270))
        label = font.render(str(game_data[0]['break']), 1, game_data[0]['color'])
        self.screen.blit(label, (200, 270))
        label = font.render(str(game_data[1]['break']), 1, game_data[1]['color'])
        self.screen.blit(label, (500, 270))

    def show_time(self, font, game_data):
        label = font.render('Time', 1, (255, 255, 255))
        self.screen.blit(label, (260, 250))
        label = font.render(str(game_data[0]['time']), 1, game_data[0]['color'])
        self.screen.blit(label, (200, 250))
        label = font.render(str(game_data[1]['time']), 1, game_data[1]['color'])
        self.screen.blit(label, (500, 250))
