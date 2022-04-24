import pgzrun
import pygame
from pvector import PVector
import math

WIDTH  = 600
HEIGHT = 450
TITLE = "Alone in the Dark"
RADIUS = 32

rocket = Actor("ship1")
rocket.location = PVector(100, 200)
rocket.velocity = PVector(0, 0)
rocket.frame = 0
rocket.angle = 90
rocket.topspeed = 5

def make_animation():
    if rocket.frame <= 5:
        rocket.image = "ship1"
    elif rocket.frame <= 10:
        rocket.image = "ship2"
    elif rocket.frame <= 15:
        rocket.image = "ship3"
    elif rocket.frame <= 20:
        rocket.image = "ship4"
    if rocket.frame >= 20:
        rocket.frame = 0
    rocket.frame += 1

def update_rocket():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse = PVector(mouse_x, mouse_y)
    dir = mouse - rocket.location
    dir.normalize()
    dir.mult(0.5)
    rocket.acceleration = dir
    rocket.velocity += (rocket.acceleration)
    rocket.velocity.limit(rocket.topspeed)
    rocket.location += (rocket.velocity)
    rocket.pos = (rocket.location.x, rocket.location.y)
    rocket.angle = -rocket.velocity.heading()*(180/math.pi)

def check_edges():
    if (rocket.location.x > WIDTH - RADIUS):
        rocket.location.x = RADIUS
    elif (rocket.location.x < RADIUS):
        rocket.location.x = WIDTH - RADIUS
    if (rocket.location.y > HEIGHT - RADIUS):
        rocket.location.y = RADIUS
    elif (rocket.location.y < RADIUS):
        rocket.location.y = HEIGHT - RADIUS

def update():
    make_animation()
    update_rocket()
    check_edges()
    
def draw():
    screen.blit("background", (0, 0))
    rocket.draw()
    
def on_key_down(key):
    # ESCAPE beendet das Spiel
    if key == keys.ESCAPE:              
        print("Bye, bye, Baby!")
        quit()

pgzrun.go()
