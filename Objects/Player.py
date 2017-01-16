class Player:
    def __init__(self):
        self.angle = 0
        self.speed = 0
        self.x = 0
        # self.y = 0 #  Player wouldn't care about their y, because their y is static ( I THINK ? )

        self.jump_state = 0  # 0 = not jumping, 1 = jumping
