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
LEFT = WIDTH/2
BOTTOM = HEIGHT/2
NO_ENEMIES = 10

# Konstanten
BG_WIDTH = 1067             # Breite des Hintergrundbildes
BG_WIDTH2   = 533           # BGWIDTH//2 (abgerundet)
BACKGROUND = "desert"
PLANE_X = 70                # X-Position des Fliegers (bleibt fest)

# Klassendefinitionen

class Missile(Actor):
    
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
    
    def update(self):
        self.x += self.speed
        if self.x <= -self.width:
            self.reset()        
    
# Init Game
# Hintergrund
backs = []
back0 = Actor(BACKGROUND, (LEFT, BOTTOM))
back1 = Actor(BACKGROUND, (BG_WIDTH + LEFT, BOTTOM))
backs = [back0, back1]
# Player (Flieger)
plane_image = []
for i in range(3):
    img = "planered_" + str(i)
    plane_image.append(img)
plane = Actor(plane_image[0], (PLANE_X, 200))   # Startposition
plane.r = 0
plane.updown = 3
plane.dir = "NONE"
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
        if pizza.colliderect(missile) and missile.fire:
            pizza.reset()
            missile.fire = False
        pizza.update()
    ## Flieger
    if plane.dir == "NONE":
        plane.y += 0
    elif plane.dir == "UP":
        if plane.y > 20:
            plane.y -= plane.updown
    elif plane.dir == "DOWN":
        if plane.y < HEIGHT - 20:
            plane.y += plane.updown
    plane.image = plane_image[int(plane.r)]
    plane.r += 0.2
    if plane.r >= 3.0:
        plane.r = 0
            
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
        print("FIRE!")
        missile.fire = True
    ## Spielende mit ESC
    if keyboard.escape:
        print("Bye, Bye, Baby!")
        sys.exit()

def on_key_up():
    plane.dir = "NONE"
    
pgzrun.go()