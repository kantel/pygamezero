import pgzrun

WIDTH = 400
HEIGHT = 400
TITLE = "🐍🐍 Hällo Alien 🐍🐍"

alien = Actor("alien")
alien.pos = (200, 250)
alien.hit = False

def draw():
    screen.fill((0, 80, 125))
    if alien.hit:
        screen.draw.textbox("Eek!", (100, 100, 200, 50))
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()

def set_alien_hurt():
    alien.image = "alien_hurt"
    alien.hit = True
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = "alien"
    alien.hit = False

pgzrun.go()
