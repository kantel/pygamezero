import pgzrun
import time, random, math

# Konstanten
TITLE = "Spacewalk 3 (Game-Map)"
WIDTH = 800
HEIGHT = 800
TILE_SIZE = 30
PLAYER_NAME = "Jörg"
FRIEND1_NAME = "Zebu"
FRIEND2_NAME = "Joey"

# Variablen
top_left_x = 100
top_left_y = 150
current_room = 31

DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

# Karten-Daten
MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH*MAP_HEIGHT

## Game Map #################################################################

GAME_MAP = [["Raum 0 – wo unnützes Zeug aufbewahrt wird", 0, 0, False, False]]

outdoor_rooms = range(1, 26) # Sektor 1 bis Sektor 25
for planetsectors in outdoor_rooms:
    GAME_MAP.append( ["Die staubige Planetenpberfläche", 13, 13, True, True])

GAME_MAP += [
        # ["Raum-Name", height, width, Top Exit? Right Exit]
        ["Luftschleuse", 13, 5, True, False], # Raum 26
        ["Konstruktionslabor", 13, 13, False, False], # Raum 27
        ["Pudel?-Kontrollraum", 9, 13, False, True], # Raum 28
        ["Aussichtsraum", 9, 15, False, False], # Raum 29
        ["Gemeinschaftsduschen", 5, 5, False, False], # Raum 30
        ["Vorraum zur Luftschleuse", 7, 11, True, True], # Raum 31
        ["Linker Vorbereitungsraum", 9, 7, True, False], # Raum 32
        ["Rechter Vorbereitungsraum", 7, 13, True, True], # Raum 33
        ["Wissenschaftslabor", 13, 13, False, True], # Raum 34
        ["Gewächshaus", 13, 13, True, False], # Raum 35
        [PLAYER_NAME + "s Schlafzimmer", 9, 11, False, False], # Raum 36
        ["Westlicher Flur", 15, 5, True, True], # Raum 37
        ["Besprechungszimmer", 7, 13, False, True], # Raum 38
        ["Gemeinschaftsraum", 11, 13, True, False], # Raum 39
        ["Kontrollzentrum", 14, 14, False, False], # Raum 40
        ["Krankenstation", 12, 7, True, False], # Raum 41
        ["Westlicher Flur", 9, 7, True, False], # Raum 42
        ["Leitwarte", 9, 9, False, True], # Raum 43
        ["Systemtechnik", 9, 11, False, False], # Raum 44
        ["Sicherheitsportal zum Kontrollzentrum", 7, 7, True, False], # Raum 45
        [FRIEND1_NAME + "s Schlafzimmer", 9, 11, True, True], # Raum 46
        [FRIEND2_NAME + "s Schlafzimmer", 9, 11, True, True], # Raum 47
        ["Raum mit Rohrleitungen", 13, 11, True, False], # Raum 48
        ["Büro des Chefingenieurs", 9, 7, True, True], # Raum 49
        ["Roboterwerkstatt", 9, 11, True, False] # Raum 50
    ]

assert len(GAME_MAP) - 1 == MAP_SIZE, "Kartengröße GAME_MAP stimmen nicht überein"

## Ende Game Map #################################################################


## Karte erstellen ###############################################################

def get_floor_type():
    if current_room in outdoor_rooms:
        return 2  # Sandboden
    else:
        return 0  # Bodenfliesen

def generate_map():
    global room_map, room_width, room_height, room_name, hazard_map
    global top_left_x, top_left_y, wall_transparency_frame
    room_data = GAME_MAP[current_room]
    room_name = room_data[0]
    room_height = room_data[1]
    room_width = room_data[2]
    
    floor_type = get_floor_type()
    if current_room in range(1, 21):   # Marsoberfläche
        bottom_edge = 2                # Sandboden
        side_edge = 2                  # Sandboden
    if current_room in range(21, 26):  # Grenze zur Marsstation
        bottom_edge = 1                # Wall
        side_edge = 2                  # Sandboden
    if current_room > 25:              # Marsstation
        bottom_edge = 1                # Wall
        side_edge = 1                  # Wall
    
    # Create top line of room map:
    room_map = [[side_edge]*room_width]
    # Add middle lines of room map (wall, floor to fill width, wall):
    for y in range(room_height - 2):
        room_map.append([side_edge] + [floor_type]*(room_width - 2) + [side_edge])
    # Add bottom line of room map:
    room_map.append([bottom_edge]*room_width)
    
    # Add doorways
    middle_row = room_height//2
    middle_column = room_width//2
    
    # If exit at right of this room
    if room_data[4]:
        room_map[middle_row][room_width - 1] = floor_type
        room_map[middle_row + 1][room_width - 1] = floor_type
        room_map[middle_row - 1][room_width - 1] = floor_type
        
    # If room is not on left of map:
    if current_room % MAP_WIDTH != 1:
        room_to_left = GAME_MAP[current_room - 1]
        # If room on the left has a right exit, add a left exit in this room
        if room_to_left[4]:
            room_map[middle_row][0] = floor_type
            room_map[middle_row + 1][0] = floor_type
            room_map[middle_row - 1][0] = floor_type
    
    # If exit at top of this room
    if room_data[3]:
        room_map[0][middle_column] = floor_type
        room_map[0][middle_column + 1] = floor_type
        room_map[0][middle_column - 1] = floor_type
    
    # If room is not on bottom row:
    if current_room <= MAP_SIZE - MAP_WIDTH:
        room_below = GAME_MAP[current_room + MAP_WIDTH]
        # If room below has a top exit, add exit at bottom of this one
        if room_below[3]:
            room_map[room_height - 1][middle_column] = floor_type
            room_map[room_height - 1][middle_column + 1] = floor_type
            room_map[room_height - 1][middle_column - 1] = floor_type

## Ende Karte erstellen ###########################################################

## Explorer (wird später ersetzt) #################################################

def draw():
    global room_height, room_width, room_map
    generate_map()
    screen.clear()
    
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[room_map[y][x]]
            screen.blit(image_to_draw, (top_left_x + (x*TILE_SIZE), 
                                        top_left_y + (y*TILE_SIZE) - image_to_draw.get_height()))

def movement():
    global current_room
    old_room = current_room
    
    if keyboard.left:
        current_room -= 1
    if keyboard.right:
        current_room += 1
    if keyboard.up:
        current_room -= MAP_WIDTH
    if keyboard.down:
        current_room += MAP_WIDTH
    
    if current_room > 50:
        current_room = 50
    if current_room < 1:
        current_room = 1
        
    if current_room != old_room:
        print("Du betrittst Raum Nummer " + str(current_room))

clock.schedule_interval(movement, 0.1)

## Ende Explorer ##################################################################

pgzrun.go()