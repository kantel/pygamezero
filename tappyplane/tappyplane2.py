import pgzrun
import sys

WIDTH = 800
HEIGHT = 480
TITLE = "The Red Baron 2"
left = WIDTH/2
bottom = HEIGHT/2
bottomground = HEIGHT - 35

BACKGROUND = "background"
GROUND     = "groundgrass"

back0 = Actor(BACKGROUND, (left, bottom))
back1 = Actor(BACKGROUND, (WIDTH + left, bottom))
backs = [back0, back1]
ground0 = Actor(GROUND, (left, bottomground))
ground1 = Actor(GROUND, (WIDTH + left, bottomground))
grounds = [ground0, ground1]

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
        if self.y >= HEIGHT - 85:    # Flugzeug ist am Boden
            self.y = HEIGHT - 85
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
            
class Enemy(Actor):
    
    def __init__(self, image, x, y):
        Actor.__init__(self, image, (x, y))
        self.width = 44
        self.speed = -1.5
    
    def update(self):
        self.x += self.speed
        if self.x <= -self.width:
            self.x = WIDTH + self.width


plane = Plane("planered1", 100, HEIGHT//2)
enemy = Enemy("shippink", WIDTH - 100, HEIGHT//3)

def update():
    for back in backs:
        back.x -= 0.4
        if back.x <= -left:
            back.x = WIDTH + left
    for ground in grounds:
        ground.x -= 0.6
        if ground.x <= -left:
            ground.x = WIDTH + left
    enemy.update()
    plane.update()


def draw():
    for back in backs:
        back.draw()
    for ground in grounds:
        ground.draw()
    enemy.draw()
    plane.draw()

def on_key_down():
    ## Spielende mit ESC
    if keyboard.escape:
        sys.exit()
    ## Hoch mit Pfeiltaste oben
    if keyboard.up:
        plane.up()
        
pgzrun.go()
