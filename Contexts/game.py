import os

import pygame

from Objects import Characters
from Objects.World import World

bg_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'temp_images', 'background.png')
player_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'temp_images', 'TEMPDOG_sprite_temp.png')

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPRITE_WIDTH = 60

CONTROL_TYPE = 'TRACKBALL'


from vars import fps


class GameContext:
    size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
    num_players = None
    player_sprites = list()

    def __init__(self, screen, character_list, level):
        self.background = None
        self.num_players = len(character_list)
        self.screen = screen
        self.victory = False
        self.objects = pygame.sprite.Group()  # hold level objects

        self.worlds = list()

        for i in range(0, len(character_list)):
            _world = World(width=(SCREEN_WIDTH / self.num_players), x_offset=i, y_offset=SCREEN_HEIGHT+10, level=level)
            _world.player_character.y = SCREEN_HEIGHT - 100
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
        try:
            while True:
                self.screen.fill((255, 255, 255))
                for world in self.worlds:  # should iterate on Players, who have Worlds
                    self.handle_input(world)
                    if world.update():
                        self.victory = world  # mark victory for Player rather than World
                    world.draw(self.screen)

                if self.victory:
                    pass
                    # TODO:  FANCY FINISH ANIMATION
                    # TODO:  PROBABLY A TIMER TO WAIT FOR IT TO FINISH, SO LIKE 10 * FPS frames?
                    return self.victory

                keystate = pygame.key.get_pressed()
                if keystate:
                    self.parse_keys(keystate)

                pygame.display.flip()
                clock.tick(fps)
                pygame.event.get()
        except Exception as e:
            print(e)

    def handle_input(self, world):
        control_input = world.player_character.read_input()
        left = control_input['left']
        right = control_input['right']

        addtl_y_vel = (left[1] / 10 + right[1] / 10) / 2 * Characters.ACCEL_COEF
        addtl_x_vel = ((left[0] / 10 - 10) + (right[0] / 10 + 10)) / 2 * Characters.ACCEL_COEF

        world.player_character.y_speed = (world.player_character.y_speed + addtl_y_vel) / world.level.theme.friction

        world.player_character.x_speed = (world.player_character.x_speed - addtl_x_vel) / world.level.theme.friction
