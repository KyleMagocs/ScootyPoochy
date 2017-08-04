import pygame

from contexts.char_select import CharacterSelectContext
from contexts.attract import AttractContext
from contexts.game import GameContext
from contexts.level_select import LevelSelectContext
from contexts.scoreboard import ScoreboardContext
from contexts.startup import StartupContext
from contexts.title import TitleContext
from objects.Characters import TestCharacter, Doge
from objects.Level import TempLevel
from objects.Player import Player
from vars import skip_intro


class GlobalContext:
    def __init__(self, screen):
        self.screen = screen

    def main_loop(self):
        while True:
            player_array = []
            if not skip_intro:
                while True:
                    title = TitleContext(self.screen)
                    if title.display_loop():
                        break
                    attract = AttractContext(self.screen)
                    attract.display_loop()
                pygame.event.clear()
                select = CharacterSelectContext(self.screen)
                characters = select.main_loop()

                theme_select = LevelSelectContext(self.screen)
                theme = theme_select.main_loop()
                # TODO:  Build level here
            else:
                characters = [Doge(), Doge()]
            levels = [TempLevel(), TempLevel()]
            game = GameContext(self.screen, characters, levels)
            game_data = game.run_game()

            scoreboard = ScoreboardContext(self.screen)  # TODO:  Probably needs players
            scoreboard.main_loop(game_data)