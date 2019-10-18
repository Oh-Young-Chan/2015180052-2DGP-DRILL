from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy():
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

class Big_Ball():
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= random.randint(10, 30)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update_close(self):
        self.y = -50

class Small_Ball():
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= random.randint(10, 30)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update_close(self):
        self.y = -50

small_ball_count = random.randint(1, 10)
big_ball_count = 20 - small_ball_count

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

grass = Grass()
team = [Boy() for i in range(11)]
small_ball = [Small_Ball() for j in range(10)]
big_ball = [Big_Ball() for k in range(10)]
running = True

while running:
    handle_events()

    for boy in team:
        boy.update()

    for s_ball in small_ball:
        s_ball.update()

    for b_ball in big_ball:
        b_ball.update()

    for s_ball in small_ball:
        if s_ball.y < 30:
            s_ball.update_close()

    for b_ball in big_ball:
        if b_ball.y < 30:
            b_ball.update_close()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for s_ball in small_ball:
        s_ball.draw()
    for b_ball in big_ball:
        b_ball.draw()
    update_canvas()

    delay(0.1)

close_canvas()