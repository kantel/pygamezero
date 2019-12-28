import pgzrun

WIDTH = 640
HEIGHT = 480
TITLE = "Rogue 1"
TILESIZE = 32
HTILES = 20
VTILES = 15

hero_walking = True
enemy_walking = True

## Der Held
hero = Actor("hero")
hero.topleft = (10*TILESIZE, (7*TILESIZE))

def hero_move():
    global hero_walking
    if keyboard.left and hero.left > 0:
        if hero_walking:
            hero.x -= TILESIZE
            hero_walking = False
    if keyboard.right and hero.right < WIDTH:
        if hero_walking:
            hero.x += TILESIZE
            hero_walking = False
    if keyboard.up and hero.top > 0:
        if hero_walking:
            hero.y -= TILESIZE
            hero_walking = False
    if keyboard.down and hero.bottom < HEIGHT:
        if hero_walking:
            hero.y += TILESIZE
            hero_walking = False

def on_key_up():
    global hero_walking, enemy_walking
    hero_walking = True
    enemy_walking = True

## Der Feind
enemy = Actor("enemy")
enemy.topleft = (12*TILESIZE, 0)

def enemy_move():
    global enemy_walking
    enemy_new_x = enemy.x
    enemy_new_y = enemy.y
    if enemy.x > hero.x and enemy_walking:
        enemy_new_x = enemy.x - TILESIZE
        enemy_walking = False
    elif enemy.x < hero.x and enemy_walking:
        enemy_new_x = enemy.x + TILESIZE
        enemy_walking = False
    
    if enemy.y > hero.y and enemy_walking:
        enemy_new_y = enemy.y - TILESIZE
        enemy_walking = False
    elif enemy.y < hero.y and enemy_walking:
        enemy_new_y = enemy.y + TILESIZE
        enemy_walking = False
    
    if enemy_new_x != hero.x:
        enemy.x = enemy_new_y
    
    if enemy_new_y != hero.y:
        enemy.y = enemy_new_y

def draw():
    screen.fill((128, 128, 130))
    enemy.draw()
    hero.draw()

def update():
    hero_move()
    enemy_move()

pgzrun.go()