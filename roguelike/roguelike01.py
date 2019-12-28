import pgzrun
from random import choice, randint

WIDTH = 640
HEIGHT = 480
TITLE = "Rogue 1"
TILESIZE = 32
HTILES = 20
VTILES = 15
MAXDIST = 4*TILESIZE

LEVEL_1 = [
    "####################",
    "#  #               #",
    "#  #######  #####  #",
    "#        #  #      #",
    "#        #  #####  #",
    "#######  #  #      #",
    "#        #  #####  #",
    "#  #######    #    #",
    "#             #   g#",
    "#  #################",
    "#                  #",
    "##########  #####  #",
    "#            #     #",
    "#            #     #",
    "####################"
]

hero_walking = True
enemy_walking = True

## Level

walls = []

def setup_maze(level):
    for y in range (len(level)):
        for x in range (len(level[y])):
            sprite = level[y][x]
            if sprite == "#":
                wall = Actor("wall")
                wall.topleft = (x*TILESIZE, y*TILESIZE)
                walls.append(wall)
                
def legal_move(walls, actor):
    hits = []
    for wall in walls:
        if wall.colliderect(actor):
            return(True)

## Der Held
hero = Actor("hero")
hero.topleft = (TILESIZE, TILESIZE)

def hero_move():
    global hero_walking
    old_hero_x = hero.x
    old_hero_y = hero.y
    if keyboard.left and hero.left > 0:
        if hero_walking:
            hero.x -= TILESIZE
            hero_walking = False
    if keyboard.right and hero.right < WIDTH:
        if hero_walking:
            hero.x += TILESIZE
            hero_walking = False
    if keyboard.up and hero.top > 0:
        if hero_walking:
            hero.y -= TILESIZE
            hero_walking = False
    if keyboard.down and hero.bottom < HEIGHT:
        if hero_walking:
            hero.y += TILESIZE
            hero_walking = False
    
    if legal_move(walls, hero):
        hero.x = old_hero_x
        hero.y = old_hero_y

def on_key_up():
    global hero_walking, enemy_walking
    hero_walking = True
    enemy_walking = True

def reset_hero(x, y):
    hero.topleft = (x*TILESIZE, y*TILESIZE)

## Der Feind
enemy = Actor("enemy")
enemy.topleft = (12*TILESIZE, TILESIZE)

def enemy_move():
    global enemy_walking
    old_enemy_x = enemy.x
    old_enemy_y = enemy.y
    if enemy.distance_to(hero) < MAXDIST:
        if enemy.x > hero.x and enemy_walking:
            enemy.x -= TILESIZE
            enemy_walking = False
        elif enemy.x < hero.x and enemy_walking:
            enemy.x += TILESIZE
            enemy_walking = False
        if enemy.y > hero.y and enemy_walking:
            enemy.y -= TILESIZE
            enemy_walking = False
        elif enemy.y < hero.y and enemy_walking:
            enemy.y += TILESIZE
            enemy_walking = False
    elif enemy_walking:
        if randint(0, 10) > 8:
            enemy.y = choice([enemy.y + TILESIZE, enemy.y - TILESIZE])
        else:
            enemy.x = choice([enemy.x + TILESIZE, enemy.x - TILESIZE])
        enemy_walking = False

    if legal_move(walls, enemy):
        enemy.x = old_enemy_x
        enemy.y = old_enemy_y


setup_maze(LEVEL_1)
    
def draw():
    screen.fill((128, 128, 130))
    for wall in walls:
        wall.draw()
    enemy.draw()
    hero.draw()

def update():
    hero_move()
    enemy_move()
    if enemy.colliderect(hero):
        reset_hero(1, 1)

pgzrun.go()