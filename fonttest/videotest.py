import pgzrun

WIDTH = 600
HEIGHT = 400
TITLE = "Video-Test"


def update():
    pass

def draw():
    screen.fill((49, 197, 244))
    
def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        quit()

pgzrun.go()