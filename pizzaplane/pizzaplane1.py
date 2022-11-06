# Pizza Plane Stage 1 (Version Pygame Zero)
# Endless Scrolling Background
# Background Image: »PWL« (https://opengameart.org/content/seamless-desert-background-in-parts)
# Aeroplane: Tappy Plane, Kenney (https://www.kenney.nl/assets/tappy-plane)
import pgzrun
import sys

WIDTH = 720
HEIGHT = 480
TITLE = "Pizza Plane Stage 1 (Pygame Zero)"
LEFT = WIDTH/2
BOTTOM = HEIGHT/2

# Konstanten
BG_WIDTH = 1067             # Breite des Hintergrundbildes
BG_WIDTH2   = 533           # BGWIDTH//2 (abgerundet)
BACKGROUND = "desert"
PLANE_X = 70                # X-Position des Fliegers (bleibt fest)

# Actors
# Hintergrund
back0 = Actor(BACKGROUND, (LEFT, BOTTOM))
back1 = Actor(BACKGROUND, (BG_WIDTH + LEFT, BOTTOM))
backs = [back0, back1]
# Player
plane_image = []
for i in range(3):
    img = "planered_" + str(i)
    plane_image.append(img)
plane = Actor(plane_image[0], (PLANE_X, 200))   # Startposition
plane.r = 0
plane.updown = 3
plane.dir = "NONE"


def update():
    ## Background
    for back in backs:
        back.x -= 1          
        if back.x <= -BG_WIDTH/2:
            back.x = BG_WIDTH + BG_WIDTH2
    ## Flieger
    if plane.dir == "NONE":
        plane.y += 0
    elif plane.dir == "UP":
        if plane.y > 20:
            plane.y -= plane.updown
    elif plane.dir == "DOWN":
        if plane.y < HEIGHT - 20:
            plane.y += plane.updown
    plane.image = plane_image[int(plane.r)]
    plane.r += 0.2
    if plane.r >= 3.0:
        plane.r = 0
            
def draw():
    global r
    screen.fill("#94b0c2")  # Light gray
    for back in backs:
        back.draw()
    plane.draw()

def on_key_down():
    ## Steuerung des Fliegers
    if keyboard.up:
        plane.dir = "UP"
    if keyboard.down:
        plane.dir = "DOWN"
    ## Spielende mit ESC
    if keyboard.escape:
        print("Bye, Bye, Baby!")
        sys.exit()

def on_key_up():
    plane.dir = "NONE"

pgzrun.go()