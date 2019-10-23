from pico2d import *
import game_framework
import main_state

image = None

def enter():
    global image
    image = load_image('pause.png')


def pause():
    pass

def update():
    pass

def draw():
    global image
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.push_state(main_state)

def exit():
    pass