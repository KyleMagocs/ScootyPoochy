import pygame

from objects.LevelObjects import LevelObject


class MiscSprite(LevelObject):  # TODO:  Making this derived from LevelObject is dumb but uh, it works, so . . .
    def update(self, addtl_x, addtl_y):
        self.image = self.images[self.image_index]
        self.image_index += 1
        if self.image_index >= len(self.images):
            self.image_index = 0


class HowToJump(MiscSprite):
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


class HowToTrackball(MiscSprite):
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


class HowToBreakStuff(MiscSprite):
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


class PawButton(MiscSprite):
    sheet_path = 'pawbutton.png'
    width = 60
    height = 60

    def __init__(self, init_pos, mirror=False):
        super().__init__()
        self.images = self.load_sprite_sheet(self.sheet_path, self.width, self.height, 1, mirror)
        self.image = self.images[0]
        self.image_index = 0
        self.x = init_pos[0]
        self.y = init_pos[1]
