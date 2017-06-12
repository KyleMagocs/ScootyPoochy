from Contexts.char_select import CharacterSelectContext
from Contexts.attract import AttractContext
from Contexts.game import GameContext
from Contexts.level_select import LevelSelectContext
from Contexts.scoreboard import ScoreboardContext
from Contexts.startup import StartupContext
from Contexts.title import TitleContext
from Objects.Characters import TestCharacter
from Objects.Level import TempLevel
from Objects.Player import Player
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
                    eyecatch = AttractContext(self.screen)
                    eyecatch.display_loop()

                select = CharacterSelectContext(self.screen)
                characters = select.main_loop()

                # for i in range(0, len(characters)):
                #     player_array.append(Player(i))   # TODO:  Expand this

                theme_select = LevelSelectContext(self.screen)
                theme = theme_select.main_loop()
                # TODO:  Build level here
            else:
                characters = [TestCharacter(),]
            game = GameContext(self.screen, characters, TempLevel())
            game_data = game.run_game()

            scoreboard = ScoreboardContext(self.screen)  # TODO:  Probably needs players
            scoreboard.main_loop(game_data)