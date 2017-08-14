import pygame

import colors
from objects.LevelObjects import Lamp
from objects.Player import Player
from objects.World import World
from utils.hollow import textHollow, textOutline

from vars import SCREEN_WIDTH, SCREEN_HEIGHT
from vars import fps, skip_countdown
from vars import PLAYER_START_Y


class GameContext:
    size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
    num_players = None
    player_sprites = list()
    countdown = ['3', '2', '1', 'GO!']

    def __init__(self, screen, character_list, levels):  # TODO:  This should receive players, not characters
        self.background = None
        self.num_players = len(character_list)
        self.screen = screen
        self.victory = False

        self.start_timer = 0
        self.finish_timer = 0
        # self.objects = pygame.sprite.Group()  # hold level objects

        self.players = []

        for i in range(0, len(character_list)):
            player = Player(i, i)
            self.players.append(player)

        self.world = World(width=(SCREEN_WIDTH / self.num_players), y_offset=SCREEN_HEIGHT+10, level=levels[0])

        self.world.player_one.y = levels[0].height - PLAYER_START_Y
        self.world.player_one.set_character(character_list[0])

        self.world.player_two.y = levels[0].height - PLAYER_START_Y
        self.world.player_two.set_character(character_list[0])

        # self.players_group = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.gameOverFlag = 0
        self.gameOverCount = 0

    def draw_hud(self, screen):
        pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH/2, 100), (SCREEN_WIDTH/2, SCREEN_HEIGHT-100), 5)
        pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH / 2 - 50, 100), (SCREEN_WIDTH / 2 + 50, 100), 5)
        pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT-100), (SCREEN_WIDTH / 2 + 50, SCREEN_HEIGHT-100), 5)
        pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH / 2 - 25, SCREEN_HEIGHT/2), (SCREEN_WIDTH / 2 + 25, SCREEN_HEIGHT/2), 5)
        # draw p1
        # draw p2
        _prog = self.world.get_progress()
        p1_y = int(_prog[0] * (SCREEN_HEIGHT - 210))
        p2_y = int(_prog[1] * (SCREEN_HEIGHT - 210))

        pygame.draw.circle(screen, self.world.player_one.character.color, (int(SCREEN_WIDTH/2 - 15), p1_y + 105), 8, 6)
        pygame.draw.circle(screen, self.world.player_two.character.color, (int(SCREEN_WIDTH/2 + 15), p2_y + 105), 8, 6)

    def check_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.players[0].world.player_character.jump()
                if event.key == pygame.K_RETURN:
                    self.players[1].world.player_character.jump()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    # def is_game_complete(self):
    #     return len([x for x in self.players if x.world.finish is True]) == len(self.players)

    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            self.screen.fill((255, 255, 255))

            p1_left, p1_right = self.players[0].read_input()
            p2_left, p2_right = self.players[1].read_input()

            self.world.player_one.update_limbs(p1_left, p1_right)
            self.world.player_two.update_limbs(p1_left, p1_right)
            p1_vel = self.players[0].get_velocity(p1_left, p1_right)
            p2_vel = self.players[1].get_velocity(p2_left, p2_right)

            self.world.update(p1_vel, p2_vel)
            self.world.draw(self.screen)
            #
            # for player in self.players:  # should iterate on Players, who have Worlds
            #     left, right = (0, 0), (0, 0)
            #     if skip_countdown or len(self.countdown) <= 1:
            #         if not self.is_game_complete():
            #             player.world.start_timer()
            #         left, right = player.read_input()
            #     player.world.player_character.update_limbs(left, right)
            #     x_vel, y_vel = player.get_velocity(left, right)
            #     if player.world.update(x_vel, y_vel):
            #         self.victory = True  # mark game finish because
            #
            #     player.world.draw(self.screen)
            #     if not skip_countdown:
            #         if len(self.countdown) > 0:
            #             player.world.draw_countdown(self.screen, self.countdown[0], self.start_timer*3)

            self.draw_hud(self.screen)

            #
            # if self.is_game_complete():
            #     self.finish_timer += 1

            # if self.finish_timer > 90:
            #     return [self.players[0].world.get_score(),
            #             self.players[1].world.get_score()
            #             ]
            #     # TODO:  FANCY FINISH ANIMATION

            if not skip_countdown:
                if self.start_timer < int(fps) and len(self.countdown) > 0:
                    self.start_timer += 1
                else:
                    if len(self.countdown) > 0:
                        self.countdown.remove(self.countdown[0])

                    self.start_timer = 0

            self.check_keys()

            pygame.display.flip()
            clock.tick(fps)
            pygame.event.get()




