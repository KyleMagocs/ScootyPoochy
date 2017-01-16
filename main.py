from Contexts.game_context import GameContext
import pygame

if __name__ == "__main__":
    pygame.init()
    game = GameContext()
    game.run_game()