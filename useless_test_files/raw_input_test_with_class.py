import time
import pygame
from math import pi
from controller_interface.trackball import Trackball

pygame.init()

screen=pygame.display.set_mode([640, 480])

trackball_one  = Trackball(53769, 5506, 0)
trackball_two = Trackball(53769, 5506, 1)

absolute_zero = [320, 240]

clock = pygame.time.Clock()

while True:
    clock.tick(30)

    distance_1 = trackball_one.read()
    distance_2 = trackball_two.read()

    screen.fill((255, 255, 255))

    distance = (distance_1[0] + distance_2[0], distance_1[1] + distance_2[1])

    pygame.draw.line(screen, (255, 0, 0), absolute_zero, [absolute_zero[0] + distance[0], absolute_zero[1] + distance[1]], 3)

    pygame.display.flip()