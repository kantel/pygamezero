import pgzrun

WIDTH = 400
HEIGHT = 400
TITLE = "🐍🐍 Hällo Alien 🐍🐍"

alien = Actor("alien")
alien.pos = (200, 250)

def draw():
    screen.fill((0, 80, 125))
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

pgzrun.go()
