import pygame


#  https://www.pygame.org/wiki/RotateCenter
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
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