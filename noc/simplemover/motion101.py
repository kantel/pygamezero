# Example 1.7: Motion 101 (Velocity) aus »The Nature of Code« portiert nach Pygame Zero
# 13. Juni 2020 by Jörg Kantel
import pgzrun
from pvector import PVector
import random
import sys

WIDTH = 400
HEIGHT = 400
TITLE = "Motion 101: Velocity"
RADIUS = 16

class Mover(object):
    
    def __init__(self, x, y, r):
        self.location = PVector(x, y)
        self.velocity = PVector(random.uniform(-5, 5), random.uniform(-5, 5))
        self.radius = r
    
    def display(self):
        screen.draw.filled_circle((self.location.x, self.location.y), self.radius, (255, 0, 0))
        screen.draw.circle((self.location.x, self.location.y), self.radius, (0, 0, 0))
    
    def update(self):
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