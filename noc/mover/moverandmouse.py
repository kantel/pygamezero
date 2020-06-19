import pygame
import pgzrun
from pvector import PVector

WIDTH = 480
HEIGHT = 480
TITLE = "Mover 2"
RADIUS = 16

class Mover(Actor):
    
    def __init__(self, x, y, im, rotspeed):
        super().__init__(im, (x, y))
        self.pos = (x, y)
        self.im = im
        self.rotspeed = rotspeed
        self.angle = 90
        self.location = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.topspeed = 10
    
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

mover = Mover(100, 200, "ball1", 5)

def draw():
    screen.fill((100, 200, 0))
    mover.draw()

def update():
    mover.update()
    mover.bounce()


pgzrun.go()