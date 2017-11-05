import pygame
import vars
import colors
from utils.sounds import SoundLib

class WinscreenContext:
    TIMEOUT = 5 * vars.fps

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def display_loop(self, winning_character):
        SoundLib.winsound(winning_character.winsound)
        while self.timer < self.TIMEOUT:

            self.clock.tick(vars.fps)

            self.timer += 1
            self.screen.fill(colors.black)

            portrait = winning_character.portrait

            self.screen.blit(portrait, (vars.SCREEN_WIDTH/2 - portrait.get_width() / 2, vars.SCREEN_HEIGHT/3))
            font = pygame.font.SysFont('Arial', 40)
            label = font.render('"' + winning_character.wintext + '"', 1, (100, 150, 200))
            self.screen.blit(label, (vars.SCREEN_WIDTH/2-label.get_width()/2, 200))

            if self.timer < int(vars.fps / 2):
                fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                fade_overlay.fill(colors.black)
                fade_overlay.set_alpha(((int(vars.fps / 2) - self.timer) / int(vars.fps / 2)) * 255)
                self.screen.blit(fade_overlay, (0, 0))
                self.timer += 1

            pygame.display.update()
            pygame.event.get()