from objects.LevelObjects import Lamp

import pygame


pygame.init()

screen = pygame.display.set_mode((1440, 900))
clock = pygame.time.Clock()

lamp1 = Lamp((400,300))
lamp1.rect.x = 200
lamp1.rect.y = 400
lamp2 = Lamp((0,300))
lamp3 = Lamp((0,300))
lamp4 = Lamp((0,300))
lamp5 = Lamp((0,300))
lamp6 = Lamp((0,300))
lamp7 = Lamp((0,300))
lamp8 = Lamp((0,300))


lamp1.draw(screen)
pygame.display.flip()

lamp1.get_wrecked()

for i in range(0, 200):
    lamp1.update(lamp1.image.get_width(), 0)
    lamp1.draw(screen)
    pygame.display.flip()
    clock.tick(30)



input('foo')
print('foo')
print('foo')
print('foo')

# wtf this works fine ?????