<<<<<<< HEAD
import random
from pico2d import *
import game_world
import game_framework
=======
from pico2d import *
import game_world
>>>>>>> 9283d2998f0fc708cfeac1fcf87c0abc9e5f9bc8

class Ball:
    image = None

<<<<<<< HEAD
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 60, 0

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
# class BigBall
=======
    def __init__(self, x = 400, y = 300, velocity = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
>>>>>>> 9283d2998f0fc708cfeac1fcf87c0abc9e5f9bc8
