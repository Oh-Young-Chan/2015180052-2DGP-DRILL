from pico2d import *


def handle_events():
    global running
    global dir
    global vector
    global stall

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                stall = 0
                vector = 1
                dir += 1
            elif event.key == SDLK_LEFT:
                stall = 0
                vector = 0
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                stall = 2
                dir -= 1
            elif event.key == SDLK_LEFT:
                stall = 2
                dir += 1


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir = 0
vector = 1
stall = 2

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * vector + 100 * stall, 100, 100, x, 90)
    if(x>800 or x<0):
        x -= dir * 3
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    x += dir * 3
    delay(0.01)

close_canvas()

