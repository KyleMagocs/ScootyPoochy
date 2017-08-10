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
            player.world = World(width=(SCREEN_WIDTH / self.num_players), x_offset=i, y_offset=SCREEN_HEIGHT+10, level=levels[i])
            player.world.player_character.y = levels[i].height - PLAYER_START_Y
            player.world.player_character.set_character(character_list[i])
            self.players.append(player)

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
        p1_y = int(self.players[0].get_progress() * (SCREEN_HEIGHT - 200)) + 75
        p2_y = int(self.players[1].get_progress() * (SCREEN_HEIGHT - 200)) + 75   # This math is stupid
        pygame.draw.circle(screen, self.players[0].world.player_character.character.color, (int(SCREEN_WIDTH/2 - 15), p1_y), 8, 6)
        pygame.draw.circle(screen, self.players[1].world.player_character.character.color, (int(SCREEN_WIDTH/2 + 15), p2_y), 8, 6)

    # def draw_sprites(self):
    #     self.draw_level_sprites()
    # #
    # # def draw_level_sprites(self):
    # #     pass  # TODO:  world object should do this?

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

    def is_game_complete(self):
        return len([x for x in self.players if x.world.finish is True]) == len(self.players)

    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            self.screen.fill((255, 255, 255))
            for player in self.players:  # should iterate on Players, who have Worlds
                left, right = (0, 0), (0, 0)
                if len(self.countdown) <= 1 or skip_countdown:
                    if not self.is_game_complete():
                        player.world.start_timer()
                    left, right = player.read_input()
                player.world.player_character.update_limbs(left, right)
                x_vel, y_vel = player.get_velocity(left, right)
                if player.world.update(x_vel, y_vel):
                    self.victory = True  # mark game finish because

                player.world.draw(self.screen)
                if not skip_countdown:
                    if len(self.countdown) > 0:
                        player.world.draw_countdown(self.screen, self.countdown[0], self.start_timer*3)

            self.draw_hud(self.screen)

            if self.is_game_complete():
                self.finish_timer += 1

            if self.finish_timer > 90:
                return [self.players[0].world.get_score(),
                        self.players[1].world.get_score()
                        ]
                # TODO:  FANCY FINISH ANIMATION

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




