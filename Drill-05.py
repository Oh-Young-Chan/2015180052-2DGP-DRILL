from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)

Back_Ground = load_image('KPU_GROUND.png')
mouse = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

x, y = KPU_WIDTH//2, KPU_HEIGHT//2
frame = 0
running = True
hide_cursor()

while running:
    clear_canvas()
    Back_Ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    mouse.draw(x, y)
    character.clip_draw(frame*100, 100*1, 100, 100, 400, 90)
    update_canvas()
    frame = (frame+1)%8
    handle_events()

close_canvas()