import game_framework
import pico2d

import main_state

<<<<<<< HEAD
pico2d.open_canvas(1280, 1024)
=======
pico2d.open_canvas(1600, 600, sync=True)
>>>>>>> 9283d2998f0fc708cfeac1fcf87c0abc9e5f9bc8
game_framework.run(main_state)
pico2d.close_canvas()