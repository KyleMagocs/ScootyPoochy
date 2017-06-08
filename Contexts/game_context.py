import os
import pygame

import math
from Objects import Characters
from Objects.World import World
from controller_interface.trackball import Trackball

bg_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'temp_images', 'background.png')
player_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'temp_images', 'TEMPDOG_sprite_temp.png')

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPRITE_WIDTH = 60

CONTROL_TYPE = 'TRACKBALL'


class GameContext:
    size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
    num_players = None
    player_sprites = list()

    def __init__(self, screen, character_list):
        self.background = None
        self.num_players = len(character_list)

        self.screen = screen

        self.objects = pygame.sprite.Group()  # hold level objects

        self.worlds = list()

        for i in range(0, len(character_list)):
            _world = World(width=(SCREEN_WIDTH / self.num_players), x_offset=i)
            _world.player_character.y = 700
            _world.player_character.set_character(character_list[i])
            self.worlds.append(_world)

        self.players = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.gameOverFlag = 0
        self.gameOverCount = 0

    def draw_bg(self):
        # self.screen.blit(self.background, (0, 0))
        pass

    def draw_hud(self):
        pass

    def draw_sprites(self):
        self.draw_level_sprites()

    def draw_level_sprites(self):
        pass  # TODO:  world object should do this?

    def parse_keys(self, keys):
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

    def run_game(self):
        clock = pygame.time.Clock()
        fps = 30

        while True:
            for world in self.worlds:
                input = world.player_character.read_input()
                left = input['left']
                right = input['right']

                new_y_vel = (left[1]/50 + right[1]/50) / 2 * Characters.ACCEL_COEF
                new_x_vel = ((left[0]/50 - 1) + (right[0]/50 + 1)) / 2 * Characters.ACCEL_COEF

                world.player_character.x_speed = world.player_character.x_speed - new_x_vel
                world.player_character.y_speed = world.player_character.y_speed + new_y_vel

            keystate = pygame.key.get_pressed()
            if keystate:
                self.parse_keys(keystate)

            for world in self.worlds:
                world.player_character.x_speed = world.player_character.x_speed / world.level.theme.friction
                world.player_character.y_speed = world.player_character.y_speed / world.level.theme.friction
                world.update()
                world.draw(self.screen)
            pygame.display.flip()
            clock.tick(fps)
