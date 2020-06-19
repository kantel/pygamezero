import pgzrun
from pvector import PVector

WIDTH = 400
HEIGHT = 400
TITLE = "Bouncing Ball 2"
RADIUS = 16

ball1 = Actor("ball1")
ball1.pos = (100, 200)
ball1.position = PVector(100, 200)
ball1.velocity = PVector(1.3, 5.0)

ball2 = Actor("ball2")
ball2.pos = (250, 100)
ball2.position = PVector(250, 100)
ball2.velocity = PVector(1.7, 3.5)

def move(ball, rotspeed):
    ball.position.add(ball.velocity)
    ball.pos = (ball.position.x, ball.position.y)
    ball.angle += rotspeed

    if (ball.position.x > WIDTH - RADIUS) or (ball.position.x < RADIUS):
        ball.velocity.x *= -1
    if (ball.position.y > HEIGHT - RADIUS) or (ball.position.y < RADIUS):
        ball.velocity.y *= -1

def draw():
    screen.fill((100, 200, 0))
    ball1.draw()
    ball2.draw()

def update():
    move(ball1, 3)
    move(ball2, -2)

pgzrun.go()