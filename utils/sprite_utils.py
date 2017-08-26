import pygame

#  https://www.pygame.org/wiki/RotateCenter
from objects import Characters
import math
import vars


def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def get_conform_deltas(obstacle, old, new):
    delta_x = 0
    delta_y = 0
    if old.right <= obstacle.left < new.right:
        delta_x = new.right - obstacle.left
    if old.left >= obstacle.right > new.left:
        delta_x = new.left - obstacle.right
    if old.bottom <= obstacle.top < new.bottom:
        delta_y = new.bottom - obstacle.top
    if old.top >= obstacle.bottom > new.top:
        delta_y = new.top - obstacle.bottom

    return delta_x, delta_y


def get_velocity(left, right):
    addtl_y_vel = (left[1] / 10 + right[1] / 10) / 2 * Characters.ACCEL_COEF
    addtl_x_vel = ((left[0] / 10 - 10) + (right[0] / 10 + 10)) / 2 * Characters.ACCEL_COEF
    return addtl_x_vel, addtl_y_vel


def angle_between_points(x1, y1, x2, y2):
    theta = math.atan(((y2 - y1)*-1) / (x2 - x1)) / vars.radians_factor + 90
    return theta
