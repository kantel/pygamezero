# Example 1.10: Motion 101 (Acceleration towards Mouse)
# aus »The Nature of Code« portiert nach Pygame Zero
# 14. Juni 2020 by Jörg Kantel
import pgzrun
import pygame
from pvector import PVector
import sys

WIDTH = 400
HEIGHT = 400
TITLE = "Motion 101: Acceleration Towards Mouse"
RADIUS = 16

class Mover(object):
    
    def __init__(self, x, y, r):
        self.location = PVector(x, y)
        self.velocity = PVector(0, 0)
        self.radius = r
        self.topspeed = 10
    
    def display(self):
        screen.draw.filled_circle((self.location.x, self.location.y), self.radius, (255, 0, 0))
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
        if (self.location.x > WIDTH - RADIUS):
            self.location.x = WIDTH - RADIUS
            self.velocity.x *= -1
        elif (self.location.x < RADIUS):
            self.location.x = RADIUS
            self.velocity.x *= -1
        if (self.location.y > HEIGHT - RADIUS):
            self.location.y = HEIGHT - RADIUS
            self.velocity.y *= -1
        elif (self.location.y < RADIUS):
            self.location.y = RADIUS
            self.velocity.y *= -1
    

mover = Mover(200, 200, RADIUS)

def draw():
    screen.fill((149, 224, 245))
    mover.display()

def update():
    mover.update()
    mover.check_edges()
    
def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()

pgzrun.go()