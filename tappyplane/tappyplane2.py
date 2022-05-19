import pgzrun
import sys
from random import randint, choice

WIDTH = 800
HEIGHT = 480
TITLE = "The Red Baron 2"
left = WIDTH/2
bottom = HEIGHT/2
bottomground = HEIGHT - 35

BACKGROUND = "background"
GROUND     = "groundgrass"
no_enemies = 10
enemyships = ["shipbeige", "shipblue", "shipgreen", "shippink", "shipyellow"]

back0 = Actor(BACKGROUND, (left, bottom))
back1 = Actor(BACKGROUND, (WIDTH + left, bottom))
backs = [back0, back1]
ground0 = Actor(GROUND, (left, bottomground))
ground1 = Actor(GROUND, (WIDTH + left, bottomground))
grounds = [ground0, ground1]
groundlevel = HEIGHT - 85

class Plane(Actor):
    
    def __init__(self, image, x, y):
        Actor.__init__(self, image, (x, y))
        self.count = 0
        self.gravity = 0.1
        self.upforce = -15
        self.velocity = 0
        
    def update(self):
        self.velocity += self.gravity
        self.velocity *= 0.9         # Reibung/Luftwiderstand
        self.y += self.velocity
        if self.y >= groundlevel:    # Flugzeug ist am Boden
            self.y = groundlevel
            self.velocity = 0
        if self.y <= 20:             # Flugzeug ist am oberen Fensterrand
            self.y = 20
            self.velocity = 0
        self.show()
    
    def up(self):
        self.velocity += self.upforce
    
    def show(self):
        self.count += 1
        if self.count > 9: self.count = 0
        if self.count < 3:
            self.image = "planered1"
        elif self.count < 6:
            self.image = "planered2"
        else:
            self.image = "planered3"

class Bullet(Actor):
    
    def __init__(self):
        Actor.__init__(self, "laserred")
        self.x = plane.x
        self.y = plane.y
        self.speed = 25
        self.fire = False
    
    def update(self):
        if not self.fire:
            self.x = plane.x
            self.y = plane.y
        else:
            self.x += self.speed
            if self.left >= WIDTH:
                self.fire = False

class Enemy(Actor):
    
    def __init__(self, image, x, y):
        Actor.__init__(self, image, (x, y))
        self.width = 44
        self.speed = -1.5

    def reset(self):
        self.x = randint(WIDTH + 50, WIDTH + 500)
        self.y = randint(25, groundlevel)    
        self.image = choice(enemyships)

    def update(self):
        self.x += self.speed
        if self.x <= -self.width:
            self.reset()

plane = Plane("planered1", 100, HEIGHT//2)
bullet = Bullet()
enemies = []
for _ in range(no_enemies):
    enemyship = choice(enemyships)
    enemy = Enemy(enemyship, randint(WIDTH + 50, WIDTH + 750), randint(50, groundlevel))
    enemies.append(enemy)

def update():
    for back in backs:
        back.x -= 0.4
        if back.x <= -left:
            back.x = WIDTH + left
    for ground in grounds:
        ground.x -= 0.6
        if ground.x <= -left:
            ground.x = WIDTH + left
    bullet.update()
    for enemy in enemies:
        if enemy.colliderect(bullet) and bullet.fire:
            enemy.reset()
            bullet.fire = False
        enemy.update()
    plane.update()

def draw():
    for back in backs:
        back.draw()
    for ground in grounds:
        ground.draw()
    for enemy in enemies:
        enemy.draw()
    bullet.draw()
    plane.draw()


def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()
    ## Hoch mit Pfeiltaste nach oben
    if keyboard.up:
        plane.up()
    ## Feuern mit rechter Pfeiltaste
    if keyboard.right:
        bullet.fire = True
        
pgzrun.go()
