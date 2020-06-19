import pgzrun
from pvector import PVector
import random

WIDTH = 400
HEIGHT = 400
TITLE = "Mover 1"
RADIUS = 16

class Mover(Actor):
    
    def __init__(self, x, y, im, rotspeed):
        super().__init__(im, (x, y))
        self.pos = (x, y)
        self.im = im
        self.rotspeed = rotspeed
        self.angle = 90
        self.location = PVector(x, y)
        self.velocity = PVector(random.uniform(-2, 2), random.uniform(-2, 2))
        # self.acceleration = PVector(-0.001, 0.01)
        self.topspeed = 10
    
    def update(self):
        self.acceleration = PVector.random2D()
        self.acceleration.mult(0.5)
        # self.acceleration.mult(random.uniform(0, 2))
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.location.add(self.velocity)
        self.pos = (self.location.x, self.location.y)
        self.angle += self.rotspeed
    
    def check_edges(self):
        if (self.location.x > WIDTH - RADIUS):
            self.location.x = RADIUS
        elif (self.location.x < RADIUS):
            self.location.x = WIDTH - RADIUS
        if (self.location.y > HEIGHT - RADIUS):
            self.location.y = RADIUS
        elif (self.location.y < RADIUS):
            self.location.y = HEIGHT - RADIUS
    
    def bounce(self):
        if (self.location.x > WIDTH - RADIUS) or (self.location.x < RADIUS):
            self.velocity.x *= -1
        if (self.location.y > HEIGHT - RADIUS) or (self.location.y < RADIUS):
            self.velocity.y *= -1

mover = Mover(100, 200, "ball1", 5)

def draw():
    screen.fill((100, 200, 0))
    mover.draw()

def update():
    mover.update()
    # mover.check_edges()
    mover.bounce()

pgzrun.go()