import pgzrun
import pygame
from pvector import PVector
import sys

WIDTH = 400
HEIGHT = 400
TITLE = "Simple Mover with Direction"
RADIUS = 16

class Mover(object):
    
    def __init__(self, x, y, r):
        self.location = PVector(x, y)
        self.radius = r
        self.dir = PVector(self.location.x + self.radius, self.location.y)
    
    def display(self):
        screen.draw.filled_circle((self.location.x, self.location.y), self.radius, (255, 0, 0))
        screen.draw.circle((self.location.x, self.location.y), self.radius, (0, 0, 0))
        screen.draw.line((self.location.x, self.location.y), (self.dir.x, self.dir.y), (0, 0, 0))
    
    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.dir = PVector(mouse_x, mouse_y)
        self.dir.mag()
        

mover = Mover(WIDTH/2, HEIGHT/2, RADIUS)

def draw():
    screen.fill((149, 224, 245))
    mover.display()

def update():
    mover.update()

def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()

pgzrun.go()
