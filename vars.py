import os

fps = 30
skip_intro = True
show_velocity = False
draw_rects = False
skip_countdown = True
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
radians_factor = 0.0174533  # Lol this is a constant not a var

selected_character_color_index = 0
IMAGES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images',)