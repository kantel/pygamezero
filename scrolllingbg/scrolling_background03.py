# Animate nach Paul Austin:
# https://github.com/PaulAustin/sb7-pgz/blob/master/actor/actor_background.py

import pgzrun
import sys

WIDTH = 800
HEIGHT = 400
TITLE = "Scrolling Background 3 (Animate)"
left = WIDTH/2
bottom = HEIGHT/2

BACKGROUND = "swampback"

back0 = Actor(BACKGROUND, (left, bottom))
back1 = Actor(BACKGROUND, (WIDTH + left, bottom))
backs = [back0, back1]

walker = Actor("walk1", (100, HEIGHT - 97))
walker.speed = 1
walker.count = 0

def update():
    for back in backs:
        back.x -= 0.5   # < 0.4 ruckelt das Bild
        if back.x <= -left:
            back.x = WIDTH + left
    walker.count += walker.speed
    if walker.count > 20: walker.count = 0
    if walker.count < 11:
        walker.image = "walk1"
    else:
        walker.image = "walk2"

def draw():
    for back in backs:
        back.draw()
    walker.draw()

def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()
        
pgzrun.go()
