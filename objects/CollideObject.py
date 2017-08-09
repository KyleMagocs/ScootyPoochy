import pygame
import vars

class collide_object(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.height = 100
        self.image = image
        self.x = x
        self.y = y
        self.old_rect = self.get_rect()

    def draw(self, screen):
        self.old_rect = self.get_rect()
        screen.blit(self.image, (self.x, self.y))
        if vars.draw_rects:
            pygame.draw.rect(screen, (0, 255, 255), self.rect, 1)

    def update(self, addtl_x, addtl_y):
        self.old_rect = self.get_rect()
        self.x += addtl_x
        self.y += addtl_y

    def get_rect(self):
        raise Exception('need to implement get_rect on the subclass')

    @property
    def rect(self):
        return self.get_rect()