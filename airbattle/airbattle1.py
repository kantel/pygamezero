import pgzrun, random

WIDTH = 400
HEIGHT = 600
TITLE = "Luftschlacht 1: Der Kampf um den Pazifik"

player = Actor("playerplane", (200, 520))
enemy1 = Actor("enemyplane1", (random.randint(40, 360), random.randint(-100, -50)))

def draw():
    screen.fill((0, 0, 128))
    enemy1.draw()
    player.draw()

def update():
    enemy1.y += 3
    if enemy1.y > 650: reset_enemy(enemy1)
    check_keys()

def check_keys():
    global player
    if keyboard.left:
        if player.x > 40: player.x -= 5
    if keyboard.right:
        if player.x < 360: player.x += 5

def reset_enemy(e):
    e.x = random.randint(40, 360)
    e.y = random.randint(-100, -50)

pgzrun.go()
