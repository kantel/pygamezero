import pgzrun
from ball import Ball

WIDTH = 400
HEIGHT = 400
TITLE = "Bouncing Ball"


ball1 = Ball(200, 150, 1.0, 3.3, 16, "red")
ball2 = Ball(100, 100, 1.5, 5.0, 16, "blue")

def draw():
    screen.fill("yellow")
    ball1.show(screen)
    ball2.show(screen)

def update():
    ball1.move()
    ball2.move()

pgzrun.go()