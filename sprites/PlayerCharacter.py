import math
import os

import copy
import pygame


from objects.Characters import PoopTrail, Nort
from utils.sprite_utils import rot_center
from utils.spritesheet import spritesheet
from vars import show_velocity, draw_rects, SCREEN_HEIGHT, PLAYER_START_Y, IMAGES_PATH, radians_factor
import colors


class PlayerCharacter(pygame.sprite.Sprite):
    def __init__(self, init_x=0, init_y=700):
        super().__init__()
        self.angle = 0
        self.speed = 0
        self.x = init_x
        self.y = init_y
        self.eff_y = 0  # used for tracking effective y (because real y is static)
        self.x_speed = 0
        self.y_speed = 0
        self.z = 0
        self.z_speed = 0
        self.min_z = 0
        self.old_rect = None

        self.poops = pygame.sprite.Group()
        self.poop_score = 0

        self.distance_travelled = 0

        self.jump_state = 0  # 0 = not jumping, 1 = jumping

        self.character = None
        self.orig_sprite = None
        self.cur_sprite = None

        self.break_score = 0

        self.larm_images = None
        self.left_index = 0
        self.rarm_images = None
        self.right_index = 5
        self.tail_images = None
        self.tail_index = 0
        self.body_images = None
        self.body_index = 0
        self.head_images = None
        self.head_index = 0

        self.timer = 0
        self.timer_activated = False
        self.final_timer = float('inf')

        self.radius = 50

    def set_character(self, character):
        self.character = character
        self.orig_sprite = character.sprite
        if hasattr(character, 'head_path'):
            self.head_images = self.load_sprite_sheet(character.head_path, 60, 60, 9, 2)
        if hasattr(character, 'larm_path'):
            self.larm_images = self.load_sprite_sheet(character.larm_path, 60, 60, 9, 2)
        if hasattr(character, 'rarm_path'):
            self.rarm_images = self.load_sprite_sheet(character.rarm_path, 60, 60, 9, 2)
        if hasattr(character, 'tail_path'):
            self.tail_images = self.load_sprite_sheet(character.tail_path, 60, 60, 9, 4)
        if hasattr(character, 'body_path'):
            self.body_images = self.load_sprite_sheet(character.body_path, 60, 60, 1, 1)

        self.cur_sprite = self.orig_sprite
        self.radius = character.radius
        # self.rect = self.orig_sprite.get_rect()

    def jump(self):
        if self.jump_state == 0:
            self.jump_state = 1
            self.z_speed = .15
            self.x_speed -= 2 * math.sin(self.angle * radians_factor)
            self.y_speed -= 2 * math.cos(self.angle * radians_factor)

    def update_limbs(self, left, right):
        try:
            head_inc = 0
            if math.fabs(left[0]) + math.fabs(left[1]) > 20:
                head_inc = 1
                self.left_index = ((self.left_index + 1) % len(self.larm_images))
            if math.fabs(right[0]) + math.fabs(right[1]) > 20:
                head_inc = 1
                self.right_index = ((self.right_index + 1) % len(self.rarm_images))
            self.tail_index = ((self.tail_index + 1) % len(self.tail_images))
            self.head_index = ((self.head_index + head_inc) % len(self.head_images))
        except:
            pass

    def start_timer(self):
        if not self.timer_activated:
            self.timer_activated = True

    def check_victory(self, finish_line):
        if self.y < finish_line:
            self.final_timer = min(self.final_timer, self.timer)
            return True

    def generate_new_sprite(self):
        _im = pygame.Surface((self.character.width, self.character.height), pygame.SRCALPHA)
        try:
            _im.blit(self.larm_images[self.left_index], (0,0))
            _im.blit(self.rarm_images[self.right_index], (0,0))
            _im.blit(self.tail_images[self.tail_index], (0,0))
            _im.blit(self.body_images[self.body_index], (0,0))
            _im.blit(self.head_images[self.head_index], (0,0))
        except:
            _im = self.orig_sprite
        return _im

    def load_sprite_sheet(self, sheet_path, width, height, num, copies=3):
        _images = []
        sheet = spritesheet(os.path.join(IMAGES_PATH, 'characters', sheet_path))
        for x in range(0,width*num,width):
            for i in range(0, copies):
                _images.append(sheet.image_at((x, 0, width, height), (255, 0, 255)))
        return _images

    def update(self):
        self.old_rect = copy.deepcopy(self.rect)
        if self.timer_activated:
            self.timer += 1

        if self.y_speed != 0:
            self.angle = math.atan(self.x_speed/self.y_speed) / 0.0174533

        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y

        if self.distance_travelled > self.character.poop_factor:
            self.distance_travelled = 0
            self.spawn_poop()

    def update_z(self):
        self.z += self.z_speed
        self.z_speed -= 0.02
        if self.z < 0:
            self.z = 0
            self.z_speed = 0
            self.jump_state = 0
        if self.z < self.min_z:
            self.z = self.min_z
            self.z_speed = 0
            self.jump_state = 0

    def draw_as_player(self, screen, x_offset, y_offset):
        self.cur_sprite = self.generate_new_sprite()
        self.cur_sprite = pygame.transform.scale(self.cur_sprite, (int(self.character.width*(self.z/1.4 + 1)), int(self.character.height*(self.z/1.4 + 1))))
        _scale_dif = (self.z/1.4 + 1) * self.character.width - self.character.width
        _image = rot_center(self.cur_sprite, self.angle)
        _rect = _image.get_rect()
        _rect.x = self.x
        _rect.y = self.y
        screen.blit(_image, (_rect.x + x_offset - _scale_dif/2, SCREEN_HEIGHT - PLAYER_START_Y + y_offset + 10 - self.z * 100))
        if show_velocity:
            pygame.draw.line(screen, colors.debug_velocity_line, [self.x + self.character.width / 2, self.y + self.character.height / 2],
                             [self.x + (self.x_speed*15) + self.character.width / 2,
                              50 - (self.y_speed*15) + self.character.height / 2], 3)
        if draw_rects:
            _rect = self.rect
            _rect.x += x_offset
            _rect.y = y_offset + (SCREEN_HEIGHT - PLAYER_START_Y + 10)
            pygame.draw.rect(screen, self.character.color, _rect, 1)   #

    def draw_normal(self, screen, x_offset, y_offset):
        self.cur_sprite = self.generate_new_sprite()
        self.cur_sprite = pygame.transform.scale(self.cur_sprite, (int(self.character.width*(self.z/1.4 + 1)), int(self.character.height*(self.z/1.4 + 1))))
        _scale_dif = (self.z/1.4+1) * self.character.width - self.character.width
        _image = rot_center(self.cur_sprite, self.angle)
        _rect = _image.get_rect()
        _rect.x = self.x
        _rect.y = self.y
        screen.blit(_image, (_rect.x + x_offset - _scale_dif/2, _rect.y + y_offset + 10 - self.z * 100))
        if show_velocity:
            pygame.draw.line(screen, colors.debug_velocity_line, [self.x + self.character.width / 2, self.y + self.character.height / 2],
                             [self.x + (self.x_speed*15) + self.character.width / 2,
                              50 - (self.y_speed*15) + self.character.height / 2], 3)
        if draw_rects:
            _rect = self.rect
            _rect.x += x_offset
            _rect.y = _rect.y + y_offset
            pygame.draw.rect(screen, (255, 0, 0), _rect, 1)   #

    @property
    def rect(self):
        _rect = pygame.Rect(self.x+self.character.width/6, self.y+self.character.height/6, self.character.width/8*6,self.character.width/8*6)

        return _rect

    def spawn_poop(self):
        self.poops.add(self.character.get_a_poop(self.x, self.y, self.z, self.angle))
        self.poop_score += self.character.poop_factor
