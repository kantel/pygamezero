import pgzrun
import pygame
import sys

WIDTH = 400
HEIGHT = 400
TITLE = "Dreieck(e)"

points = [(25, 0), (50, 25), (0, 25)]

def draw():
    screen.fill((149, 224, 245))
    screen.draw.polygon(points, (255, 0, 0))

def update():
    pass

def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()

pgzrun.go()