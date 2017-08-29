import pygame

from utils.hollow import textOutline
from utils.roundrects import round_rect
import colors
import vars

TOTAL_WAIT = 5

LEFT_ALIGN = vars.SCREEN_WIDTH / 6
CENTER_ALIGN = vars.SCREEN_WIDTH / 2
RIGHT_ALIGN = vars.SCREEN_WIDTH / 6 * 5


class ScoreboardContext:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.left_color = None
        self.right_color = None

    def main_loop(self, game_data):
        self.left_color = game_data[0]['char'].color
        self.right_color = game_data[1]['char'].color

        l_total = int(game_data[0]['time']) + int(game_data[0]['poop']) + int(game_data[0]['break'])
        r_total = int(game_data[1]['time']) + int(game_data[1]['poop']) + int(game_data[1]['break'])

        _p1 = pygame.transform.scale(game_data[0]['char'].portrait, (150, 150))
        _p1 = pygame.transform.flip(_p1, True, False)
        _p2 = pygame.transform.scale(game_data[1]['char'].portrait, (150, 150))

        start_timer = 0
        end_timer = 0

        while True:
            self.clock.tick(vars.fps)

            self.timer += 1
            self.screen.fill(colors.black)

            round_rect(self.screen, (LEFT_ALIGN-150, 150, 300, 420), self.left_color, 20, 5)
            round_rect(self.screen, (LEFT_ALIGN-155, 145, 310, 430), self.left_color, 20, 2)
            round_rect(self.screen, (RIGHT_ALIGN-150, 150, 300, 420), self.right_color, 20, 5)
            round_rect(self.screen, (RIGHT_ALIGN-155, 145, 310, 430), self.right_color, 20, 2)
            pygame.draw.rect(self.screen, colors.black, (LEFT_ALIGN - _p1.get_width() / 2 - 10, 75, _p1.get_width()+20, 800), 0)
            pygame.draw.rect(self.screen, colors.black, (RIGHT_ALIGN - _p2.get_width() / 2 - 10, 75, _p2.get_width()+20, 800), 0)

            font = pygame.font.SysFont('Arial', 40)
            label = font.render('SCORE!'.format(self.timer / vars.fps), 1, (100, 150, 200))
            self.screen.blit(label, (CENTER_ALIGN-label.get_width()/2, 200))

            pygame.draw.rect(self.screen, colors.black, (LEFT_ALIGN-_p1.get_width()/2, 75, _p1.get_width(), _p1.get_height()), )
            self.screen.blit(_p1, (LEFT_ALIGN-_p1.get_width()/2, 75))
            pygame.draw.rect(self.screen, self.left_color, (LEFT_ALIGN-_p1.get_width()/2, 75, _p1.get_width(), _p1.get_height()), 6)

            pygame.draw.rect(self.screen, colors.black, (RIGHT_ALIGN-_p2.get_width()/2, 75, _p2.get_width(), _p2.get_height()), 0)
            self.screen.blit(_p2, (RIGHT_ALIGN-_p2.get_width()/2, 75))
            pygame.draw.rect(self.screen, self.right_color, (RIGHT_ALIGN-_p2.get_width()/2, 75, _p2.get_width(), _p2.get_height()), 6)

            if self.timer > int(vars.fps * 1.75):
                self.show_stat(font, game_data[0]['time'], game_data[1]['time'], 'TIME', 280)

            if self.timer > int(vars.fps * 3):
                self.show_stat(font, game_data[0]['break'], game_data[1]['break'], 'ITEMS BROKEN', 340)

            if self.timer > int(vars.fps * 4.25):
                self.show_stat(font, game_data[0]['poop'], game_data[1]['poop'], 'POOP', 400)

            if self.timer > int(vars.fps * 6.3):
                self.show_stat(font, l_total, r_total, 'TOTAL', 540)

            if start_timer < int(vars.fps / 2):
                fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                fade_overlay.fill(colors.black)
                fade_overlay.set_alpha(((int(vars.fps / 2) - start_timer) / int(vars.fps / 2)) * 255)
                self.screen.blit(fade_overlay, (0, 0))
                start_timer += 1

            if self.timer > int(vars.fps * 10):
                if end_timer > int(vars.fps / 2):
                    return
                else:
                    fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                    fade_overlay.fill(colors.black)
                    fade_overlay.set_alpha((end_timer / int(vars.fps / 2)) * 255)
                    self.screen.blit(fade_overlay, (0, 0))
                    end_timer += 1

            pygame.display.update()
            pygame.event.get()

    def show_stat(self, font, left_val, right_val, stat_label, y):
        label = font.render(stat_label, 1, colors.white)
        self.screen.blit(label, (CENTER_ALIGN-label.get_width()/2, y))

        label = textOutline(font, str(left_val), colors.black, self.left_color)
        self.screen.blit(label, (LEFT_ALIGN-label.get_width()/2, y))

        label = textOutline(font, str(right_val), colors.black, self.right_color)
        self.screen.blit(label, (RIGHT_ALIGN-label.get_width()/2, y))

    # def show_total(self, font, game_data):
    #     label = font.render('Total', 1, (255, 255, 255))
    #     self.screen.blit(label, (300, 360))
    #
    #     label = font.render(str(total), 1, game_data[1]['color'])
    #     self.screen.blit(label, (800, 360))
    #
    # def show_poop(self, font, game_data):
    #     label = font.render('Poop', 1, (255, 255, 255))
    #     self.screen.blit(label, (300, 320))
    #
    #     label = font.render(str(game_data[0]['poop']), 1, game_data[0]['color'])
    #     self.screen.blit(label, (200, 320))
    #
    #     label = font.render(str(game_data[1]['poop']), 1, game_data[1]['color'])
    #     self.screen.blit(label, (800, 320))
    #
    # def show_break(self, font, game_data):
    #     label = font.render('Items broken', 1, (255, 255, 255))
    #     self.screen.blit(label, (300, 300))
    #
    #     label = font.render(str(game_data[0]['break']), 1, game_data[0]['color'])
    #     self.screen.blit(label, (200, 300))
    #
    #     label = font.render(str(game_data[1]['break']), 1, game_data[1]['color'])
    #     self.screen.blit(label, (800, 300))
    #
    # def show_time(self, font, game_data):
    #     label = font.render('Time', 1, (255, 255, 255))
    #     self.screen.blit(label, (300, 280))
    #
    #     label = font.render(str(game_data[0]['time']), 1, game_data[0]['color'])
    #     self.screen.blit(label, (200, 280))
    #
    #     label = font.render(str(game_data[1]['time']), 1, game_data[1]['color'])
    #     self.screen.blit(label, (800, 280))
    #
    #
    #     # TODO:  All these placements should be dynamic or something so it doesn't look like shit
