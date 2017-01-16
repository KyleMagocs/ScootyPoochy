from Contexts.game_context import GameContext
from Objects.Characters import *
import pygame

if __name__ == "__main__":
    pygame.init()
    game = GameContext((TestCharacter(), TestCharacter()))
    game.run_game()