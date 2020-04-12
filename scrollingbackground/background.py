import pgzrun

WIDTH = 640
HEIGHT = 540
TITLE = "Scrolling Background"

scroll_speed = 1
scroll_position = 0

def draw():
    screen.blit("background", (scroll_position, 0))
    screen.blit("background", (scroll_position + 960, 0))

def update():
    global scroll_position
    scroll_position -= scroll_speed
    if (scroll_position <= -960):
        scroll_position = 0

pgzrun.go()
