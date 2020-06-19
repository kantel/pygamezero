import pygame
import pgzrun
from pvector import PVector
import math

WIDTH = 600
HEIGHT = 450
TITLE = "Rocket 1"
RADIUS = 32

class Rocket(Actor):
    
    def __init__(self, x, y, im):
        super().__init__(im, (x, y))
        self.pos = (x, y)
        self.im = im
        self.location = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.frame = 0
        self.angle = 90
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
        # self.angle = self.angle_to((mouse_x, mouse_y))
        self.angle = -self.velocity.heading()*(180/math.pi)
        
    def make_animation(self):
        if self.frame <= 5:
            self.image = "ship1"
        elif self.frame <= 10:
            self.image = "ship2"
        elif self.frame <= 15:
            self.image = "ship3"
        elif self.frame <= 20:
            self.image = "ship4"
        if self.frame >= 20:
            self.frame = 0
        self.frame += 1

    def check_edges(self):
        if (self.location.x > WIDTH - RADIUS):
            self.location.x = RADIUS
        elif (self.location.x < RADIUS):
            self.location.x = WIDTH - RADIUS
        if (self.location.y > HEIGHT - RADIUS):
            self.location.y = RADIUS
        elif (self.location.y < RADIUS):
            self.location.y = HEIGHT - RADIUS

rocket = Rocket(100, 200, "ship1")

def draw():
    screen.blit("background", (0, 0))
    rocket.draw()

def update():
    rocket.make_animation()
    rocket.update()
    rocket.check_edges()

pgzrun.go()