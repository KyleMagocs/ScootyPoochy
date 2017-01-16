class Player:
    def __init__(self, init_x=0, init_y=700):
        self.angle = 0
        self.speed = 0
        self.x = init_x
        self.y = init_y

        self.jump_state = 0  # 0 = not jumping, 1 = jumping
        self.character = None

    def draw(self, screen):
        screen.blit(self.character.sprite, (self.x-self.character.width/2, self.y))
