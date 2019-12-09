import pgzrun

TITLE = "Hällo PyGame Zero 🐍"
WIDTH = 300
HEIGHT = 300

kitty = Actor("horngirl")
kitty.topleft = 100, 60

def draw():
    screen.fill((0, 128, 0))
    kitty.draw()

pgzrun.go()