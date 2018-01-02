import pygame

import colors
import debugcontrols
from objects.LevelObjects import Lamp
from objects.Player import Player
from objects.World import World
from utils.hollow import textHollow, textOutline
from utils.sounds import MusicLib
import vars


class GameContext:
    size = width, height = vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT
    num_players = None
    player_sprites = list()

    def __init__(self, screen, character_list, levels, p1, p2):  # TODO:  This should receive players, not characters
        self.background = None
        self.num_players = len(character_list)
        self.screen = screen
        self.victory = False

        self.start_timer = 0
        self.finish_timer = 0
        # self.objects = pygame.sprite.Group()  # hold level objects

        self.players = []

        self.players.append(p1)
        self.players.append(p2)

        self.world = World(width=600, players=self.players, y_offset=vars.SCREEN_HEIGHT + 10, level=levels[0])

        self.world.player_one.y = levels[0].height - vars.PLAYER_START_Y
        self.world.player_one.set_character(character_list[0])

        self.world.player_two.y = levels[0].height - vars.PLAYER_START_Y
        self.world.player_two.set_character(character_list[1])

        self.clock = pygame.time.Clock()

        self.gameOverFlag = 0
        self.gameOverCount = 0

        self.draw_frame = True

    def draw_hud(self, screen):
        pygame.draw.line(screen, colors.white, (vars.SCREEN_WIDTH / 2, 100), (vars.SCREEN_WIDTH / 2, vars.SCREEN_HEIGHT - 100), 4)
        pygame.draw.line(screen, colors.white, (vars.SCREEN_WIDTH / 2 - 35, 100), (vars.SCREEN_WIDTH / 2 + 35, 100), 4)
        pygame.draw.line(screen, colors.white, (vars.SCREEN_WIDTH / 2 - 35, vars.SCREEN_HEIGHT - 100), (vars.SCREEN_WIDTH / 2 + 35, vars.SCREEN_HEIGHT - 100), 4)
        pygame.draw.line(screen, colors.white, (vars.SCREEN_WIDTH / 2 - 25, vars.SCREEN_HEIGHT / 2), (vars.SCREEN_WIDTH / 2 + 25, vars.SCREEN_HEIGHT / 2), 4)
        _prog = self.world.get_progress()
        p1_y = int(_prog[0] * (vars.SCREEN_HEIGHT - 210))
        p2_y = int(_prog[1] * (vars.SCREEN_HEIGHT - 210))

        pygame.draw.circle(screen, self.world.player_one.character.color, (int(vars.SCREEN_WIDTH / 2 - 15), p1_y + 105), 8, 6)
        pygame.draw.circle(screen, self.world.player_two.character.color, (int(vars.SCREEN_WIDTH / 2 + 15), p2_y + 105), 8, 6)

    def check_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f and self.world.race_started:
                    self.world.player_one.jump()
                if event.key == pygame.K_j and self.world.race_started:
                    self.world.player_two.jump()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    def run_game(self):
        clock = pygame.time.Clock()
        start_timer = 0
        end_timer = 0
        while True:
            self.draw_frame = not self.draw_frame
            real_fps = clock.tick(vars.fps)

            self.screen.fill(colors.black)

            # results = self.world.update(p1_left, p1_right, p2_left, p2_right)
            results = self.world.update(real_fps)

            self.world.draw(self.screen)
            self.draw_hud(self.screen)

            if debugcontrols.debug_mode:
                font = pygame.font.SysFont('Comic Sans MS', 25)
                label = font.render(str(real_fps), 1, (0, 255, 255))
                self.screen.blit(label, (vars.SCREEN_WIDTH / 2 - label.get_width() / 2, vars.SCREEN_HEIGHT - 75))

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
                    MusicLib.update_volume((int(vars.fps / 2) - end_timer) / int(vars.fps / 2))
                    fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                    fade_overlay.fill(colors.black)
                    fade_overlay.set_alpha((end_timer / int(vars.fps / 2)) * 255)
                    self.screen.blit(fade_overlay, (0, 0))
                    end_timer += 1

                    # TODO:  FANCY FINISH ANIMATION

            self.check_keys()
            pygame.display.update()
            pygame.event.get()
