import random


class Dummy:
    def __init__(self):
        self.toggle = True
        self.toggleCount = 0



    def read(self):
        try:
            if self.toggle:
                return random.randint(100, 200), random.randint(100, 200)
            else:
                return random.randint(50, 100), random.randint(100, 200)
        finally:
            self.toggleCount += 1
            if self.toggleCount >= 60:
                self.toggle = not self.toggle
                self.toggleCount = 0