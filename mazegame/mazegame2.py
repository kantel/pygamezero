# Simple Maze Game with Pygame Zero (v 1.2) , Python 3 
# Stage 2 (Objektorientierung)
# Assets: DawnLike-Tileset (CC BY 4.0) by DawnBringer und DragonDePlatino
# (https://opengameart.org/content/dawnlike-16x16-universal-rogue-like-tileset-v181)
# Jörg Kantel 2022 (MIT-Lizenz)

import pgzrun

# WIDTH: 25 Tiles á 16 Pixel + je 20 Pixel Rand
WIDTH = 440
# HEIGHT: 25 Tiles á 16 Pixel + je 20 Pixel Rand
HEIGHT = 440
TITLE = "Mazegame Stage 2"

WALL  = 63
DOOR  = 62
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
            [63,63,63,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,62],
            [63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63]]

class Wall(Actor):
    
    def __init__(self, image):
        Actor.__init__(self, image)
        self.image = image
    
    def set_screen_pos(self, x, y):
        self.x = x
        self.y = y
        self.topleft = margin_x + self.x*sz, margin_y + self.y*sz

class Door(Actor):
    
    def __init__(self, image):
        Actor.__init__(self, image)
        self.image = image
        self.status = "closed"
    
    def set_screen_pos(self, x, y):
        self.x = x
        self.y = y
        self.topleft = margin_x + self.x*sz, margin_y + self.y*sz
    
class Chest (Actor):
    
    def __init__(self, image):
        Actor.__init__(self, image)
        self.image = image
        self.score = 100
    
    def set_screen_pos(self, x, y):
        self.x = x
        self.y = y
        self.topleft = margin_x + self.x*sz, margin_y + self.y*sz
    
class Rogue(Actor):
    
    def __init__(self, image):
        Actor.__init__(self, image)
        self.image = image
        self.xpos = 1   # x-Position im Grid
        self.ypos = 1   # y-Position im Grid
        # Rogue ohne Animation auf Startposition setzen
        self.topleft = margin_x + self.xpos*sz, margin_y + self.ypos*sz
        self.dir = None
        self.score = 0

    def set_screen_pos(self):
        x, y = margin_x + self.xpos*sz + 0.5*sz, margin_y + self.ypos*sz + 0.5*sz
        animate(self, duration = .2, pos = (x, y))

        
    def walk(self):
        if self.dir == "left":
            move_to_x = self.xpos - 1
            move_to_y = self.ypos
            self.dir = None
            # Kollisionserkennung
            if (move_to_x, move_to_y) not in walls_pos:
                self.xpos -= 1
                self.set_screen_pos()
        elif self.dir == "right":
            move_to_x = self.xpos + 1
            move_to_y = self.ypos
            self.dir = None
            # Kollisionserkennung
            if (move_to_x, move_to_y) not in walls_pos:
                self.xpos += 1
                self.set_screen_pos()
        elif self.dir == "up":
            move_to_x = self.xpos
            move_to_y = self.ypos - 1
            self.dir = None
            # Kollisionserkennung
            if (move_to_x, move_to_y) not in walls_pos:
                self.ypos -= 1
                self.set_screen_pos()
        elif self.dir == "down":
            move_to_x = self.xpos
            move_to_y = self.ypos + 1
            self.dir = None
            # Kollisionserkennung
            if (move_to_x, move_to_y) not in walls_pos:
                self.ypos += 1
                self.set_screen_pos()        
    
rogue = Rogue("rogue16")

walls      = []
chests     = []
doors      = []
walls_pos  = []
chests_pos = []

def init_game():
    for y in range(25):
        for x in range(25):
            if maze_map[y][x] == WALL:
                wall = Wall("wall16")
                wall.set_screen_pos(x, y)
                walls.append(wall)
                walls_pos.append((x, y))
            if maze_map[y][x] == DOOR:
                door = Door("door16")
                door.set_screen_pos(x, y)
                doors.append(door)
                walls_pos.append((x, y))
                
            if maze_map[y][x] == CHEST:
                chest = Chest("chest16")
                chest.set_screen_pos(x, y)
                chests.append(chest)
                chests_pos.append((x, y))

def update():
    rogue.walk()
    for chest in chests:
        if rogue.colliderect(chest):
            rogue.score += chest.score
            chests.remove(chest)
            print(rogue.score)
    
def draw():
    screen.fill((90, 90, 90))    
    for wall in walls:
        wall.draw()
    for door in doors:
        door.draw()
    for chest in chests:
        chest.draw()
    rogue.draw()

def on_key_down(key):
    if key == keys.LEFT:
        rogue.dir = "left"
    elif key == keys.RIGHT:
        rogue.dir = "right"
    elif key == keys.UP:
        rogue.dir = "up"
    elif key == keys.DOWN:
        rogue.dir = "down"
    if key == keys.ESCAPE:              # ESCAPE beendet das Spiel
        print("Bye, bye, Baby!")
        quit()

init_game()
pgzrun.go()