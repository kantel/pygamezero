import pgzrun
import os

x = 10
y = 10
# os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (x,y)
os.environ["SDL_VIDEO_WINDOW_POS"] = "10, 10"
TITLE = "Win pos"
WIDTH = 100
HEIGHT = 150


pgzrun.go()