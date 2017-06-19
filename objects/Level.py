from objects.Theme import TempTheme


class Level:
    objects = None
    theme = None
    friction = 0
    x = 0
    y = 0
    height = 0
    width = 0

    def __init__(self):
        self.theme = None
        pass

    def update(self, addtl_x, addtl_y):
        self.x += addtl_x
        self.y += addtl_y

    def draw(self, screen):
        screen.blit(self.theme.background_sprite, (self.x, self.y))

        # draw background at x, y
        # iterate through my_objects and draw each (pass camera x and camera y so they don't draw if they don't need to)


class TempLevel(Level):
    def __init__(self):
        self.theme = TempTheme()
        self.height = self.theme.background_sprite.get_height()
        self.width = self.theme.background_sprite.get_width()