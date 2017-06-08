from controller_interface.trackball import Trackball


class Player:
    def __init__(self, player_id):
        self.DUMMY_FLAG = False
        self.set_controls(2*player_id, 2*player_id+1)

    # noinspection PyAttributeOutsideInit\
    # TODO:  Maybe move this to the init?
    def set_controls(self, id_1, id_2):
        if id_1 > 1:
            self.DUMMY_FLAG = True
            return  # TODO:  SET UP MORE TRACKBALLS

        self.trackball_one = Trackball(53769, 5506, id_1)
        self.trackball_two = Trackball(53769, 5506, id_2)

    def read_input(self):
        if self.DUMMY_FLAG:
            return {'left': (0, 0,), 'right': (0, 0,)}
        tball_one = self.trackball_one.read()
        tball_two = self.trackball_two.read()
        # TODO:  BUTTONS ?

        return {'left': tball_one, 'right': tball_two}
