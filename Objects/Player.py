from Objects import Characters
from controller_interface.dummy import Dummy
from controller_interface.trackball import Trackball

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
            self.control_one = Dummy()
            self.control_two = Dummy()
        elif control_type == TRACKBALL:
            self.control_one = Trackball(53769, 5506, self.player_id*2)
            self.control_two = Trackball(53769, 5506, (self.player_id*2) + 1)
        else:
            raise Exception('DIDNT GET AN INPUT?!?!?')

    def read_input(self):
        left = self.control_one.read()
        right = self.control_two.read()
        # TODO:  BUTTONS

        return {'left': left, 'right': right}

    def handle_input(self):
        control_input = self.read_input()
        left = control_input['left']
        right = control_input['right']

        addtl_y_vel = (left[1] / 10 + right[1] / 10) / 2 * Characters.ACCEL_COEF
        addtl_x_vel = ((left[0] / 10 - 10) + (right[0] / 10 + 10)) / 2 * Characters.ACCEL_COEF

        self.world.player_character.y_speed = (self.world.player_character.y_speed + addtl_y_vel) / self.world.level.theme.friction

        self.world.player_character.x_speed = (self.world.player_character.x_speed - addtl_x_vel) / self.world.level.theme.friction