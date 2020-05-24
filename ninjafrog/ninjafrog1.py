import pgzrun
import pygame
import time
import sys

WIDTH = 640
HEIGHT = 480
TITLE = "🐸 Ninja Frog (1) 🐸"

blue = 130
blueforward = True

ground = Rect((0, HEIGHT - 16), (WIDTH, 16))

ninja = Actor("ninja_idle1")
ninja.pos = (WIDTH/2, HEIGHT - 32)

platform_x = [20, 180, 360, 540, 100, 280, 480, 20, 180, 360, 540, 280]
platform_y = [120, 120, 120, 120, 220, 220, 220, 320, 320, 320, 320, 400]
platforms = []
for i in range(len(platform_x)):
    platforms.append(Actor("platform", (platform_x[i] + 40, platform_y[i])))

def draw():
    screen.fill((85, 180, blue))
    screen.blit("background", (0, 0))
    screen.blit("ninjafrogground", (0, HEIGHT - 16))
    for platform in platforms:
        platform.draw()
        
    ninja.draw()

def update():
    background_colour_fade()

def background_colour_fade():
    global blue, blueforward
    if blue < 220 and blueforward:
        blue += 1
    else:
        blueforward = False
    if blue > 130 and not blueforward:
        blue -= 1
    else:
        blueforward = True

def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()

pgzrun.go()