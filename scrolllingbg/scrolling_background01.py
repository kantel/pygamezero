import pgzrun
import sys

WIDTH = 800
HEIGHT = 400
TITLE = "Scrolling Background 1"
left = WIDTH/2
bottom = HEIGHT/2

BACKGROUND = "desertback"

back0 = Actor(BACKGROUND, (left, bottom))
back1 = Actor(BACKGROUND, (WIDTH + left, bottom))
backs = [back0, back1]

def update():
    for back in backs:
        back.x -= 0.5   # < 0.4 ruckelt das Bild
        if back.x <= -left:
            back.x = WIDTH + left

def draw():
    for back in backs:
        back.draw()

def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()
        
pgzrun.go()
