# Simple Maze Game with Pygame Zero (v 1.2) , Python 3 
# Stage 1 (Initialisierung und Kollisionserkennung)
# Assets: DawnLike-Tileset (CC BY 4.0) by DawnBringer und DragonDePlatino
# (https://opengameart.org/content/dawnlike-16x16-universal-rogue-like-tileset-v181)
# Jörg Kantel 2022 (MIT-Lizenz)

import pgzrun

# WIDTH: 25 Tiles á 16 Pixel + je 20 Pixel Rand
WIDTH = 440
# HEIGHT: 25 Tiles á 16 Pixel + je 20 Pixel Rand
HEIGHT = 440
TITLE = "Mazegame Stage 1"

WALL  = 63
CHEST = 22

margin_x = 20
margin_y = 20
sz = 16  # Step-/Tile-Size

maze_map = [[63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,-1,-1,63,63,63,63,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,63],
            [63,-1,-1,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,-1,-1,63,63,-1,-1,63,63,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,-1,-1,63,63,-1,-1,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,63,63],
            [63,63,63,63,63,63,-1,-1,63,63,-1,-1,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,63,63],
            [63,63,63,63,63,63,-1,-1,63,63,-1,-1,63,63,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,63,63,63,63,63,-1,-1,63,63,-1,-1,-1,-1,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,-1,-1,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,22,-1,63,63,63,63,63],
            [63,-1,-1,63,63,63,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,63,63,63,63],
            [63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,-1,-1,-1,63,63,63,63,63,-1,22,63],
            [63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63,-1,-1,63],
            [63,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,63,63,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,63],
            [63,63,63,63,63,63,63,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,22,-1,-1,63,63,63,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,-1,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,63,63,63,63,63,63,63,63,63,63,63,63,-1,-1,63,63,63,63,63],
            [63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63,63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,63],
            [63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63]]

walls      = []
chests     = []
walls_pos  = []
chests_pos = []
for y in range(25):
    for x in range(25):
        if maze_map[y][x] == WALL:
            wall = Actor("wall16.png")
            wall.topleft = margin_x + x*sz, margin_y + y*sz
            walls.append(wall)
            walls_pos.append((margin_x + x*sz, margin_y + y*sz))
        if maze_map[y][x] == CHEST:
            chest = Actor("chest16.png")
            chest.topleft = margin_x + x*sz, margin_y + y*sz
            chests.append(chest)
            chests_pos.append((margin_x + x*sz, margin_y + y*sz))
                
rogue = Actor("rogue16")
rogue_x = 1
rogue_y = 1
rogue.topleft = margin_x + rogue_x*sz, margin_y + rogue_y*sz

def update():
    global dir, rogue_x, rogue_y
    if dir == "left":
        move_to_x = margin_x + (rogue_x*sz) - sz
        move_to_y = margin_y + rogue_y*sz
        dir = None
        if (move_to_x, move_to_y) not in walls_pos:   # Kollisionserkennung
            rogue.topleft = move_to_x, move_to_y
            rogue_x -= 1
    elif dir == "right":
        move_to_x = margin_x + (rogue_x*sz) + sz
        move_to_y = margin_y + rogue_y*sz
        dir = None
        if (move_to_x, move_to_y) not in walls_pos:   # Kollisionserkennung
            rogue.topleft = move_to_x, move_to_y
            rogue_x += 1
    elif dir == "up":
        move_to_x = margin_x + rogue_x*sz
        move_to_y = margin_y + (rogue_y*sz) - sz
        dir = None
        if (move_to_x, move_to_y) not in walls_pos:   # Kollisionserkennung
            rogue.topleft = move_to_x, move_to_y
            rogue_y -= 1
    elif dir == "down":
        move_to_x = margin_x + rogue_x*sz
        move_to_y = margin_y + (rogue_y*sz) + sz
        dir = None
        if (move_to_x, move_to_y) not in walls_pos:   # Kollisionserkennung
            rogue.topleft = move_to_x, move_to_y
            rogue_y += 1
    
def draw():
    screen.fill((90, 90, 90))
    
    for wall in walls:
        wall.draw()
    for chest in chests:
        chest.draw()
    rogue.draw()

def on_key_down(key):
    global dir
    if key == keys.LEFT:
        dir = "left"
    elif key == keys.RIGHT:
        dir = "right"
    elif key == keys.UP:
        dir = "up"
    elif key == keys.DOWN:
        dir = "down"
    if key == keys.ESCAPE:              # ESCAPE beendet das Spiel
        print("Bye, bye, Baby!")
        quit()
        
pgzrun.go()