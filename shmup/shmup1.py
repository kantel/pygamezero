import pgzrun

WIDTH = 680
HEIGHT = 400
TITLE = "Shmup 1"
TILEWIDTH = 640

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
        self.pos = pos
        self.frame = 0
        
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
        elif keyboard.down:
            self.y += 1
    
    def check_edges(self):
        if self.y >= HEIGHT - 16:
            self.y = HEIGHT - 16
        elif self.y <= 16:
            self.y = 16

bg1 = Layer("bg", 0)
bg2 = Layer("bg", 1188)
layers = [bg1, bg2]

player = Ship("ship1", (60, HEIGHT/2))

def draw():
    for layer in layers:
        layer.draw()
    player.draw()

def update():
    for layer in layers:
        layer.update()
    player.make_animation()
    player.update()
    player.check_edges()

pgzrun.go()
