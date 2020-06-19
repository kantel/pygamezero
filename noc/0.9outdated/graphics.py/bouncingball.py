from pvector import PVector
import graphics as gfx
import sys

WIDTH = 400
HEIGHT = 400
RADIUS = 16
FPS = 15

location = PVector(100, 100)
velocity = PVector(1.0, 3.3)

win = gfx.GraphWin("Bouncing Ball", WIDTH, HEIGHT, autoflush = False)
win.setBackground("yellow")
c = gfx.Circle(gfx.Point(location.x, location.y), RADIUS)
c.setFill("red")
c.setOutline("black")
c.draw(win)

keep_going = True
i = 0
while keep_going:
    c.undraw()
    location.add(velocity)

    # check border
    if (location.x > WIDTH - RADIUS) or (location.x < RADIUS):
        velocity.x *= -1
    if (location.y > HEIGHT - RADIUS) or (location.y < RADIUS):
        velocity.y *= -1
    while i > 1200:
        keep_going = False
        win.close()
        sys.exit()
    i += 1
    c.move(velocity.x, velocity.y)
    c.draw(win)
    gfx.update()
