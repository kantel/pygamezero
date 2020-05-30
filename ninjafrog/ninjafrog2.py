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
jumped = False
allow_x = True
timer = []

platform_x = [20, 540, 100, 480, 180, 360, 280]
platform_y = [100, 100, 200, 200, 300, 300, 400]
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
    global ninja_x_velocity, ninja_y_velocity, jumping, jumped, gravity, allow_x, timer
    # Facing the Front
    if ninja_x_velocity == 0 and not jumped:
        ninja.image = "ninja_idle1"
    # Gravity
    if collide_check():
        gravity = 1
        ninja.y -= 1
        allow_x = True
        timer = []
    if not collide_check():
        ninja.y += gravity
        if gravity <= 20:
            gravity += 0.5
        timer.append(pygame.time.get_ticks())
        if len(timer) > 5 and not jumped:
            ninja.image = "ninja_jump"
            if len(timer) > 20:
                ninja.image = "ninja_fall"
    # Left and Right Movement
    if keyboard.left and allow_x:
        if (ninja.x > 16) and (ninja_x_velocity > -8):
            ninja_x_velocity -= 2
            ninja.image = "run_l1"
            if keyboard.left and jumped:
                ninja.image = "ninja_jump_l"
    if keyboard.right and allow_x:
        if (ninja.x < WIDTH - 16) and (ninja_x_velocity < 8):
            ninja_x_velocity += 2
            ninja.image = "run_r1"
            if keyboard.right and jumped:
                ninja.image = "ninja_jump_r"
    ninja.x += ninja_x_velocity
    # Velocity
    if ninja_x_velocity > 0:
        ninja_x_velocity -= 1
    if ninja_x_velocity < 0:
        ninja_x_velocity += 1
    if (ninja.x < 20) or (ninja.x > WIDTH - 20):
        ninja_x_velocity = 0
    # Jumping
    if keyboard.up and collide_check() and not jumped:
        jumping = True
        jumped = True
        clock.schedule_unique(jumped_recently, 0.4)
        ninja.image = "ninja_jump"
        ninja_y_velocity = 92
    if jumping and ninja_y_velocity > 25:
        ninja_y_velocity = ninja_y_velocity - ((100 - ninja_y_velocity)/2)
        ninja.y -= ninja_y_velocity/3
    else:
        ninja_y_velocity = 0
        jumping = False

def collide_check():
    collide = False
    for platrect in platrects:
        if ninja.colliderect(platrect):
            collide = True
    return(collide)

def jumped_recently():
    global jumped
    jumped = False

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
