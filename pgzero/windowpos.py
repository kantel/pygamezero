import pgzrun
import os

x = 10
y = 10
os.environ["SDL_VIDEO_WINDOW_POS"] = "%d,%d" % (x,y)

TITLE = "Win pos"
WIDTH = 100
HEIGHT = 150


pgzrun.go()