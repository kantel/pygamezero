# Example 1.11: Motion 101 (Acceleration towards Mouse)
# aus »The Nature of Code« portiert nach Pygame Zero
# 14. Juni 2020 by Jörg Kantel
import pgzrun
import pygame
from pvector import PVector
from random import randint, choice
import sys

WIDTH = 400
HEIGHT = 400
TITLE = "Motion 101: Many Movers Acceleration Towards Mouse"
NUMBERMOVERS = 10

colorlist = [(239, 242, 63), (198, 102, 230), (151, 87, 165), (129, 122, 198), (98, 199, 119)]

class Mover(object):
    
    def __init__(self):
        self.location = PVector(randint(0, HEIGHT), randint(0, WIDTH))
        self.velocity = PVector(0, 0)
        self.topspeed = randint(6, 12)
        self.radius = randint(8, 24)
        self.color = choice(colorlist)
    
    def display(self):
        screen.draw.filled_circle((self.location.x, self.location.y), self.radius, self.color)
        screen.draw.circle((self.location.x, self.location.y), self.radius, (0, 0, 0))
    
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
    
    def check_edges(self):
        if (self.location.x > WIDTH - self.radius):
            self.location.x = WIDTH - self.radius
            self.velocity.x *= -1
        elif (self.location.x < self.radius):
            self.location.x = self.radius
            self.velocity.x *= -1
        if (self.location.y > HEIGHT - self.radius):
            self.location.y = HEIGHT - self.radius
            self.velocity.y *= -1
        elif (self.location.y < self.radius):
            self.location.y = self.radius
            self.velocity.y *= -1
    

movers = []
for _ in range(NUMBERMOVERS):
    movers.append(Mover())

def draw():
    screen.fill((149, 224, 245))
    for mover in movers:
        mover.display()

def update():
    for mover in movers:
        mover.update()
        mover.check_edges()
    
def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()

pgzrun.go()