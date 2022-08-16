import pgzrun

WIDTH = 512      # Tilesize * ROOMWIDTH
HEIGHT = 512     # Tilesize * ROOMHEIGHT
TITLE = "Pygame Zero Hack Stage 1"

TS = 32          # Tilesize
ROOMWIDTH = 16
ROOMHEIGHT = 16

WALL = 63
TREE = 62
DOOR_CLOSED = 60
DOOR_OPEN = 59

room01 = [[63, 63, 63, 63, 63, 63, 63, 63, 60, 63, 63, 63, 63, 63, 63, 63],
          [63, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, 62, 62, 63],
          [63, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, 62, 63],
          [63, -1, -1, 62, 62, 62, 62, 62, -1, -1, -1, -1, -1, 62, 62, 63],
          [63, -1, 62, 62, 62, 63, 62, 62, -1, -1, -1, -1, -1, -1, 62, 63],
          [63, -1, -1, -1, -1, 63, 62, -1, -1, -1, -1, -1, -1, -1, -1, 63],
          [63, -1, -1, -1, -1, 63, 62, -1, -1, -1, -1, -1, -1, -1, -1, 63],
          [63, -1, -1, 63, 63, 63, 62, -1, -1, -1, -1, -1, -1, -1, -1, 59],
          [63, -1, -1, -1, -1, 63, 62, -1, -1, -1, -1, -1, -1, -1, -1, 63],
          [63, -1, -1, -1, -1, 63, 62, -1, -1, -1, -1, -1, -1, -1, -1, 63],
          [63, -1, -1, 63, 63, 63, 62, -1, -1, -1, -1, -1, -1, -1, -1, 63],
          [63, -1, -1, -1, -1, 62, 62, -1, -1, -1, -1, -1, -1, -1, -1, 63],
          [63, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 63],
          [63, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 63],
          [63, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 63],
          [63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 60, 63]]

# Walls
walls = []
for y in range(ROOMHEIGHT):
    for x in range(ROOMWIDTH):
        if room01[y][x] == WALL:
            wall = Actor("wall")
            wall.topleft = x*TS, y*TS
            walls.append(wall)
        elif room01[y][x] == TREE:
            wall = Actor("tree")
            wall.topleft = x*TS, y*TS
            walls.append(wall)
        elif room01[y][x] == DOOR_CLOSED:
            wall = Actor("door_closed")
            wall.topleft = x*TS, y*TS
            walls.append(wall)
        elif room01[y][x] == DOOR_OPEN:
            wall = Actor("door_open")
            wall.topleft = x*TS, y*TS
            walls.append(wall)
        
link = Actor("link")
link.topleft = 10*TS, 7*TS

def on_key_down(key):
    if key == keys.UP and room01[int(link.top//TS) - 1][int(link.left//TS)] < 50:
        link.y -= TS
    elif key ==keys.DOWN and room01[int(link.top//TS) + 1][int(link.left//TS)] < 50:
        link.y += TS
    elif key == keys.LEFT and room01[int(link.top//TS)][int(link.left//TS) - 1] < 50:
        link.x -= TS
    elif key == keys.RIGHT and room01[int(link.top//TS)][int(link.left//TS) + 1] < 50:
        link.x += TS

def update():
    pass

def draw():
    screen.fill("#94b0c2")  # Light gray
    for wall in walls:
        wall.draw()
    link.draw()     

pgzrun.go()