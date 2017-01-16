from Contexts.game_context import GameContext
from Objects.Characters import *
import pygame

if __name__ == "__main__":
    pygame.init()

    # THIS WOULD BE CALLED FROM A PLAYER SELECT CONTEXT, WHEREIN IT WOULD MAKE A SHITLOAD MORE SENSE
    game = GameContext((TestCharacter(), TestCharacter()))
    game.run_game()