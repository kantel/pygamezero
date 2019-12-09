import pgzrun

TITLE = "Fetching Kitty"
WIDTH = 500
HEIGHT = 150

kitty = Actor("horngirl")
kitty.topleft = 200, -10

score = 0
mouse_pos = (-2000, -2000)

def draw():
    global mouse_pos
    screen.fill((0, 80, 125))
    kitty.draw()
    screen.draw.circle(mouse_pos, 30, "pink")
    mouse_pos = -200, -200

def update():
    kitty.left += 2
    if kitty.left > WIDTH + 10:
        kitty.left = -10

def on_mouse_down(pos):
    global score
    global mouse_pos
    mouse_pos = pos
    if kitty.collidepoint(pos):
        score += 1
    else:
        score -= 1
        print("Daneben!")
    print(score)

pgzrun.go()