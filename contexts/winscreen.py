import random
random.seed()
import pygame
import vars
import colors
from utils.lights import ColorLib
from utils.sounds import SoundLib

class WinscreenContext:
    TIMEOUT = 7 * vars.fps

    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def display_loop(self, winning_character):
        SoundLib.winsound(winning_character.winsound)
        ColorLib.set_colors(winning_character.colorcode, winning_character.colorcode)
        text = winning_character.wintext[random.randint(0, len(winning_character.wintext) - 1)]

        while self.timer < self.TIMEOUT:

            self.clock.tick(vars.fps)

            self.timer += 1
            self.screen.fill(colors.black)

            portrait = winning_character.victory_portrait

            self.screen.blit(portrait, (vars.SCREEN_WIDTH/2 - portrait.get_width() / 2, vars.SCREEN_HEIGHT/3))
            pygame.draw.rect(self.screen, winning_character.color, (vars.SCREEN_WIDTH / 2 - portrait.get_width() / 2, vars.SCREEN_HEIGHT/3, portrait.get_width(), portrait.get_height()), 6)
            font = pygame.font.SysFont('Arial', 40)
            font2 = pygame.font.SysFont('Arial', 60)

            label = font2.render('WINNER', 1, winning_character.color)
            self.screen.blit(label, (vars.SCREEN_WIDTH/2-label.get_width()/2, 70))
            label = font.render(winning_character.name, 1, winning_character.color)
            self.screen.blit(label, (vars.SCREEN_WIDTH / 2 - label.get_width() / 2, 175))

            label = font.render(text, 1, winning_character.color)
            self.screen.blit(label, (vars.SCREEN_WIDTH/2-label.get_width()/2, vars.SCREEN_HEIGHT/3 + portrait.get_height() + 15))

            if self.timer < int(vars.fps / 2):
                fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                fade_overlay.fill(colors.black)
                fade_overlay.set_alpha(((int(vars.fps / 2) - self.timer) / int(vars.fps / 2)) * 255)
                self.screen.blit(fade_overlay, (0, 0))
            if self.timer > self.TIMEOUT - int(vars.fps / 2):
                fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                fade_overlay.fill(colors.black)
                fade_overlay.set_alpha((self.timer / int(vars.fps / 2)) * 255)
                self.screen.blit(fade_overlay, (0, 0))

            pygame.display.update()
            pygame.event.get()