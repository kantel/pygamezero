import pgzrun

room_map = [[1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 1, 1, 1]]

TITLE = "Spacewalk 2 (Demo-Raum)"
WIDTH = 800
HEIGHT = 600
TILE_SIZE = 30

DEMO_OBJECTS = [images.floor, images.pillar]

top_left_x = 100
top_left_y = 150
room_height = 9
room_width  = 9

def draw():
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[room_map[y][x]]
            screen.blit(image_to_draw, 
                (top_left_x + (x*TILE_SIZE),
                 top_left_y + (y*TILE_SIZE) - image_to_draw.get_height()))

pgzrun.go()