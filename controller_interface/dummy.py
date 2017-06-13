import random

import pygame


class Dummy:
    button_one = None
    button_two = None
    button_three = None

    def __init__(self):
        self.toggle = True
        self.toggleCount = 30

    def set_buttons(self, one, two, three):
        self.button_one = one
        self.button_two = two
        self.button_three = three

    def read(self):
        try:
            if self.toggle:
                return random.randint(25, 50), random.randint(25, 50)
            else:
                return -1 * random.randint(25, 50), random.randint(25, 50)
        finally:
            self.toggleCount += 1
            if self.toggleCount >= 60:
                self.toggle = not self.toggle
                self.toggleCount = 0

    def get_buttons(self):
        # TODO:  Replace all of this with real buttons
        #         Y'know, like arcade buttons
        rtn = list()
        keystate = pygame.key.get_pressed()

        if keystate[self.button_one]:
            rtn.append('one')
        if keystate[self.button_two]:
            rtn.append('two')
        if keystate[self.button_three]:
            rtn.append('three')

        return rtn
