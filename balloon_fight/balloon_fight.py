import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "Balloon Fight"

game_over = False
up = False

balloon = Actor("balloon")
balloon.pos = 400, 300

def on_key_up(key):
    global up
    if key == keys.SPACE:
        up = True
        balloon.y -= 50
        up = False
 
def update():
    if not game_over:
        if not up:
            balloon.y += 1

def draw():
    screen.blit("background", (0, 0))
    if not game_over:
        balloon.draw()

pgzrun.go()