# Pizza Plane Stage 2 (Version Pygame Zero)
# Endless Scrolling Background
# Background Image: »PWL« (https://opengameart.org/content/seamless-desert-background-in-parts)
# Aeroplane: Tappy Plane, Kenney (https://www.kenney.nl/assets/tappy-plane)
# Pizzas: Twitter Twemoji (https://twemoji.twitter.com/)
import pgzrun
import sys
from random import randint

WIDTH = 720
HEIGHT = 480
TITLE = "Pizza Plane Stage 2 (mit Missile und pösen Pizzas)"

# Konstanten
BG_LEFT = WIDTH/2
BG_BOTTOM = HEIGHT/2
BG_WIDTH = 1067             # Breite des Hintergrundbildes
BG_WIDTH2   = 533           # BG_WIDTH//2 (abgerundet)
BACKGROUND = "desert"
NO_ENEMIES = 10
PLANE_X = 70                # X-Position des Fliegers (bleibt fest)

# Klassendefinitionen

class Plane(Actor):
    
    def __init__(self):
        Actor.__init__(self, "planered_0", (PLANE_X, 200))
        self.images = []
        for i in range(3):
            img = "planered_" + str(i)
            self.images.append(img)
        self.r = 0
        self.updown = 3
        self.dir = "NONE"
        
    def update(self):
        if self.dir == "NONE":
            self.y += 0
        elif self.dir == "UP":
            if self.y > 20:
                self.y -= self.updown
        elif self.dir == "DOWN":
            if self.y < HEIGHT - 20:
                self.y += self.updown
        self.image = self.images[int(self.r)]
        self.r += 0.2
        if self.r >= 3.0:
            self.r = 0

class Missile(Actor):
    
    def __init__(self):
        Actor.__init__(self, "laserred", (plane.x, plane.y))
        self.speed = 25
        self.fire = False
    
    def update(self):
        if not self.fire:
            self.pos = plane.x, plane.y
        else:
            self.x += self.speed
            if self.x >= WIDTH:
                self.fire = False
                
class Pizza(Actor):
    
    def __init__(self, x, y):
        Actor.__init__(self, "pizza", (x, y))
        self.width = 36
        self.height = 36
        self.speed = -randint(2, 5)
    
    def reset(self):
        self.x = randint(WIDTH + 50, WIDTH + 750)
        self.y = randint(self.height, HEIGHT - self.height)
        self.speed = -randint(2, 5)
    
    def update(self):
        if self.colliderect(missile) and missile.fire:
            self.reset()
            missile.fire = False
        self.x += self.speed
        if self.x <= -self.width:
            self.reset()        
    
# Init Game
# Hintergrund
backs = []
back0 = Actor(BACKGROUND, (BG_LEFT, BG_BOTTOM))
back1 = Actor(BACKGROUND, (BG_WIDTH + BG_LEFT, BG_BOTTOM))
backs = [back0, back1]
# Player (Flieger)
plane = Plane()
# Missile
missile = Missile()
pizzas = []
for _ in range(NO_ENEMIES):
    pizza = Pizza(randint(WIDTH + 50, WIDTH + 750), randint(36, HEIGHT - 36))
    pizzas.append(pizza)

def update():
    ## Background
    for back in backs:
        back.x -= 1          
        if back.x <= -BG_WIDTH2:
            back.x = BG_WIDTH + BG_WIDTH2
    ## Missile
    missile.update()
    ## Pizzas
    for pizza in pizzas:
        pizza.update()
    ## Flieger
    plane.update()
            
def draw():
    screen.fill("#94b0c2")  # Light gray
    for back in backs:
        back.draw()
    for pizza in pizzas:
        pizza.draw()
    missile.draw()
    plane.draw()

def on_key_down():
    ## Steuerung des Fliegers
    if keyboard.up:
        plane.dir = "UP"
    if keyboard.down:
        plane.dir = "DOWN"
    ## Feuern mit rechter Pfeiltaste
    if keyboard.right:
        # print("FIRE!")
        missile.fire = True
    ## Spielende mit ESC
    if keyboard.escape:
        print("Bye, Bye, Baby!")
        sys.exit()

def on_key_up():
    plane.dir = "NONE"
    
pgzrun.go()