from Contexts.char_select_context import CharacterSelectContext
from Contexts.eyecatch_context import EyecatchContext
from Contexts.game_context import GameContext
from Contexts.level_select_context import LevelSelectContext
from Contexts.startup_context import StartupContext
from Contexts.title_context import TitleContext
from Objects.Level import Level


class GlobalContext:
    def __init__(self, screen):
        self.screen = screen

    def main_loop(self):
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

        theme_select = LevelSelectContext(self.screen)
        theme = theme_select.main_loop()
        # TODO:  Build level here

        game = GameContext(self.screen, characters, Level())
        game.run_game()