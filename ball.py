import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1280-1), random.randint(0, 1024-1)

    def get_bb(self):
        # fill here
        return 0,0,0,0

    def draw(self):
        self.image.draw(self.x, self.y)
        # fill here for draw

    def update(self):
        pass

    #fill here for def stop


# fill here
class BigBall:
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 1280-1), random.randint(0, 1024-1)

    def get_bb(self):
        return 0, 0, 0, 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        pass

