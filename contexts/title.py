import os
import pygame

import colors
from utils.hollow import textHollow, textOutline
import vars
TOTAL_WAIT = 10


class TitleContext:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def display_loop(self):
        start_timer = 0
        end_timer = 0
        affirmative = False
        while True:
            self.clock.tick(vars.fps)
            self.screen.fill((0, 0, 0))

            self.timer += 1


            font = pygame.font.SysFont('Impact', 15)
            font2 = pygame.font.SysFont('Impact', 300)
            font3 = pygame.font.SysFont('Impact', 30)

            title_image = pygame.image.load_extended(os.path.join(vars.IMAGES_PATH, 'title.png'))
            title_image = pygame.transform.scale(title_image, (title_image.get_width()*2, title_image.get_height()*2))
            self.screen.blit(title_image, (vars.SCREEN_WIDTH/2-title_image.get_width()/2,0))
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
            self.screen.blit(sub_text, (vars.SCREEN_WIDTH/2-sub_text.get_width()/2, 480))

            sub_text = font.render('Title art by Dylan Gallagher ( @aintnofuntime )', 0, colors.white)
            self.screen.blit(sub_text, (vars.SCREEN_WIDTH / 2 - sub_text.get_width() / 2, 500))

            if (self.timer // 15) % 2 == 0 or (affirmative and self.timer % 2 == 0):
                if affirmative:
                    text = 'HERE WE GO!'
                else:
                    text = 'PRESS {BUTTON} TO BEGIN'
                sub_text = font3.render(text, 0, colors.white)
                self.screen.blit(sub_text, (vars.SCREEN_WIDTH / 2 - sub_text.get_width() / 2, 600))

            if start_timer < int(vars.fps / 2):
                fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                fade_overlay.fill(colors.black)
                fade_overlay.set_alpha(((int(vars.fps / 2) - start_timer) / int(vars.fps / 2)) * 255)
                self.screen.blit(fade_overlay, (0, 0))
                start_timer += 1

            if self.timer > TOTAL_WAIT * vars.fps and not affirmative:
                if end_timer > int(vars.fps / 2):
                    return 0
                else:
                    fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                    fade_overlay.fill(colors.black)
                    fade_overlay.set_alpha((end_timer / int(vars.fps / 2)) * 255)
                    self.screen.blit(fade_overlay, (0, 0))
                    end_timer += 1

            keystate = pygame.key.get_pressed()
            if keystate:
                if self.parse_keys(keystate):
                    affirmative = True

            if affirmative:
                if end_timer > int(vars.fps / 2):
                    return 1
                else:
                    fade_overlay = pygame.Surface((vars.SCREEN_WIDTH, vars.SCREEN_HEIGHT))
                    fade_overlay.fill(colors.black)
                    fade_overlay.set_alpha((end_timer / int(vars.fps / 2)) * 255)
                    self.screen.blit(fade_overlay, (0, 0))
                    end_timer += 1

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
