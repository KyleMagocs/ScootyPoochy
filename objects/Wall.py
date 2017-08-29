import os

import pygame

import vars
from objects.CollideObject import collide_object
import colors
from utils.sprite_utils import image_to_surface


class Wall(pygame.sprite.Sprite):
    side_image = 'objects/house_wall_side.png'
    top_image = 'objects/house_wall_top.png'
    bottom_image = 'objects/house_wall_bottom.png'

    def __init__(self, init_x, init_y, door_x):
        super().__init__()
        self.x = init_x
        self.y = init_y
        self.door_x = door_x

        left_side_image = pygame.image.load_extended(os.path.join(vars.IMAGES_PATH, self.side_image))
        self.left_side = image_to_surface(left_side_image)

        right_side_image = pygame.transform.flip(left_side_image, True, False)
        self.right_side = image_to_surface(right_side_image)

        top_image = pygame.image.load_extended(os.path.join(vars.IMAGES_PATH, self.top_image))
        self.top = image_to_surface(top_image)

        _wall_base = pygame.image.load_extended(os.path.join(vars.IMAGES_PATH, self.bottom_image))
        _wall_flipped = pygame.transform.flip(_wall_base, True, False)

        _left_flipped = _wall_flipped.subsurface((0, 0, self.top.get_width() - door_x, _wall_flipped.get_height()))
        _left_wall = pygame.transform.flip(_left_flipped, True, False)
        _left_wall.set_colorkey(colors.TRANSPARENT, pygame.RLEACCEL)
        self.left_wall = left_wall(_left_wall, init_x + self.left_side.get_width(), init_y + self.top.get_height())

        _right_wall = _wall_flipped.subsurface((0, 0, door_x, _wall_flipped.get_height()))
        _right_wall.set_colorkey(colors.TRANSPARENT, pygame.RLEACCEL)
        self.right_wall = right_wall(_right_wall, init_x + self.left_side.get_width() + self.left_wall.image_surface.get_width(), init_y + self.top.get_height())

        self.rect = self.top.get_rect()

    def draw(self, screen, x_offset, y_offset):
        self.draw_part_one(screen, x_offset, y_offset)
        self.draw_part_two(screen, x_offset, y_offset)

    def draw_part_one(self, screen, x_offset, y_offset):
        screen.blit(self.left_side, (self.x + x_offset, self.y + y_offset))
        self.left_wall.draw(screen, x_offset, y_offset)
        self.right_wall.draw(screen, x_offset, y_offset)
        screen.blit(self.right_side, (self.x + x_offset + self.left_side.get_width() + self.left_wall.image_surface.get_width() + self.right_wall.image_surface.get_width(), self.y + y_offset))

    def draw_part_two(self, screen, x_offset, y_offset):
        screen.blit(self.top, (self.x + x_offset + self.left_side.get_width(), self.y + y_offset))

    def update(self, addtl_x, addtl_y):
        pass
        # self.x += addtl_x
        # self.y += addtl_y
        # self.left_wall.update(addtl_x, addtl_y)
        # self.right_wall.update(addtl_x, addtl_y)

    def get_collide_walls(self):
        return [self.left_wall, self.right_wall]


class left_wall(collide_object):
    def get_collide_rect(self):
        _rect = self.image_surface.subsurface((0, 0, self.image_surface.get_width()-47, self.image_surface.get_height()/1.2)).get_rect()
        _rect.x += self.x
        _rect.y += self.y
        return _rect


class right_wall(collide_object):
    def get_collide_rect(self):
        _new = self.image_surface.subsurface((0, 0, self.image_surface.get_width() - 42, self.image_surface.get_height()/1.2))
        _reflip = pygame.transform.flip(_new, True, False)
        _rect = _reflip.get_rect()
        _rect.x += self.x + 49
        _rect.y += self.y
        return _rect

class SideWall(collide_object):
    def __init__(self, x, width, height):
        self.width = width  # Todo: hack
        super().__init__(None, x, 0)
        self.x = x
        self.y = 0
        self.height = height

    def update(self, *args):
        pass

    def get_collide_walls(self):
        return self

    def draw_part_one(self, *args):
        pass

    def draw_part_two(self, screen, x_offset, *args):
        if vars.draw_rects:
            _rect = self.rect
            _rect.x += x_offset
            pygame.draw.rect(screen, (0, 255, 255), _rect, 1)

    def get_collide_rect(self):
        return pygame.Rect(self.x, 0, self.width, self.height)

class BathroomWall(Wall):
    side_image = 'objects/bathroom_wall_side.png'
    top_image = 'objects/bathroom_wall_top.png'
    bottom_image = 'objects/bathroom_wall_bottom.png'