import os

from objects.Wall import Wall
import pygame
import vars
import time

pygame.init()

screen = pygame.display.set_mode((1440, 900))
clock = pygame.time.Clock()

_bg = pygame.image.load_extended(os.path.join(vars.IMAGES_PATH, 'level_assets', 'house_bg_temp.png'))
screen.blit(_bg, (0,0))

wall = Wall(0, 210, 200)
wall.draw_part_one(screen)
wall.draw_part_two(screen)

wall2 = Wall(0, 610, 400)
wall2.draw_part_one(screen)
wall2.draw_part_two(screen)


pygame.display.update()

time.sleep(1)

screen.blit(_bg, (0,0))

wall.update(0, 50)
wall.draw_part_one(screen)
wall.draw_part_two(screen)

wall2.update(0, 60)
wall2.draw_part_one(screen)
wall2.draw_part_two(screen)


pygame.display.update()


input('FOO')