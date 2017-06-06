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

CONTROL_TYPE = 'KEYBOARD'  # TODO:  NOT THIS
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
            _world.player.y = 700
            _world.player.set_character(character_list[i])
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
        pass

    def parse_keys(self, keys):
        # TODO:  MAKE THIS LOGIC BETTER AND NOT HARDCODED
        # if keys[pygame.K_a]:
        #     print("A")
        #     # push player 1 left
        #     self.worlds[0].player.speed = min(self.worlds[0].player.speed + self.worlds[0].player.character.acceleration * Characters.ACCEL_COEF,
        #                                       self.worlds[0].player.character.max_speed)
        #     self.worlds[0].player.angle += self.worlds[0].player.character.handling
        #     print(self.worlds[0].player.angle)
        #
        # elif keys[pygame.K_d]:
        #     print("D")
        #     # push player 1 right
        #     self.worlds[0].player.speed = min(self.worlds[0].player.speed + self.worlds[0].player.character.acceleration * Characters.ACCEL_COEF,
        #                                       self.worlds[0].player.character.max_speed)
        #     self.worlds[0].player.angle -= self.worlds[0].player.character.handling
        #     print(self.worlds[0].player.angle)

        if keys[pygame.K_LEFT]:
            print("LEFT")
            # push player 2 left
            self.worlds[1].player.speed = min(self.worlds[1].player.speed + self.worlds[1].player.character.acceleration * Characters.ACCEL_COEF,
                                              self.worlds[1].player.character.max_speed)
            self.worlds[1].player.angle += self.worlds[1].player.character.handling
            print(self.worlds[1].player.angle)

        elif keys[pygame.K_RIGHT]:
            print("RIGHT")
            # push player 2 right
            self.worlds[1].player.speed = min(self.worlds[1].player.speed + self.worlds[1].player.character.acceleration * Characters.ACCEL_COEF,
                                              self.worlds[1].player.character.max_speed)
            self.worlds[1].player.angle -= self.worlds[1].player.character.handling
            print(self.worlds[1].player.angle)

        if keys[pygame.K_ESCAPE]:
            pygame.quit()

    def run_game(self):
        clock = pygame.time.Clock()
        fps = 30

        while True:
            if CONTROL_TYPE == 'KEYBOARD':
                for event in pygame.event.get():
                    pass
                keystate = pygame.key.get_pressed()
                if keystate:
                    self.parse_keys(keystate)
                    pass
            elif CONTROL_TYPE == 'TRACKBALL':
                for world in self.worlds:
                    input = world.player.read_input()
                    left = input['left']
                    right = input['right']

                    new_y_vel = (left[1]/75 + right[1]/75) / 2 * Characters.ACCEL_COEF
                    new_x_vel = ((left[0]/75 - .5) + (right[0]/75 + 0.5)) / 2 * Characters.ACCEL_COEF

                    world.player.x_speed = world.player.x_speed - new_x_vel
                    world.player.y_speed = world.player.y_speed + new_y_vel


                # still gotta read keystate here for now
                keystate = pygame.key.get_pressed()
                if keystate:
                    self.parse_keys(keystate)

            for world in self.worlds:
                world.player.x_speed = world.player.x_speed / world.level.theme.friction
                world.player.y_speed = world.player.y_speed / world.level.theme.friction
                world.update()
                world.draw(self.screen)
            pygame.display.update()
            clock.tick(fps)
