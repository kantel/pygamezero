import pgzrun
from random import randint

WIDTH = 480
HEIGHT = 380
CENTER = WIDTH/2
TITLE = "🍏🍎 Apple Invaders 🍎🍏"
GROUNDWIDTH = 32
green_apple_speed = 2
red_apple_speed = 3
score = 0
game_over = False

## Player
gripe = Actor("gripe")
gripe.pos = midbottom=(CENTER, HEIGHT - 48)
gripe.speed = 5

def gripe_move():
    if keyboard.left and gripe.left > 0:
        gripe.x -= gripe.speed
    elif keyboard.right and gripe.right < WIDTH:
        gripe.x += gripe.speed

## Green Apples
green_apples = []
number_of_green_apples = 6
apple_frame = 0

def green_apples_spawn():
    green_apples.append(Actor("applegreen", pos = (randint(8, WIDTH -  8), 16)))

def green_apple_fall(apple):
    global apple_frame, score, game_over
    if apple.y < HEIGHT - 40:
        apple.y += green_apple_speed
    else:
        if apple_frame < 1:
            apple_frame += 0.025
        else:
            apple.pos = (randint(8, WIDTH - 8), 16)
            score -= 1
            if score < 0:
                score = 0
                game_over = True
            apple_frame = 0
            

for i in range(number_of_green_apples):
    # green_apples_spawn()
    clock.schedule(green_apples_spawn, i*2)

## Red Apples
red_apples = []
number_of_red_apples = 3

def red_apples_spawn():
    red_apples.append(Actor("applered", pos = (randint(8, WIDTH -  8), 16)))

def red_apple_fall(apple):
    if apple.y < HEIGHT:
        apple.y += red_apple_speed
    else:
        apple.pos = (randint(8, WIDTH -  8), 16)

for i in range(number_of_red_apples):
    # red_apples_spawn()
    clock.schedule(red_apples_spawn, i*5)

## Game Loop

def draw():
    screen.blit(images.background, (0, 0))
    gripe.draw()
    for apple in green_apples:
        apple.draw()
    for apple in red_apples:
        apple.draw()
    for i in range(15):
        screen.blit(images.ground, (i*GROUNDWIDTH, HEIGHT - 32))
        screen.blit(images.checker, (i*GROUNDWIDTH, HEIGHT - 16))
    screen.draw.text(f"Score: {score}", midtop = (CENTER, 10), fontsize = 36)
    screen.draw.text("Vermeide die Roten und schnappe die Grünen", midbottom = (CENTER, HEIGHT - 3), fontsize = 24)

def update():
    global score, game_over
    gripe_move()
    
    for apple in green_apples:
        green_apple_fall(apple)
        if gripe.colliderect(apple):
            apple.pos = (randint(8, WIDTH - 8), 16)
            score += 1
    for apple in red_apples:
        red_apple_fall(apple)
        if gripe.colliderect(apple):
            game_over = True

pgzrun.go()
