from Objects.Theme import TempTheme


class Level:
    objects = None
    theme = None
    x = 0
    y = 0

    def __init__(self):
        self.theme = TempTheme()
        pass

    def update(self, addtl_x, addtl_y):
        self.x += addtl_x
        self.y += addtl_y

    def draw(self, screen):
        screen.blit(self.theme.background_sprite, (self.x, self.y))

        # draw background at x, y
        # iterate through my_objects and draw each (pass camera x and camera y so they don't draw if they don't need to)
