from Objects.Theme import TempTheme


class Level:
    objects = None
    theme = None

    def __init__(self):
        self.theme = TempTheme()
        pass

    def draw(self, screen, camera_x, camera_y):
        screen.blit(self.theme.background_sprite, (camera_x, camera_y))

        # draw background at x, y
        # iterate through my_objects and draw each (pass camera x and camera y so they don't draw if they don't need to)
