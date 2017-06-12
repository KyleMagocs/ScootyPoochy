import os

import pygame

from Objects import Characters
from Objects.Player import Player
from Objects.World import World

bg_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'temp_images', 'background.png')
player_image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'temp_images', 'TEMPDOG_sprite_temp.png')

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPRITE_WIDTH = 60

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

        self.players = []

        for i in range(0, len(character_list)):
            player = Player(i)
            player.world = World(width=(SCREEN_WIDTH / self.num_players), x_offset=i, y_offset=SCREEN_HEIGHT+10, level=level)
            player.world.player_character.y = SCREEN_HEIGHT - 100
            player.world.player_character.set_character(character_list[i])
            self.players.append(player)

        self.players_group = pygame.sprite.Group()

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
        # try:
        while True:
            self.screen.fill((255, 255, 255))
            for player in self.players:  # should iterate on Players, who have Worlds
                player.handle_input()
                if player.world.update():
                    self.victory = True  # mark game finish because
                player.world.draw(self.screen)

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
        # except Exception as e:
        #     print(e)


