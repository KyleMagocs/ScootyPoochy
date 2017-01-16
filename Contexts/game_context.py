import os

import pygame
import time
from Objects.Player import Player
from Objects.World import World

bg_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'temp_images', 'background.png')
player_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'temp_images', 'player.png')

MAX_SPEED = 20

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

class GameContext:
    size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT

    def __init__(self):
        self.background = None
        self.player1_sprite = None
        self.player2_sprite = None

        self.screen = pygame.display.set_mode(self.size)
        self.objects = pygame.sprite.Group()  # hold level objects

        self.player1_world = World(x_offset=0)
        self.player2_world = World(x_offset=SCREEN_WIDTH / 2)
        self.player1_world.player = Player()
        self.player1_world.player.x = 120
        self.player1_world.player.y = 700
        self.player2_world.player = Player()
        self.player2_world.player.x = 420
        self.player2_world.player.y = 700
        self.players = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.gameOverFlag = 0
        self.gameOverCount = 0
        self.load_images()

    def load_images(self):
        self.background = pygame.image.load(bg_image_path)
        self.player1_sprite = pygame.image.load(player_image_path)
        self.player2_sprite = pygame.image.load(player_image_path)

    def draw_bg(self):
        # self.screen.blit(self.background, (0, 0))
        pass

    def draw_hud(self):
        pass

    def draw_sprites(self):
        self.draw_player_sprites()
        self.draw_level_sprites()

    def draw_player_sprites(self):
        # TODO:  MOVE TO World.py
        self.screen.blit(self.player1_sprite, (self.player1_world.player.x, self.player1_world.player.y))
        self.screen.blit(self.player2_sprite, (self.player2_world.player.x, self.player2_world.player.y))

    def draw_level_sprites(self):
        pass

    def parse_keys(self, keys):
        if keys[pygame.K_a]:
            print("A")
            # push player 1 left
            self.player1_world.player.speed = min(self.player1_world.player.speed + 1, MAX_SPEED)
            self.player1_world.player.angle -= 1
            self.player1_world.player.x -= 1  # REMOVE LATER
            pass
        elif keys[pygame.K_d]:
            print("D")
            # push player 1 right
            self.player1_world.player.speed = min(self.player1_world.player.speed + 1, MAX_SPEED)
            self.player1_world.player.angle += 1
            self.player1_world.player.x += 1  # REMOVE LATER
            pass

        if keys[pygame.K_LEFT]:
            print("LEFT")
            # push player 2 left
            self.player2_world.player.speed = min(self.player2_world.player.speed + 1, MAX_SPEED)
            self.player2_world.player.angle -= 1
            self.player2_world.player.x -= 1  # REMOVE LATER

        elif keys[pygame.K_RIGHT]:
            print("RIGHT")
            # push player 2 right
            self.player2_world.player.speed = min(self.player2_world.player.speed + 1, MAX_SPEED)
            self.player2_world.player.angle += 1
            self.player2_world.player.x += 1  # REMOVE LATER

    # TODO: MOVE TO World.py
    def update_player_one_position(self):
        pass

    def update_player_two_position(self):
        pass

    def run_game(self):
        clock = pygame.time.Clock()
        fps = 30

        while True:
            for event in pygame.event.get():
                pass
            keystate = pygame.key.get_pressed()
            if keystate:
                self.parse_keys(keystate)
                pass

            self.draw_bg()
            self.draw_sprites()
            pygame.display.update()
            clock.tick(fps)
