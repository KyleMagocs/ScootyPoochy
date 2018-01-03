import pygame

import debugcontrols
from contexts.char_select import CharacterSelectContext
from contexts.attract import AttractContext
from contexts.char_select_new import CharacterSelectTrackballContext
from contexts.game import GameContext
from contexts.howtoplay import HowToPlayContext
from contexts.level_select import LevelSelectContext
from contexts.scoreboard import ScoreboardContext
from contexts.startup import StartupContext
from contexts.title import TitleContext
from contexts.winscreen import WinscreenContext
from objects.Characters import Cooper, Doge, Beef
from objects.Level import TempLevel, ButtLevel, ShortLevel, DecentLevel
from objects.Player import Player
import vars
from utils.lights import ColorLib
from utils.sounds import MusicLib


class GlobalContext:
    def __init__(self, screen):
        self.screen = screen

    def main_loop(self):
        p1 = Player(0, 0)
        p2 = Player(1, 0)

        while True:

            player_array = []
            if not debugcontrols.skip_intro:
                MusicLib.update_volume(1)
                MusicLib.play_title()
                ColorLib.set_colors(b'w', b'w')
                while True:
                    title = TitleContext(self.screen)
                    if title.display_loop():
                        break
                    # attract = AttractContext(self.screen)
                    # attract.display_loop()
                pygame.event.clear()
                if debugcontrols.use_keyboard_character_select:
                    select = CharacterSelectContext(self.screen, p1, p2)
                else:
                    select = CharacterSelectTrackballContext(self.screen, p1, p2)
                characters = select.main_loop()

                # theme_select = LevelSelectContext(self.screen)
                # theme = theme_select.main_loop()
                # TODO:  Build level here
            else:
                characters = [Beef(), Doge()]
            levels = [ButtLevel(), None]
            if not debugcontrols.skip_intro:
                howtoplay = HowToPlayContext(self.screen)
                howtoplay.display_loop()
            game = GameContext(self.screen, characters, levels, p1, p2)
            game_data = game.run_game()

            scoreboard = ScoreboardContext(self.screen)  # TODO:  Probably needs players
            scoreboard.main_loop(game_data)

            winscreen = WinscreenContext(self.screen)

            # BAD >: ( DON'T DO THIS
            l_total = int(game_data[0]['time']) + int(game_data[0]['poop']) + int(game_data[0]['break'])
            r_total = int(game_data[1]['time']) + int(game_data[1]['poop']) + int(game_data[1]['break'])
            if l_total > r_total:
                winscreen.display_loop(characters[0])
            elif r_total > l_total:
                winscreen.display_loop(characters[1])
            else:
                pass  # ITS A DRAW, I DON'T KNOW WHAT TO DO
