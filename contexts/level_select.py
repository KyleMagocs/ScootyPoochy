import pygame
import math
from objects.Characters import Cooper
from objects.Theme import get_all_themes
from vars import fps, radians_factor
import vars

TOTAL_WAIT = 5


def generate_grid_coords():
    ret = []
    x = 250
    y = 200
    themes = get_all_themes()
    for i in range(0, len(themes)):
        if i % 3 == 0:
            x = 250
            y += 170

        ret.append((x, y,))
        x += 210
    return ret


def generate_circle_coords():
    ret = []
    themes = get_all_themes()
    inc = 360 / (len(themes) + 1)
    radius = 300
    for i in range(0, len(themes) + 1):
        x = math.cos(i * inc * radians_factor) * radius + vars.SCREEN_WIDTH / 2
        y = math.sin(i * inc * radians_factor) * radius + vars.SCREEN_HEIGHT / 2

        ret.append((x, y,))

    return ret


grid_coords = generate_grid_coords()


class SelectorTheme(pygame.sprite.Sprite):
    def __init__(self, theme):
        super().__init__()
        self.theme = theme()
        self.sprite = self.theme.load_thumb_sprite()
        self.x = 0
        self.y = 0

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.sprite, (self.x - self.sprite.get_width() / 2, self.y - self.sprite.get_height() / 2))


class LevelSelector:
    def __init__(self, color1, color2, player_id, player_name, width, height):
        self.color = (color1, color2)
        self.disp_color = 0
        self.color_counter = 0
        self.x = 0
        self.y = 0
        self.player_id = player_id
        self.player_name = player_name
        self.width = width
        self.height = height
        self.selected_index = 0

    def update_index(self, inc):
        self.selected_index = (self.selected_index + inc) % len(get_all_themes())

    def update(self):
        self.color_counter = (self.color_counter + 1) % 5  # swap every five frames
        if self.color_counter == 0:
            self.disp_color = (self.disp_color + 1) % 2

        self.x = grid_coords[self.selected_index][0]
        self.y = grid_coords[self.selected_index][1]

    def draw(self, screen):
        pygame.draw.rect(screen, self.color[self.disp_color],
                         (self.x + self.player_id - self.width / 2, self.y + self.player_id - self.height / 2,
                          self.width, self.height), 5)
        font = pygame.font.SysFont('Comic Sans MS', 15)
        label = font.render(self.player_name, 1, self.color[1])
        screen.blit(label,
                    (self.x + (self.width - 15) * self.player_id + 5 - self.width / 2, self.y - 20 - self.height / 2))


class LevelSelectContext:
    def __init__(self, screen):
        self.screen = screen
        self.thumbs = pygame.sprite.Group()
        self.p1 = LevelSelector((0, 255, 0), (50, 200, 50), 0, 'P1', 200, 150)
        self.p1.selected_index = 0
        self.p2 = LevelSelector((255, 0, 0), (200, 50, 50), 1, 'P2', 200, 150)
        self.p2.selected_index = 2
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.load_thumbs()

    def load_thumbs(self):
        x = 200
        y = 200
        themes = get_all_themes()
        for i in range(0, len(themes)):
            selector_theme = SelectorTheme(themes[i])
            selector_theme.x = grid_coords[i][0]
            selector_theme.y = grid_coords[i][1]

            self.thumbs.add(selector_theme)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.p1.update_index(-3)
                if event.key == pygame.K_s:
                    self.p1.update_index(3)
                if event.key == pygame.K_a:
                    self.p1.update_index(-1)
                if event.key == pygame.K_d:
                    self.p1.update_index(1)
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_UP:
                    self.p2.update_index(-3)
                if event.key == pygame.K_DOWN:
                    self.p2.update_index(3)
                if event.key == pygame.K_LEFT:
                    self.p2.update_index(-1)
                if event.key == pygame.K_RIGHT:
                    self.p2.update_index(1)
                if event.key == pygame.K_RETURN:
                    pass
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

    def main_loop(self):
        while True:
            self.check_events()
            self.timer += 1
            self.screen.fill((0, 0, 0))
            self.p1.update()
            self.p2.update()
            for theme_thumb in self.thumbs:  # todo: replace with real sprite group stuff
                theme_thumb.draw(self.screen)

            if self.timer > 60:
                return

            self.p1.draw(self.screen)
            self.p2.draw(self.screen)

            font = pygame.font.SysFont('Comic Sans MS', 15)
            label = font.render('CHOOSE A LEVEL ! {0:.2f}'.format(self.timer / fps), 1, (255, 255, 0))
            self.screen.blit(label, (450, 100))

            pygame.display.update()

            self.clock.tick(fps)
