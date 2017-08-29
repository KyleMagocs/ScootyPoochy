import pygame

import colors
from objects.LevelObjects import Lamp
from objects.Player import Player
from objects.World import World
from utils.hollow import textHollow, textOutline

import vars


class GameContext:
    size = width, height = vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT
    num_players = None
    player_sprites = list()


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

        self.world = World(width=600, y_offset=vars.SCREEN_HEIGHT+10, level=levels[0])

        self.world.player_one.y = levels[0].height - vars.PLAYER_START_Y
        self.world.player_one.set_character(character_list[0])

        self.world.player_two.y = levels[0].height - vars.PLAYER_START_Y
        self.world.player_two.set_character(character_list[1])

        # self.players_group = pygame.sprite.Group()

        self.clock = pygame.time.Clock()

        self.gameOverFlag = 0
        self.gameOverCount = 0

    def draw_hud(self, screen):
        pygame.draw.line(screen, colors.white, (vars.SCREEN_WIDTH/2, 100), (vars.SCREEN_WIDTH/2, vars.SCREEN_HEIGHT-100), 4)
        pygame.draw.line(screen, colors.white, (vars.SCREEN_WIDTH / 2 - 50, 100), (vars.SCREEN_WIDTH / 2 + 50, 100), 4)
        pygame.draw.line(screen, colors.white, (vars.SCREEN_WIDTH / 2 - 50, vars.SCREEN_HEIGHT-100), (vars.SCREEN_WIDTH / 2 + 50, vars.SCREEN_HEIGHT-100), 4)
        pygame.draw.line(screen, colors.white, (vars.SCREEN_WIDTH / 2 - 25, vars.SCREEN_HEIGHT/2), (vars.SCREEN_WIDTH / 2 + 25, vars.SCREEN_HEIGHT/2), 4)
        # draw p1
        # draw p2
        _prog = self.world.get_progress()
        p1_y = int(_prog[0] * (vars.SCREEN_HEIGHT - 210))
        p2_y = int(_prog[1] * (vars.SCREEN_HEIGHT - 210))

        pygame.draw.circle(screen, self.world.player_one.character.color, (int(vars.SCREEN_WIDTH/2 - 15), p1_y + 105), 8, 6)
        pygame.draw.circle(screen, self.world.player_two.character.color, (int(vars.SCREEN_WIDTH/2 + 15), p2_y + 105), 8, 6)

    def check_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.world.player_one.jump()
                if event.key == pygame.K_RETURN:
                    self.world.player_two.jump()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    def run_game(self):
        clock = pygame.time.Clock()
        start_timer = 0
        end_timer = 0
        while True:


            real_fps = clock.tick(vars.fps)

            self.screen.fill(colors.black)


            p1_left, p1_right = self.players[0].read_input()
            p2_left, p2_right = self.players[1].read_input()

            results = self.world.update(p1_left, p1_right, p2_left, p2_right)
            self.world.draw(self.screen)

            self.draw_hud(self.screen)

            if vars.debug_mode:
                font = pygame.font.SysFont('Comic Sans MS', 25)
                label = font.render(str(real_fps), 1, (0,255,255))
                self.screen.blit(label, (vars.SCREEN_WIDTH/2-label.get_width()/2, vars.SCREEN_HEIGHT-75))

            if start_timer < int(vars.fps / 2):
                fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                fade_overlay.fill(colors.black)
                fade_overlay.set_alpha(((int(vars.fps / 2) - start_timer) / int(vars.fps / 2)) * 255)
                self.screen.blit(fade_overlay, (0, 0))
                start_timer += 1

            if results is not None:
                self.finish_timer += 1

            if self.finish_timer > 75:
                if end_timer > int(vars.fps / 2):
                    return results
                else:
                    fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                    fade_overlay.fill(colors.black)
                    fade_overlay.set_alpha((end_timer / int(vars.fps / 2)) * 255)
                    self.screen.blit(fade_overlay, (0, 0))
                    end_timer += 1

                # TODO:  FANCY FINISH ANIMATION

            self.check_keys()

            pygame.display.update()
            pygame.event.get()




