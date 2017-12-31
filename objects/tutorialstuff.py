import pygame

from objects.LevelObjects import LevelObject


class TutorialSprite(LevelObject):  # TODO:  Making this derived from LevelObject is dumb but uh, it works, so . . .
    def update(self, addtl_x, addtl_y):
        self.image = self.images[self.image_index]
        self.image_index += 1
        if self.image_index >= len(self.images):
            self.image_index = 0


class HowToJump(TutorialSprite):
    sheet_path = 'howtojump.png'
    width = 600
    height = 300

    def __init__(self, init_pos, mirror=False):
        super().__init__()
        self.images = self.load_sprite_sheet(self.sheet_path, self.width, self.height, 10, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]


class HowToTrackball(TutorialSprite):
    sheet_path = 'howtotrackball.png'
    width = 725
    height = 280

    def __init__(self, init_pos, mirror=False):
        super().__init__()
        self.images = self.load_sprite_sheet(self.sheet_path, self.width, self.height, 10, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]


class HowToBreakStuff(TutorialSprite):
    sheet_path = 'howtobreakstuff.png'
    width = 260
    height = 350

    def __init__(self, init_pos, mirror=False):
        super().__init__()
        self.images = self.load_sprite_sheet(self.sheet_path, self.width, self.height, 13, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
