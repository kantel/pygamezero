import pgzrun

WIDTH = 640
HEIGHT = 480
TITLE = "Rogue 1"
TILESIZE = 32
HTILES = 20
VTILES = 15

walking = True

## Der Held
hero = Actor("hero")
hero.topleft = (10*TILESIZE, (7*TILESIZE))

def hero_move():
    global walking
    if keyboard.left and hero.left > 0:
        if walking:
            hero.x -= TILESIZE
            walking = False
    if keyboard.right and hero.right < WIDTH:
        if walking:
            hero.x += TILESIZE
            walking = False
    if keyboard.up and hero.top > 0:
        if walking:
            hero.y -= TILESIZE
            walking = False
    if keyboard.down and hero.bottom < HEIGHT:
        if walking:
            hero.y += TILESIZE
            walking = False

def on_key_up():
    global walking
    walking = True

## Der Feind
enemy = Actor("enemy")
enemy.topleft = (12*TILESIZE, 0)

def draw():
    screen.fill((128, 128, 130))
    enemy.draw()
    hero.draw()

def enemy_move():
    pass

def update():
    hero_move()
    enemy_move()

pgzrun.go()