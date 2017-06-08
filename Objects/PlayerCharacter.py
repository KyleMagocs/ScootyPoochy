import math

import pygame

from controller_interface.trackball import Trackball


class PlayerCharacter:
    def __init__(self, init_x=0, init_y=700):
        self.angle = 0
        self.speed = 0
        self.x = init_x
        self.y = init_y
        self.x_speed = 0
        self.y_speed = 0
        self.DUMMY_FLAG = False

        self.jump_state = 0  # 0 = not jumping, 1 = jumping
        self.character = None
        self.orig_sprite = None

    def set_character(self, character):
        self.character = character
        self.orig_sprite = character.sprite

    def update(self):
        if self.y_speed != 0:
            self.angle = -1 * math.atan(self.x_speed/self.y_speed) / 0.0174533
        # if self.angle > 30:
        #     self.angle = 30
        # if self.angle < -30:
        #     self.angle = -30
        # self.x -= math.sin(self.angle * 0.0174533) * self.speed  # 0.0174533 = radians convert
        self.x += self.x_speed

    def draw(self, screen):
        new_sprite = pygame.transform.rotate(self.orig_sprite, self.angle)
        screen.blit(new_sprite, (self.x - self.character.width / 2, self.y))

    # noinspection PyAttributeOutsideInit\
    # TODO:  Maybe move this to the init?
    def set_controls(self, id_1, id_2):
        if id_1 > 1:
            self.DUMMY_FLAG = True
            return  # TODO:  SET UP MORE TRACKBALLS

        self.trackball_one = Trackball(53769, 5506, id_1)
        self.trackball_two = Trackball(53769, 5506, id_2)

    def read_input(self):
        if self.DUMMY_FLAG:
            return {'left': (0, 0,), 'right': (0, 0,)}
        tball_one = self.trackball_one.read()
        tball_two = self.trackball_two.read()
        # TODO:  BUTTONS ?

        return {'left': tball_one, 'right': tball_two}
