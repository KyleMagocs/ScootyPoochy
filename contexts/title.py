import os
import pygame

import colors
from utils.hollow import textHollow, textOutline
from vars import fps, IMAGES_PATH, SCREEN_WIDTH

TOTAL_WAIT = 10


class TitleContext:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def display_loop(self):
        while True:
            self.clock.tick(fps)

            self.timer += 1
            if self.timer > TOTAL_WAIT * fps:
                return 0
            keystate = pygame.key.get_pressed()
            if keystate:
                if self.parse_keys(keystate):
                    return 1

            self.screen.fill((0, 0, 0))
            font = pygame.font.SysFont('Impact', 15)
            font2 = pygame.font.SysFont('Impact', 300)
            font3 = pygame.font.SysFont('Impact', 30)

            title_image = pygame.image.load_extended(os.path.join(IMAGES_PATH, 'title.png'))
            title_image = pygame.transform.scale(title_image, (title_image.get_width()*2, title_image.get_height()*2))
            self.screen.blit(title_image, (SCREEN_WIDTH/2-title_image.get_width()/2,0))
            # if (self.timer // 30) % 2 == 0:
            #     label = font.render('TITLE! {0:.2f}'.format(self.timer/fps), 1, (255, 0, 255))
            # else:
            #     label = font.render('TITLE! {0:.2f}'.format(self.timer/fps), 1, (255, 255, 255))
            # self.screen.blit(label, (200, 150))
            #
            # # label = font2.render('SUPER POOCH SCOOT !!'.format(self.timer / fps), 1, (255, 0, 255))
            #
            title_text = textOutline(font2, 'S', colors.blue, colors.white)
            self.screen.blit(title_text, (300, 90))
            sub_text = font.render('© 2017 Rotten Tuna Games', 0, colors.white)
            self.screen.blit(sub_text, (SCREEN_WIDTH/2-sub_text.get_width()/2, 480))

            sub_text = font.render('Title art by Dylan Gallagher ( @aintnofuntime )', 0, colors.white)
            self.screen.blit(sub_text, (SCREEN_WIDTH / 2 - sub_text.get_width() / 2, 500))

            if (self.timer // 15) % 2 == 0:
                sub_text = font3.render('PRESS {BUTTON} TO BEGIN', 0, colors.white)
                self.screen.blit(sub_text, (SCREEN_WIDTH / 2 - sub_text.get_width() / 2, 600))

            pygame.display.flip()


            pygame.event.get()

    def parse_keys(self, keys):
        if keys[pygame.K_RETURN]:
            pygame.event.clear()
            return True
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        else:
            return False
