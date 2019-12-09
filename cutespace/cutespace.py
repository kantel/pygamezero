import pgzrun
from random import randint

WIDTH = 640
HEIGHT = 480
TITLE = "Cute Space"

octopussy = Actor("octopussy", center = (100, HEIGHT/2))

rocketboys = []
for _ in range(3):
    rocketboys.append(Actor("rocketboy", center = (randint(700, 1400), randint(40, 440))))

for rocketboy in rocketboys:
    rocketboy.speed = randint(2, 4)

planets = []
for i in range(2):
    planets.append(Actor("planet"))
planets[0].pos = (800, 125)
planets[1].pos = (1025, 220)

score = 0
game_over = False
up = False

def reset(actor):
    actor.x = randint(700, 2100)
    actor.y = randint(40, 440)

def draw():
    if not game_over:
        screen.fill((0, 80, 125))
        for planet in planets:
            planet.draw()
        octopussy.draw()
        for rocketboy in rocketboys:
            rocketboy.draw()
        screen.draw.text("Punkte: " + str(score), (10, 10), color = "white")
    else:
        screen.fill((0, 80, 125))
        screen.draw.text("GAME OVER!", (WIDTH/2 - 50, HEIGHT/2), color = "white")

def update():
    global game_over, score
    if not game_over:
        if not up:
            octopussy.y += 1
        for rocketboy in rocketboys:
            if rocketboy.x > -rocketboy.width:
                rocketboy.x -= rocketboy.speed
            else:
                score += 1
                reset(rocketboy)
        for planet in planets:
            if planet.x > -planet.width:
                planet.x -= 0.25 
            else:
                reset(planet)
        if octopussy.top < 0 or octopussy.bottom > HEIGHT:
            game_over = True
        for rocketboy in rocketboys:
            if octopussy.collidepoint(rocketboy.x, rocketboy.y):
                game_over = True
    
def on_mouse_down():
    global up
    up = True
    octopussy.y -= 50

def on_mouse_up():
    global up
    up = False
    
pgzrun.go()
