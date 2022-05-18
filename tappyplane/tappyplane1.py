import pgzrun
import sys

WIDTH = 800
HEIGHT = 480
TITLE = "The Red Baron 1"
left = WIDTH/2
bottom = HEIGHT/2
bottomground = HEIGHT - 35

BACKGROUND = "background"
GROUND     = "groundgrass"

back0 = Actor(BACKGROUND, (left, bottom))
back1 = Actor(BACKGROUND, (WIDTH + left, bottom))
backs = [back0, back1]
ground0 = Actor(GROUND, (left, bottomground))
ground1 = Actor(GROUND, (WIDTH + left, bottomground))
grounds = [ground0, ground1]

plane = Actor("planered1", (100, HEIGHT//2))
plane.count = 0

def update():
    for back in backs:
        back.x -= 0.4
        if back.x <= -left:
            back.x = WIDTH + left
    for ground in grounds:
        ground.x -= 0.6
        if ground.x <= -left:
            ground.x = WIDTH + left
    plane.count += 1
    if plane.count > 9: plane.count = 0
    if plane.count < 3:
        plane.image = "planered1"
    elif plane.count < 6:
        plane.image = "planered2"
    else:
        plane.image = "planered3"

def draw():
    for back in backs:
        back.draw()
    for ground in grounds:
        ground.draw()
    plane.draw()

def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()
        
pgzrun.go()