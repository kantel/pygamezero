import pgzrun

WIDTH = 640
HEIGHT = 480
TITLE = "🐍 Graphische Primitive in Pygame Zero"

WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)

def draw():
    screen.fill(WHITE)
    screen.draw.line((0, 0), (640, 480), RED)
    screen.draw.circle((200, 100), 74, BLUE)
    screen.draw.filled_circle((400, 100), 74, BLUE)
    screen.draw.rect(Rect((150, 200), (100, 150)), GREEN)
    screen.draw.filled_rect(Rect((350, 200), (100, 150)), GREEN)
    screen.draw.line((0, 240), (640, 240), RED)

pgzrun.go()