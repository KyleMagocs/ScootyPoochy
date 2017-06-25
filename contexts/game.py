import pygame

from objects.LevelObjects import Lamp
from objects.Player import Player
from objects.World import World

from vars import SCREEN_WIDTH, SCREEN_HEIGHT
from vars import fps


class GameContext:
    size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT
    num_players = None
    player_sprites = list()

    def __init__(self, screen, character_list, levels):  # TODO:  This should receive players, not characters
        self.background = None
        self.num_players = len(character_list)
        self.screen = screen
        self.victory = False
        # self.objects = pygame.sprite.Group()  # hold level objects

        self.players = []

        for i in range(0, len(character_list)):
            player = Player(i, i)
            player.world = World(width=(SCREEN_WIDTH / self.num_players), x_offset=i, y_offset=SCREEN_HEIGHT+10, level=levels[i])
            player.world.player_character.y = SCREEN_HEIGHT - 100
            player.world.player_character.set_character(character_list[i])
            self.players.append(player)

        # self.players_group = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.gameOverFlag = 0
        self.gameOverCount = 0

    def draw_hud(self):
        pass

    def draw_sprites(self):
        self.draw_level_sprites()
    #
    # def draw_level_sprites(self):
    #     pass  # TODO:  world object should do this?

    def check_keys(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

    def run_game(self):
        clock = pygame.time.Clock()
        try:
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

                self.check_keys()

                pygame.display.flip()
                clock.tick(fps)
                pygame.event.get()
        except Exception as e:
            print(e)




