import pygame

import colors
from objects.miscsprites import HowToJump, HowToTrackball, HowToBreakStuff, PawButton
from utils.hollow import textOutline
from vars import fps, SCREEN_WIDTH, SCREEN_HEIGHT

TOTAL_WAIT = 20


class HowToPlayContext:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.timer = 0

    def display_loop(self):
        howtotrackball = HowToTrackball((SCREEN_WIDTH / 2 - HowToTrackball.width / 2, 95))
        howtojump = HowToJump((25, 360))
        breakstuff = HowToBreakStuff((950, 300))
        button = PawButton((SCREEN_WIDTH/2-PawButton.width, SCREEN_HEIGHT-60))
        while True:
            self.timer += 1
            if self.timer > TOTAL_WAIT * fps:
                return 0
            keystate = pygame.key.get_pressed()
            if keystate:
                if self.parse_keys(keystate):
                    return 1

            self.screen.fill((0, 0, 0))
            font = pygame.font.SysFont('IMPACT', 64)
            label = textOutline(font, 'HOW TO PLAY', colors.white, colors.black)
            self.screen.blit(label, (SCREEN_WIDTH / 2 - label.get_width() / 2, 0))

            font = pygame.font.SysFont('IMPACT', 32)

            pygame.draw.rect(self.screen, colors.black, (howtotrackball.x, howtotrackball.y, howtotrackball.width, howtotrackball.height), 0)
            howtotrackball.draw(self.screen, 0, 0)
            howtotrackball.update(0, 0)
            pygame.draw.rect(self.screen, colors.white, (howtotrackball.x, howtotrackball.y, howtotrackball.width, howtotrackball.height), 4)
            label = textOutline(font, 'SCOOT!', colors.white, colors.black)
            self.screen.blit(label, (howtotrackball.x + howtotrackball.width / 2 - 40, howtotrackball.y + 10))
            label = textOutline(font, 'or', colors.white, colors.black)
            self.screen.blit(label, (howtotrackball.x + howtotrackball.width / 2 - 20, howtotrackball.y + howtotrackball.height / 2))

            pygame.draw.rect(self.screen, colors.black, (howtojump.x, howtojump.y, howtojump.width, howtojump.height), 0)
            howtojump.draw(self.screen, 0, 0)
            howtojump.update(0, 0)
            pygame.draw.rect(self.screen, colors.white, (howtojump.x, howtojump.y, howtojump.width, howtojump.height), 4)
            label = textOutline(font, 'JUMP!', colors.white, colors.black)
            self.screen.blit(label, (howtojump.x + howtojump.width / 2 - 40, howtojump.y + 10))
            label = textOutline(font, 'or', colors.white, colors.black)
            self.screen.blit(label, (howtojump.x + howtojump.width / 2, howtojump.y + howtojump.height / 2))

            pygame.draw.rect(self.screen, colors.black, (breakstuff.x, breakstuff.y, breakstuff.width, breakstuff.height), 0)
            breakstuff.draw(self.screen, 0, 0)
            breakstuff.update(0, 0)
            pygame.draw.rect(self.screen, colors.white, (breakstuff.x, breakstuff.y, breakstuff.width, breakstuff.height), 4)
            label = textOutline(font, 'BREAK STUFF!', colors.white, colors.black)
            self.screen.blit(label, (breakstuff.x + breakstuff.width / 2 - label.get_width() / 2, breakstuff.y + 10))

            label = textOutline(font, '  PRESS               TO CONTINUE', colors.white, colors.black)
            self.screen.blit(label, (SCREEN_WIDTH/2 - label.get_width() / 2, SCREEN_HEIGHT - label.get_height() - 10))
            button.draw(self.screen, 0, 0)

            pygame.display.flip()
            self.clock.tick(fps)
            pygame.event.get()

    def parse_keys(self, keys):
        if len([x for x in keys if x == 1]):
            pygame.event.clear()
            return True
        else:
            return False
