import pgzrun
from random import choice, randint
import sys

WIDTH = 640
HEIGHT = 480
TITLE = "Rogue 1"
TILESIZE = 32
HTILES = 20
VTILES = 15
MAXDIST = 5*TILESIZE

LEVEL_1 = [
    "####################",
    "#@ #               #",
    "#  #   ##   ####   #",
    "#       #   #      #",
    "#       #   ####   #",
    "#####   #   #      #",
    "#       #   ####   #",
    "#   #####          #",
    "#                 E#",
    "#   ################",
    "#                  #",
    "#########    ###   #",
    "#            #     #",
    "#            #     #",
    "####################"
]

hero_walking = True
enemy_walking = False

def legal_move(walls, actor):
    for wall in walls:
        if wall.colliderect(actor):
            return(True)

## Der Held
hero = Actor("hero")

def hero_move():
    global hero_walking
    old_hero_x = hero.x
    old_hero_y = hero.y
    if keyboard.left:
        if hero_walking:
            hero.x -= TILESIZE
            hero_walking = False
    if keyboard.right:
        if hero_walking:
            hero.x += TILESIZE
            hero_walking = False
    if keyboard.up:
        if hero_walking:
            hero.y -= TILESIZE
            hero_walking = False
    if keyboard.down:
        if hero_walking:
            hero.y += TILESIZE
            hero_walking = False
    
    ## Kollision mit Wall
    if legal_move(walls, hero):
        hero.x = old_hero_x
        hero.y = old_hero_y

def reset_hero(x, y):
    hero.topleft = (x*TILESIZE, y*TILESIZE)

## Der Feind
enemy = Actor("enemy")

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

    ## Kollision mit Wall
    if legal_move(walls, enemy):
        enemy.x = old_enemy_x
        enemy.y = old_enemy_y

## User Input
def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()

def on_key_up():
    global hero_walking, enemy_walking
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
            if sprite == "@":
                hero.topleft = (x*TILESIZE, y*TILESIZE)
            if sprite == "E":
                enemy.topleft = (x*TILESIZE, y*TILESIZE)

## Das Spiel
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