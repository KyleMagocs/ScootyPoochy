from Contexts.char_select_context import CharacterSelectContext
from Contexts.eyecatch_context import EyecatchContext
from Contexts.game_context import GameContext
from Contexts.level_select_context import LevelSelectContext
from Contexts.scoreboard_context import ScoreboardContext
from Contexts.startup_context import StartupContext
from Contexts.title_context import TitleContext
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
                startup = StartupContext(self.screen)
                if not startup.display_startup():
                    quit()

                while True:
                    title = TitleContext(self.screen)
                    if title.display_loop():
                        break
                    eyecatch = EyecatchContext(self.screen)
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
            winning_player = game.run_game()

            scoreboard = ScoreboardContext(self.screen)  # TODO:  Probably needs players
            scoreboard.main_loop()