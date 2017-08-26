import pygame

from contexts.scoreboard import ScoreboardContext
from objects.Characters import Doge, Nort

pygame.init()
screen = pygame.display.set_mode((1280, 800))
game_data = ({'time': 1000,
              'break': 1000,
              # todo: 1000,
              'poop': 1000,
              'char': Doge(), },
             {'time': 1000,
              'break': 1000,
              # todo: 1000,
              'poop': 1000,
              'char': Nort(), })
scoreboard = ScoreboardContext(screen)  # TODO:  Probably needs players
scoreboard.main_loop(game_data)
