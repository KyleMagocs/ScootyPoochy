import math
import os
import pygame


from objects.Characters import PoopTrail, Nort
from utils.sprite_utils import rot_center
from utils.spritesheet import spritesheet
from vars import show_velocity, draw_rects, SCREEN_HEIGHT, IMAGES_PATH
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
        self.z = 1
        self.z_speed = 0
        self.min_z = 1

        self.poops = pygame.sprite.Group()

        self.distance_travelled = 0

        self.jump_state = 0  # 0 = not jumping, 1 = jumping

        self.character = None
        self.orig_sprite = None
        self.cur_sprite = None
        #
        # self.rect = None

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

    def set_character(self, character):
        self.character = character
        self.orig_sprite = character.sprite
        if hasattr(character, 'head_path'):
            self.head_images = self.load_sprite_sheet(character.head_path, 60, 60, 9)
        if hasattr(character, 'larm_path'):
            self.larm_images = self.load_sprite_sheet(character.larm_path, 60, 60, 9)
        if hasattr(character, 'rarm_path'):
            self.rarm_images = self.load_sprite_sheet(character.rarm_path, 60, 60, 9)
        if hasattr(character, 'tail_path'):
            self.tail_images = self.load_sprite_sheet(character.tail_path, 60, 60, 9)
        if hasattr(character, 'body_path'):
            self.body_images = self.load_sprite_sheet(character.body_path, 60, 60, 1)

        self.cur_sprite = self.orig_sprite
        # self.rect = self.orig_sprite.get_rect()

    def jump(self):
        if self.jump_state == 0:
            self.jump_state = 1
            self.z_speed = .15

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


    def load_sprite_sheet(self, sheet_path, width, height, num):
        _images = []
        sheet = spritesheet(os.path.join(IMAGES_PATH, 'characters', sheet_path))
        for x in range(0,width*num,width):
            _images.append(sheet.image_at((x, 0, x+width, height), (255, 0, 255)))
            _images.append(sheet.image_at((x, 0, x+width, height), (255, 0, 255)))
            _images.append(sheet.image_at((x, 0, x+width, height), (255, 0, 255)))
        return _images

    def update(self):
        if self.y_speed != 0:
            self.angle = -1 * math.atan(self.x_speed/self.y_speed) / 0.0174533
        self.x += self.x_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.distance_travelled > self.character.poop_factor:
            self.distance_travelled = 0
            self.spawn_poop()

    def update_z(self):
        self.z += self.z_speed
        self.z_speed -= 0.02
        if self.z < 1:
            self.z = 1
            self.z_speed = 0
            self.jump_state = 0
        if self.z < self.min_z:
            self.z = self.min_z
            self.z_speed = 0
            self.jump_state = 0

    def draw(self, screen):
        self.cur_sprite = self.generate_new_sprite()
        self.cur_sprite = pygame.transform.scale(self.cur_sprite, (int(self.character.width*self.z), int(self.character.height*self.z)))
        _image = rot_center(self.cur_sprite, self.angle)
        _rect = _image.get_rect()
        _rect.x = self.x
        _rect.y = self.y
        screen.blit(_image, (_rect.x, _rect.y))
        if show_velocity:
            pygame.draw.line(screen, colors.debug_velocity_line, [self.x + self.character.width / 2, self.y + self.character.height / 2],
                             [self.x + (self.x_speed*15) + self.character.width / 2,
                              self.y - (self.y_speed*15) + self.character.height / 2], 3)
        if draw_rects:
            pygame.draw.rect(screen, self.character.color, self.rect, 1)   #

    @property
    def rect(self):
        _rect = pygame.Rect(self.x+self.character.width/6, self.y+self.character.height/6, self.character.width/8*6,self.character.width/8*6)

        return _rect

    def spawn_poop(self):
        self.poops.add(self.character.get_a_poop(self.x, self.y, self.z, self.angle))
