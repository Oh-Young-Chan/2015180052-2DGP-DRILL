import game_framework
from pico2d import *

import game_world

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 1.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 300
        self.width, self.height = 3 * PIXEL_PER_METER, 3 * PIXEL_PER_METER
        self.image = load_image('bird_animation.png')
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.frame_x = 0
        self.frame_y = 2

    def update(self):
        if self.x >= 1600:
            self.dir = 0
        elif self.x <= 0:
            self.dir = 1

        if self.dir == 1:
            self.x += self.velocity * game_framework.frame_time
        elif self.dir == 0:
            self.x -= self.velocity * game_framework.frame_time

        if self.frame_y != 0:
            self.frame_x = (self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            if int(self.frame_x) >= 4:
                self.frame_y = (self.frame_y-1) % 3
        else:
            self.frame_x = (self.frame_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            if int(self.frame_x) >= 3:
                self.frame_y = 3
                self.frame_y = (self.frame_y-1) % 3

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(182 * int(self.frame_x), 167 * self.frame_y, 182, 167, 0, '', self.x, self.y, self.width, self.height)
        else:
            self.image.clip_composite_draw(182 * int(self.frame_x), 165 * self.frame_y, 182, 165, 0, 'h', self.x, self.y, self.width, self.height)