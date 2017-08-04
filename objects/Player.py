from objects import Characters
from controller_interface.dummy import Dummy, SprintDummy, SinDummy
import math

from vars import SCREEN_HEIGHT

DUMMY = 1
TRACKBALL = 0
KEYBOARD = 2
GOOD_DUMMY = 3


class Player:
    def __init__(self, player_id, control_type=DUMMY):
        self.DUMMY_FLAG = False
        self.player_id = player_id
        self.world = None
        self.character = None
        self.control_one = None
        self.control_two = None
        self.set_controls(control_type)

    def set_controls(self, control_type):
        if control_type == DUMMY:
            self.control_one = SinDummy()
            self.control_two = SinDummy()
        elif control_type == TRACKBALL:
            try:
                from controller_interface.trackball import Trackball
                self.control_one = Trackball(53769, 5506, self.player_id*2)
                self.control_two = Trackball(53769, 5506, (self.player_id*2) + 1)
            except:
                self.control_one = SinDummy()  # TODO:  Fallback to keyboard?
                self.control_two = SinDummy()
        else:
            raise Exception('DIDNT GET AN INPUT?!?!?')

    def read_input(self):
        left = self.control_one.read()
        right = self.control_two.read()
        # TODO:  BUTTONS

        return left, right

    def get_progress(self):
        return math.fabs((self.world.player_character.eff_y) / self.world.level.height)

    def handle_input(self):
        left, right = self.read_input()

        return self.get_velocity(left, right)

    def get_velocity(self, left, right):
        addtl_y_vel = (left[1] / 10 + right[1] / 10) / 2 * Characters.ACCEL_COEF
        addtl_x_vel = ((left[0] / 10 - 10) + (right[0] / 10 + 10)) / 2 * Characters.ACCEL_COEF
        return addtl_x_vel, addtl_y_vel