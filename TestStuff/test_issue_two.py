from Objects.Characters import get_all_characters

import pygame


pygame.init()


chars = get_all_characters()


screen = pygame.display.set_mode((1440, 900))

x = 100
y = 100

for char in chars:
    character = char()
    screen.blit(character.portrait, (x, y))
    x += 300
    y += 300

pygame.display.flip()

print('foo')
print('foo')
print('foo')

# wtf this works fine ?????