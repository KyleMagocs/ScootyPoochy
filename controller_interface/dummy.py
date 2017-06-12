import random


class Dummy:
    def __init__(self):
        self.toggle = True
        self.toggleCount = 30

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