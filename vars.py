import os

fps = 30
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PLAYER_START_Y = 200

radians_factor = 0.0174533  # Lol this is a constant not a var

selected_character_color_index = 0
IMAGES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'images',)