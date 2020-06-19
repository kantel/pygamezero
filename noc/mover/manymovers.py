import pygame
import pgzrun
from pvector import PVector
from random import randint

WIDTH = 480
HEIGHT = 480
TITLE = "Mover 3 (Der Tanz der Bälle)"
RADIUS = 16
NUMBERMOVERS = 10

class Mover(Actor):
    
    def __init__(self, im):
        super().__init__(im)
        # self.pos = (x, y)
        self.im = im
        self.rotspeed = randint(-5, 5)
        self.angle = 90
        self.location = PVector(randint(0, HEIGHT), randint(0, WIDTH))
        self.velocity = PVector(0, 0)
        self.topspeed = randint(6, 12)
    
    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse = PVector(mouse_x, mouse_y)
        dir = mouse - self.location
        dir.normalize()
        dir.mult(0.5)
        self.acceleration = dir
        self.velocity.add(self.acceleration)
        self.velocity.limit(self.topspeed)
        self.location.add(self.velocity)
        self.pos = (self.location.x, self.location.y)
        self.angle += self.rotspeed
    
    def bounce(self):
        if (self.location.x > WIDTH - RADIUS) or (self.location.x < RADIUS):
            self.velocity.x *= -1
        if (self.location.y > HEIGHT - RADIUS) or (self.location.y < RADIUS):
            self.velocity.y *= -1

movers = []
for _ in range(NUMBERMOVERS):
    movers.append(Mover("ball1"))

def draw():
    screen.fill((100, 200, 0))
    for mover in movers:
        mover.draw()

def update():
    for mover in movers:
        mover.update()
        mover.bounce()

pgzrun.go()