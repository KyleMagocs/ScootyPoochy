import pygame

import vars
from objects.Characters import PoopTrail
from sprites.PlayerCharacter import PlayerCharacter
import math

class World:
    def __init__(self, width, x_offset, y_offset, level):
        self.width = width
        self.x_offset = x_offset * width
        self.score = 0

        self.finish = False

        self.level = level
        self.level.x = self.x_offset
        self.level.y = 0 - self.level.height + y_offset
        self.level.update_objects(self.x_offset)

        self.player_character = PlayerCharacter(init_x=self.x_offset + self.width / 2, init_y=y_offset)  # TODO:  This math is bad
        self.player_group = pygame.sprite.Group(self.player_character)
        self.player_character.eff_y = 0 - self.level.height

        self.poops = pygame.sprite.Group()

        # self.y = 0

    def load_level(self):
        pass
        # TODO:  PARSE OUT LEVEL OBJECTS INTO LOCAL STORAGE

    def update(self, x_vel, y_vel):
        # HANDLE PLAYER X DIRECTION

        self.player_character.x_speed = (self.player_character.x_speed - x_vel) / self.level.theme.friction
        self.player_character.y_speed = (self.player_character.y_speed + y_vel) / self.level.theme.friction
        self.player_character.update()

        if self.check_victory():
            self.player_character.y -= 10
            self.finish = True
        else:
            # HANDLE WORLD Y DIRECTION
            if self.player_character.x < self.level.x + 60:
                self.player_character.x = self.level.x + 60
            if self.player_character.x > self.level.x + self.width - 60:
                self.player_character.x = self.level.x + self.width - 60
            if self.level.y + self.player_character.y_speed >= 0:
                # self.y = 0
                self.level.update(addtl_x=0, addtl_y=0)
                self.level.y = 0
                self.player_character.y -= self.player_character.y_speed
            else:
                # self.y += self.player_character.y_speed
                self.level.update(addtl_x=0, addtl_y=self.player_character.y_speed)
                for poop in self.poops:
                    poop.update(0, self.player_character.y_speed)
                    if poop.rect.y > vars.SCREEN_HEIGHT or poop.rect.y < 0:
                        self.poops.remove(poop)
            self.player_character.eff_y += self.player_character.y_speed
        self.player_character.distance_travelled += math.sqrt(x_vel*x_vel+y_vel*y_vel)
        if self.player_character.distance_travelled > 15:
            self.player_character.distance_travelled = 0
            self.spawn_poop()

        # check collisions
        col = pygame.sprite.groupcollide(self.level.objects, self.player_group, dokilla=False, dokillb=False)

        for sprite in col:
            if sprite.breakable and sprite.get_wrecked():
                self.score += sprite.score

        return False

    def check_victory(self):
        if self.player_character.eff_y > -180:
            return True

    def draw_win_text(self, screen):
        font = pygame.font.SysFont('Impact', 48)
        label = font.render('FINISH !', 1, (0, 0, 0))
        screen.blit(label, (self.x_offset + self.width / 4, vars.SCREEN_HEIGHT/2-10))
        label = font.render('FINISH !', 1, (255, 255, 255))
        screen.blit(label, (self.x_offset + self.width / 4 + 2, vars.SCREEN_HEIGHT / 2 - 10 + 2))

    def spawn_poop(self):
        new_poop = PoopTrail('poop_temp.png', self.player_character.x + self.player_character.character.width / 2,
                             self.player_character.y + self.player_character.character.width / 2)
        self.poops.add(new_poop)

    def draw(self, screen):
        self.level.draw(screen)
        self.poops.draw(screen)
        self.player_character.draw(screen)
        if self.finish:
            self.draw_win_text(screen)

        font = pygame.font.SysFont('Impact', 14)
        # label = font.render(str(self.player_character.distance_travelled), 1, (255, 255, 255))
        # screen.blit(label, (self.x_offset + self.width / 4 + 2, vars.SCREEN_HEIGHT / 2 - 10 + 2))