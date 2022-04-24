import pgzrun

WIDTH = 640
HEIGHT = 240
TITLE = "Moving Circle"
RADIUS = 60
pos_x = WIDTH/2
pos_y = HEIGHT/2

def update():
    global pos_x
    pos_x += 1
    if pos_x >= WIDTH + RADIUS:
        pos_x = -RADIUS

def draw():
    screen.fill((49, 197, 244))
    screen.draw.filled_circle((pos_x, pos_y), RADIUS, (240, 80, 37))
    screen.draw.circle((pos_x, pos_y), RADIUS, (30, 30, 30))

def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        quit()

pgzrun.go()
