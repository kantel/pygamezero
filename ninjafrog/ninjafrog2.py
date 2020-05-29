import pgzrun
import pygame
import time
import sys

WIDTH = 640
HEIGHT = 480
TITLE = "🐸 Ninja Frog (2) 🐸"

blue = 130
blueforward = True

ground = Rect((0, HEIGHT - 16), (WIDTH, 16))
platrects = [ground]

ninja = Actor("ninja_idle1")
ninja.pos = (320, 180)
ninja_x_velocity = 0
ninja_y_velocity = 0
gravity = 1
jumping = False

platform_x = [20, 180, 360, 540, 100, 480, 20, 180, 360, 540, 280]
platform_y = [120, 120, 120, 120, 220, 220, 320, 320, 320, 320, 400]
platforms = []
for i in range(len(platform_x)):
    platforms.append(Actor("platform", (platform_x[i] + 40, platform_y[i])))
for j in range(len(platform_x)):
    platrect = Rect((platform_x[j], platform_y[j] - 8), (80, 16))
    platrects.append(platrect)

def draw():
    screen.fill((85, 180, blue))
    screen.blit("background", (0, 0))
    screen.blit("ninjafrogground", (0, HEIGHT - 16))
    for platform in platforms:
        platform.draw()
    ninja.draw()

def update():
    background_colour_fade()
    ninja_move()

def ninja_move():
    global ninja_x_velocity, ninja_y_velocity, jumping, gravity
    # Gravity
    if collide_check():
        gravity = 1
        ninja.y -= 1
    if not collide_check():
        ninja.y += gravity
        if gravity <= 20:
            gravity += 0.5

def collide_check():
    collide = False
    for platrect in platrects:
        if ninja.colliderect(platrect):
            collide = True
    return(collide)

def background_colour_fade():
    global blue, blueforward
    if blue < 220 and blueforward:
        blue += 0.2
    else:
        blueforward = False
    if blue > 130 and not blueforward:
        blue -= 0.2
    else:
        blueforward = True

def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()

pgzrun.go()
