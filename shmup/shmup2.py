import pgzrun
import math
import sys

WIDTH = 680
HEIGHT = 400
TITLE = "Shmup 2"
TILEWIDTH = 640
NIRWANA = -2000, -2000
NO_ENEMYS = 9

class Layer(Actor):
    
    def __init__(self, image, xpos):
        Actor.__init__(self, image)
        self.left = xpos
        self.scroll_speed = 0.3

    def update(self):
        self.left -= self.scroll_speed
        if self.right < 0:
            self.left = TILEWIDTH

class Ship(Actor):
    
    def __init__(self, image, pos):
        Actor.__init__(self, image, pos)
        self.state = "ready"
        self.pos = pos
        self.frame = 0
        self.hitpoints = 0
        
    def make_animation(self):
        if self.frame <= 5:
            self.image = "ship1"
        elif self.frame <= 10:
            self.image = "ship2"
        elif self.frame <= 15:
            self.image = "ship3"
        elif self.frame <= 20:
            self.image = "ship4"
        if self.frame >= 20:
            self.frame = 0
        self.frame += 1
        
    def update(self):
        if keyboard.up:
            self.y -= 1
            self.state = "moving"
        elif keyboard.down:
            self.y += 1
            self.state = "moving"
        else:
            self.state = "ready"
        if self.hitpoints == NO_ENEMYS:
            print("You Won!")
            sys.exit()
    
    def check_edges(self):
        if self.y >= HEIGHT - 16:
            self.y = HEIGHT - 16
        elif self.y <= 16:
            self.y = 16

class Bullet(Actor):
    
    def __init__(self, image):
        Actor.__init__(self, image)
        self.state = "ready"
        self.pos = NIRWANA
        self.speed = 10

    def update(self):
        if keyboard.space:
            if self.state == "ready" and player.state == "ready":
                self.pos = player.pos
                self.state = "fire"
        if self.state == "fire":
            self.x += self.speed
        if self.x >= WIDTH:
            self.state = "ready"
            self.pos = NIRWANA

class Enemy(Actor):
    
    def __init__(self, image, pos):
        Actor.__init__(self, image)
        self.pos = pos
        self.start_pos = pos
        self.frame = 0
        self.speed = 1
    
    def update(self):
        self.y += self.speed
        if self.y >= HEIGHT - 20 or self.y <= 20:
            self.x -= 60
            self.speed *= -1

    def make_animation(self):
        if self.frame <= 5:
            self.image = "enemy1"
        elif self.frame <= 10:
            self.image = "enemy2"
        elif self.frame <= 15:
            self.image = "enemy3"
        elif self.frame <= 20:
            self.image = "enemy4"
        elif self.frame <= 25:
            self.image = "enemy5"
        elif self.frame <= 30:
            self.image = "enemy6"
        if self.frame >= 30:
            self.frame = 0
        self.frame += 1
    
    def hit(self, bullet):
        a = self.x - bullet.x
        b = self.y - bullet.y
        d = math.sqrt((a**2) + (b**2))
        if d < 20:
            bullet.state = "ready"
            bullet.pos = NIRWANA
            self.pos = NIRWANA
            player.hitpoints += 1
            print("Score " + str(player.hitpoints))
            
bg1 = Layer("bg", 0)
bg2 = Layer("bg", 1188)
layers = [bg1, bg2]

enemy_pos = []
for i in range(NO_ENEMYS):
    enemy_pos.append((WIDTH + 20, (i+1)*40))

enemys = []
for i in range(len(enemy_pos)):
    enemys.append(Enemy("enemy1", enemy_pos[i]))
    
player = Ship("ship1", (60, HEIGHT/2))
bullet = Bullet("laserred")

def draw():
    for layer in layers:
        layer.draw()
    for enemy in enemys:
        enemy.draw()
    bullet.draw()
    player.draw()

def update():
    for layer in layers:
        layer.update()
    for enemy in enemys:
        enemy.make_animation()
        enemy.update()
        enemy.hit(bullet)
    bullet.update() 
    player.make_animation()
    player.update()
    player.check_edges()

pgzrun.go()