import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
<<<<<<< HEAD
from ball import Ball
from ground import Ground
from zombie import Zombie
=======
from grass import Grass
from bird import Bird
>>>>>>> 9283d2998f0fc708cfeac1fcf87c0abc9e5f9bc8


name = "MainState"

boy = None
<<<<<<< HEAD
zombie = None


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


=======
>>>>>>> 9283d2998f0fc708cfeac1fcf87c0abc9e5f9bc8

def get_boy():
    return boy


def enter():
    global boy
    boy = Boy()
<<<<<<< HEAD
    game_world.add_object(boy, 1)
=======
    grass = Grass()
    bird = Bird()
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(bird, 1)
>>>>>>> 9283d2998f0fc708cfeac1fcf87c0abc9e5f9bc8

    global ball
    ball = Ball()
    game_world.add_object(ball, 1)

<<<<<<< HEAD
    global zombie
    zombie = Zombie()
    game_world.add_object(zombie, 1)

    ground = Ground()
    game_world.add_object(ground, 0)

=======
>>>>>>> 9283d2998f0fc708cfeac1fcf87c0abc9e5f9bc8
def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
<<<<<<< HEAD
=======
    # fill here
>>>>>>> 9283d2998f0fc708cfeac1fcf87c0abc9e5f9bc8


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






