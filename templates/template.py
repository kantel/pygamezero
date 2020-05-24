import pgzrun
import sys

WIDTH = 640
HEIGHT = 480
TITLE = "🐍 Pygame Zero Template"

def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()

pgzrun.go()