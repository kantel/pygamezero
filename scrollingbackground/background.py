import pgzrun

WIDTH = 480
HEIGHT = 320
TITLE = "Happy Walker"
TILEWIDTH = 640

class Layer(Actor):
    
    def __init__(self, image, xpos, speed):
        Actor.__init__(self, image)
        self.left = xpos
        self.scroll_speed = speed

    def update(self):
        self.left -= self.scroll_speed
        if self.right < 0:
            self.left = TILEWIDTH - 1

class Walker(Actor):
    
    def __init__(self, image, pos):
        Actor.__init__(self, image, pos)
        self.pos = pos
        self.count = 0
        self.speed = 1

    def update(self):
        self.count += self.speed
        if self.count > 20:
            self.count = 0
        if self.count < 11:
            self.image = "walk1.png"
        else:
            self.image = "walk2.png"

bg = Layer("layer-1", 0, 0)
sky1 =Layer("layer-3", 0, 0.05)
sky2 =Layer("layer-3", TILEWIDTH, 0.05)
mountain1 =Layer("layer-4", 0, 0.1)
mountain2 =Layer("layer-4", TILEWIDTH, 0.1)
hill1 =Layer("layer-5", 0, 0.2)
hill2 =Layer("layer-5", TILEWIDTH, 0.2)
fence1 =Layer("layer-6", 0, 0.5)
fence2 =Layer("layer-6", TILEWIDTH, 0.5)
ground1 =Layer("layer-7", 0, 0.5)
ground2 =Layer("layer-7", TILEWIDTH, 0.5)

layers = [bg, sky1, sky2, mountain1, mountain2, hill1, hill2,
          fence1, fence2, ground1, ground2]

walker = Walker("walk1", (100, HEIGHT - 90))

def draw():
    for layer in layers:
        layer.draw()
    walker.draw()

def update():
    for layer in layers:
        layer.update()
    walker.update()

pgzrun.go()
