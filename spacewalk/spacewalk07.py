import pgzrun
import time, random, math

# Konstanten
TITLE = "Spacewalk 7 (Cleaning Up)"
WIDTH = 800
HEIGHT = 800
TILE_SIZE = 30
PLAYER_NAME = "Jörg"
FRIEND1_NAME = "Zebu"
FRIEND2_NAME = "Joey"

# DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

LANDER_SECTOR = random.randint(1, 24)
LANDER_X = random.randint(2, 11)
LANDER_Y = random.randint(2, 11)

BLACK = (0, 0, 0)
BLUE = (0, 155, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (128, 0, 0)


## Variablen #####################################################################

top_left_x = 100
top_left_y = 150
current_room = 31

## Ende Variablen ################################################################

## Player ########################################################################

player_y, player_x = 2, 5
game_over = False

PLAYER = {
    "left": [images.spacesuit_left, images.spacesuit_left_1,
             images.spacesuit_left_2, images.spacesuit_left_3,
             images.spacesuit_left_4],
    "right": [images.spacesuit_right, images.spacesuit_right_1,
              images.spacesuit_right_2, images.spacesuit_right_3,
              images.spacesuit_right_4],
    "up": [images.spacesuit_back, images.spacesuit_back_1,
           images.spacesuit_back_2, images.spacesuit_back_3,
           images.spacesuit_back_4],
    "down": [images.spacesuit_front, images.spacesuit_front_1,
             images.spacesuit_front_2, images.spacesuit_front_3,
             images.spacesuit_front_4]
}

player_direction = "down"
player_frame = 0
player_image = PLAYER[player_direction][player_frame]
player_offset_x, player_offset_y = 0, 0

PLAYER_SHADOW = {
    "left": [images.spacesuit_left_shadow, images.spacesuit_left_1_shadow,
             images.spacesuit_left_2_shadow, images.spacesuit_left_3_shadow,
             images.spacesuit_left_4_shadow],
    "right": [images.spacesuit_right_shadow, images.spacesuit_right_1_shadow,
              images.spacesuit_right_2_shadow, images.spacesuit_right_3_shadow,
              images.spacesuit_right_4_shadow],
    "up": [images.spacesuit_back_shadow, images.spacesuit_back_1_shadow,
           images.spacesuit_back_2_shadow, images.spacesuit_back_3_shadow,
           images.spacesuit_back_4_shadow],
    "down": [images.spacesuit_front_shadow, images.spacesuit_front_1_shadow,
             images.spacesuit_front_2_shadow, images.spacesuit_front_3_shadow,
             images.spacesuit_front_4_shadow]
}

player_image_shadow = PLAYER_SHADOW["down"][0]

## Ende Player ###################################################################

PILLARS = [images.pillar, images.pillar_95, images.pillar_80,
           images.pillar_60, images.pillar_50]
        
wall_transparency_frame = 0


## Game Map ######################################################################

# Karten-Daten
MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH*MAP_HEIGHT

GAME_MAP = [["Raum 0 – wo unnützes Zeug aufbewahrt wird", 0, 0, False, False]]

outdoor_rooms = range(1, 26) # Sektor 1 bis Sektor 25
for planetsectors in outdoor_rooms:
    GAME_MAP.append( ["Die staubige Planetenoberfläche", 13, 13, True, True])

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

## Objects #######################################################################

objects = {
    0: [images.floor, None, "Der Boden ist glänzend und sauber"],
    1: [images.pillar, images.full_shadow, "Die Wand ist glatt und kalt"],
    2: [images.soil, None, "Es ist wie Wüste. Oder ist es Wüste?"],
    3: [images.pillar_low, images.half_shadow, "Die Wand ist glatt und kalt"],
    4: [images.bed, images.half_shadow, "Ein ordentliches, bequemes Bett"],
    5: [images.table, images.half_shadow, "Er besteht aus festem Kunststoff."],
    6: [images.chair_left, None, "Ein Stuhl mit weichem Kissen"],
    7: [images.chair_right, None, "Ein Stuhl mit weichem Kissen"],
    8: [images.bookcase_tall, images.full_shadow, "Regal mit Handbüchern"],
    9: [images.bookcase_small, images.half_shadow, "Regal mit Handbüchern"],
    10: [images.cabinet, images.half_shadow, "Schließfach zum Aufbewahren persönlicher Gegenstände"],
    11: [images.desk_computer, images.half_shadow, "Computer. Nutzen sie ihn für Ihre Überlebensdiagnose"],
    12: [images.plant, images.plant_shadow, "Eine Raumbeerenpflane, hier gewachsen"],
    13: [images.electrical1, images.half_shadow, "Elektrische Systeme zur Stromversorgung der Weltraumstation"],
    14: [images.electrical2, images.half_shadow, "Elektrische Systeme zur Stromversorgung der Weltraumstation"],
    15: [images.cactus, images.cactus_shadow, "Autsch! Vorsicht beim Kaktus!"],
    16: [images.shrub, images.shrub_shadow, "Ein Weltraumsalat. etwas schlaff, aber erstaunlicherweise wächst er hier"],
    17: [images.pipes1, images.pipes1_shadow, "Wasserreinigungsrohre"],
    18: [images.pipes2, images.pipes2_shadow, "Rohre für die Lebenserhaltungssysteme"],
    19: [images.pipes3, images.pipes3_shadow, "Rohre für die Lebenserhaltungssysteme"],
    20: [images.door, images.door_shadow, "Sicherheitstür. Öffnet sich automatisch für Astronauten in funktionierenden Raumanzügen."],
    21: [images.door, images.door_shadow, "Luftschleuse. Aus Sicherheitsgründen ist eine Zwei-Personen-Bedienung erforderlich."],
    22: [images.door, images.door_shadow, "Eine verschlossene Tür. Sie braucht " + PLAYER_NAME + "s Zugangskarte"],
    23: [images.door, images.door_shadow, "Eine verschlossene Tür. Sie braucht " + FRIEND1_NAME + "s Zugangskarte"],
    24: [images.door, images.door_shadow, "Eine verschlossene Tür. Sie braucht " + FRIEND2_NAME + "s Zugangskarte"],
    25: [images.door, images.door_shadow,
         "Eine verschlossene Tür. Sie wird vom Kontrollzentrum aus geöffnet"],
    26: [images.door, images.door_shadow, "Eine verschlossene Tür in der Systemtechnik."],
    27: [images.map, images.full_shadow,
         "Auf dem Bildschirm wird angezeigt, daß die Abnsturzstelle " \
         + str(LANDER_SECTOR) + " // X: " + str(LANDER_X) + \
         " // Y: " + str(LANDER_Y) + " war"],
    28: [images.rock_large, images.rock_large_shadow, "Ein Felsen. Ihre raue Oberfläche fühlt sich an wie ein Schleifstein", "Ein Felsen"],
    29: [images.rock_small, images.rock_small_shadow, "Ein kleines aber schweres Stück Marsfelsen"],
    30: [images.crater, None, "Ein Krater in der Planetenoberfläche"],
    31: [images.fence, None, "Ein feiner Gazezaun. Er schützt die Station vor Staubstürmen"],
    32: [images.contraption, images.contraption_shadow, "Eines der wissenschaftlichen Experimente. Das Gerät vibriert sanft"],
    33: [images.robot_arm, images.robot_arm_shadow, "Ein Roboterarm für schwere Teile"],
    34: [images.toilet, images.half_shadow, "Eine funkelnde, saubere Toilette"],
    35: [images.sink, None, "Ein Waschbecken mit fließendem Wasser", "Wasserhähne"],
    36: [images.globe, images.globe_shadow, "Eine riesiger Marsglobus. Es schimmert sanft von innen"],
    37: [images.science_lab_table, None, "Eine Tabelle mit Experimenten zur Analyse des Planetenbodens und des Marsstaubes"],
    38: [images.vending_machine, images.full_shadow, "Ein Verkaufsautomat mit Münzeinwurf.", "Verkaufsautomat"],
    39: [images.floor_pad, None,
         "Ein Drucksensor sorgt dafür, daß niemand die Station alleine verläßt."],
    40: [images.rescue_ship, images.rescue_ship_shadow, "Ein Rettungsschiff!"],
    41: [images.mission_control_desk, images.mission_control_desk_shadow, "Anzeige im Kontrollzentrum"],
    42: [images.button, images.button_shadow, "Dieser Knopf öffnet die zeitverriegelte Tür zur Leitwarte."],
    43: [images.whiteboard, images.full_shadow, "Das Whiteboard wird in Brainstorming- und Planungssitzungen verwendet."],
    44: [images.window, images.full_shadow,  "Das Fenster bietet einen Blick auf die Planetenoberfläche."],
    45: [images.robot, images.robot_shadow, "Ein ausgeschalteter Reinigungsroboter."],
    46: [images.robot2, images.robot2_shadow, "Ein Roboter zur Erforschung der Planetenoberfläche, der auf seinen Aufbau wartet."],
    47: [images.rocket, images.rocket_shadow, "Ein Einpersonen-Schiff in Reparatur"], 
    48: [images.toxic_floor, None, "Giftboden, nicht betreten!"],
    49: [images.drone, None, "Lieferdrohne"],
    50: [images.energy_ball, None, "Ein Energieball – gefährlich!"],
    51: [images.energy_ball2, None, "Ein Energieball – gefährlich!"],
    52: [images.computer, images.computer_shadow, "Ein Computer zur Bedienung der Systeme der Raumstation"],
    53: [images.clipboard, None, "Ein Clipboard mit Gekritzel", "Clipboard"],
    54: [images.bubble_gum, None,
         "Ein Stück klebriges Kaugummi. Raumbeeren-Geschmack.", "Kaugummi"],
    55: [images.yoyo, None, "Ein Spielzeug mit feiner, starker Schnur und aus Kunststoff. Wird für Antigravitations-Experimente verwendet.", PLAYER_NAME + "s Jojo"],
    56: [images.thread, None, "Ein Stück feine, starke Schnur", "Schnur"],
    57: [images.needle, None, "Eine Nadel vom Kaktus", "Kakteennadel"],
    58: [images.threaded_needle, None, "Eine Kakteennadel, die ein Ende einer Schnur durchbohrt", "Nadel und Schnur"],
    59: [images.canister, None, "Der Luftbehälter hat ein Leck.", "Durchlöcherter Luftbehälter"],
    60: [images.canister, None, "Es sieht so aus, als würde das Siegel halten!", "Versiegelter Luftbehälter"],
    61: [images.mirror, None, "Der Spiegel wirft einen Lichtkreis an die Wände.", "Spiegel"], 
    62: [images.bin_empty, None, "Ein selten benutzter Kanister aus leichtem Kunststoff", "Kanister"],
    63: [images.bin_full, None, "Ein schwerer Kanister voll Wasser", "Kanister voll Wasser"],
    64: [images.rags, None,
         "Ein öliger Lappen. Fasse ihn nur an einer Ecke an, wenn Du ihn aufhebst!", "Öliger Lappen"], 
    65: [images.hammer, None, "Ein Hammer. Vielleicht gut, um Dinge aufzubrechen ...", "Hammer"],
    66: [images.spoon, None, "Ein großer Servierlöffel", "Löffel"],
    67: [images.food_pouch, None, "Ein Beutel mit getrockneter Nahrung. Sie braucht Wasser", "Weltraumnahrung"], 
    68: [images.food, None,
         "Ein Beutel mit Fertignahrung. Verwende ihn, um 100% Energie zu erhalten.", "Fertignahrung"], 
    69: [images.book, None, "Das Buch hat die Worte »Don't Panic« in großen, freundlichen Buchstaben auf dem Umschlag", "Buch"], 
    70: [images.mp3_player, None, "Ein MP3-Player mit den neuesten Hits", "MP3-Player"],
    71: [images.lander, None, "Der »Pudel«, ein Mini-Raumschiff.In der schwarzen Box ist ein Funkgerät eingebaut", "Der »Puidel«"],
    72: [images.radio, None, "Das Funkgerät aus dem »Pudel«", "Funkgerät"],
    73: [images.gps_module, None, "Ein GPS-Modul", "GPS-Modul"],
    74: [images.positioning_system, None, "Teil eines Ortungssystems. Benötigt ein GPS-Modul", "Ortungssystem-Schnittstelle"],
    75: [images.positioning_system, None, "Ein funktionierendes Ortungssystem", "Ortungssystem"],
    76: [images.scissors, None, "Schere. Sie ist zu stumpf, um irgendetwas zu schneiden. Kannst Du sie schärfen?", "Stumpfe Schere"],
    77: [images.scissors, None, "Rasiermesserscharfe Schere. Vorsicht!", "Scharfe Schere"],
    78: [images.credit, None, "Eine kleine Münze für die Verkaufsautomaten der Station", "Automatenmünze"],
    79: [images.access_card, None,
         "Diese Zutrittskarte ist auf " + PLAYER_NAME + " ausgestellt", "Zutrittskarte"],
    80: [images.access_card, None,
         "Diese Zutrittskarte ist auf  " + FRIEND1_NAME + " ausgestellt", "Zutrittskarte"],
    81: [images.access_card, None,
         "Diese Zutrittskarte ist auf  " + FRIEND2_NAME + " ausgestellt", "Zutrittskarte"]
}

items_player_may_carry = list(range(52, 83))
items_player_may_stand_on = items_player_may_carry + [0, 39, 2, 48]

## Ende Objects ##################################################################

## Scenery #######################################################################

# Scenery describes objects that cannot move between rooms.
# room number: [[object number, y position, x position]...]
scenery = {
    26: [[39,8,2]],
    27: [[33,5,5], [33,1,1], [33,1,8], [47,5,2],
         [47,3,10], [47,9,8], [42,1,6]],
    28: [[27,0,3], [41,4,3], [41,4,7]],
    29: [[7,2,6], [6,2,8], [12,1,13], [44,0,1],
         [36,4,10], [10,1,1], [19,4,2], [17,4,4]],
    30: [[34,1,1], [35,1,3]],
    31: [[11,1,1], [19,1,8], [46,1,3]],
    32: [[48,2,2], [48,2,3], [48,2,4], [48,3,2], [48,3,3],
         [48,3,4], [48,4,2], [48,4,3], [48,4,4]],
    33: [[13,1,1], [13,1,3], [13,1,8], [13,1,10], [48,2,1],
         [48,2,7], [48,3,6], [48,3,3]],
    34: [[37,2,2], [32,6,7], [37,10,4], [28,5,3]],
    35: [[16,2,9], [16,2,2], [16,3,3], [16,3,8], [16,8,9], [16,8,2], [16,1,8],
         [16,1,3], [12,8,6], [12,9,4], [12,9,8],
         [15,4,6], [12,7,1], [12,7,11]],
    36: [[4,3,1], [9,1,7], [8,1,8], [8,1,9],
         [5,5,4], [6,5,7], [10,1,1], [12,1,2]],
    37: [[48,3,1], [48,3,2], [48,7,1], [48,5,2], [48,5,3],
         [48,7,2], [48,9,2], [48,9,3], [48,11,1], [48,11,2]],
    38: [[43,0,2], [6,2,2], [6,3,5], [6,4,7], [6,2,9], [45,1,10]],
    39: [[38,1,1], [7,3,4], [7,6,4], [5,3,6], [5,6,6],
         [6,3,9], [6,6,9], [45,1,11], [12,1,8], [12,1,4]], 
    40: [[41,5,3], [41,5,7], [41,9,3], [41,9,7],
         [13,1,1], [13,1,3], [42,1,12]],
    41: [[4,3,1], [10,3,5], [4,5,1], [10,5,5], [4,7,1],
         [10,7,5], [12,1,1], [12,1,5]],
    43: [[18, 1, 1], [18, 1, 4], [14, 1, 6], [52, 4, 5], [52, 4, 2]],
    44: [[46,4,3], [46,4,5], [18,1,1], [19,1,3],
         [19,1,5], [52,4,7], [14,1,8]],
    45: [[48,2,1], [48,2,2], [48,3,3], [48,3,4], [48,1,4], [48,1,1]],
    46: [[10,1,1], [4,1,2], [8,1,7], [9,1,8], [8,1,9], [5,4,3], [7,3,2]],
    47: [[9,1,1], [9,1,2], [10,1,3], [12,1,7], [5,4,4], [6,4,7], [4,1,8]],
    48: [[17,4,1], [17,4,2], [17,4,3], [17,4,4], [17,4,5], [17,4,6], [17,4,7],
         [17,8,1], [17,8,2], [17,8,3], [17,8,4],
         [17,8,5], [17,8,6], [17,8,7], [14,1,1]],
    49: [[14,2,2], [14,2,4], [7,5,1], [5,5,3], [48,3,3], [48,3,4]], 
    50: [[45,4,8], [11,1,1], [13,1,8], [33,2,1], [46,4,6]] 
}

checksum = 0
check_counter = 0
for key, room_scenery_list in scenery.items():
    for scenery_item_list in room_scenery_list:
        checksum += (scenery_item_list[0] * key
                     + scenery_item_list[1] * (key + 1) 
                     + scenery_item_list[2] * (key + 2))
        check_counter += 1
print(check_counter, "scenery items")
## assert check_counter == 161, "Expected 161 scenery items"
## assert checksum == 200095, "Error in scenery data"
print("Scenery checksum: " + str(checksum))

# Add random scenery in planet locations:
for room in range(1, 26):
    if room != 13: #Skip room 13
        scenery_item = random.choice([16, 28, 29, 30])
        scenery[room] = [[scenery_item, random.randint(2, 10), random.randint(2, 10)]]

# Use loops to add fences to the planet surface:
for room_coordinate in range(0, 13):
    for room_number in [1, 2, 3, 4, 5]:      # Add top fence
        scenery[room_number] += [[31, 0, room_coordinate]]
    for room_number in [1, 6, 11, 16, 21]:   # Add left fence
        scenery[room_number] += [[31, room_coordinate, 0]]
    for room_number in [5, 10, 15, 20, 25]:  # Add right fence
        scenery[room_number] += [[31, room_coordinate, 12]]

del scenery[21][-1]   # Delete last fence panel in room 21
del scenery[25][-1]   # Delete last fence panel in room 25

## Ende Scenery ##################################################################

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
    
    if current_room in scenery:
        for this_scenery in scenery[current_room]:
            scenery_number = this_scenery[0]
            scenery_y = this_scenery[1]
            scenery_x = this_scenery[2]
            room_map[scenery_y][scenery_x] = scenery_number
            image_here = objects[scenery_number][0]
            image_width = image_here.get_width()
            image_width_in_tiles = image_width//TILE_SIZE
            for tile_number in range(1, image_width_in_tiles):
                room_map[scenery_y][scenery_x + tile_number] = 255
    
    center_y = HEIGHT//2
    center_x = WIDTH//2
    room_pixel_width = room_width*TILE_SIZE
    room_pixel_height = room_height*TILE_SIZE
    top_left_x = center_x - 0.5*room_pixel_width
    top_left_y = (center_y - 0.5*room_pixel_height) + 110

## Ende Karte erstellen ###########################################################

## Game Loop ######################################################################

def start_room():
    show_text("Du bist hier (" + str(current_room) + "): " + room_name, 0)

def game_loop():
    global player_x, player_y, current_room
    global from_player_y, from_player_y
    global player_image, player_image_shadow
    global selecterd_item, item_carrying, energy
    global player_offset_x, player_offset_y
    global player_frame, player_direction
    
    if game_over:
        return
    
    if player_frame > 0:
        player_frame += 1
        time.sleep(0.05)
        if player_frame == 5:
            player_frame = 0
            player_offset_x = 0
            player_offset_y = 0
            
    # Save Players current position
    old_player_x = player_x
    old_player_y = player_y
    
    # Move if key is pressed
    if player_frame == 0:
        if keyboard.right:
            from_player_x = player_x
            from_player_y = player_y
            player_x += 1
            player_direction = "right"
            player_frame = 1
        elif keyboard.left:
            from_player_x = player_x
            from_player_y = player_y
            player_x -= 1
            player_direction = "left"
            player_frame = 1
        elif keyboard.up:
            from_player_x = player_x
            from_player_y = player_y
            player_y -= 1
            player_direction = "up"
            player_frame = 1
        elif keyboard.down:
            from_player_x = player_x
            from_player_y = player_y
            player_y += 1
            player_direction = "down"
            player_frame = 1

    # Check for exiting the room
    # through door on right
    if player_x == room_width:
        current_room += 1
        generate_map()
        player_x = 0   # enter at left
        player_y = room_height//2   # enter at door
        player_frame = 0
        start_room()
        return
    
    #through door on left
    if player_x == -1:
        current_room -= 1
        generate_map()
        player_x = room_width - 1   # enter at right
        player_y = room_height//2   # enter at door
        player_frame = 0
        start_room()
        return
    
    # through door at bottom
    if player_y == room_height:
        current_room += MAP_WIDTH
        generate_map()
        player_y = 0   # enter at to
        player_x = room_width//2   # enter at door
        player_frame = 0
        start_room()
        return
    
    # through door at top
    if player_y == -1:
        current_room -= MAP_WIDTH
        generate_map()
        player_y = room_height - 1   # enter at left
        player_x = room_width//2     # enter at door
        player_frame = 0
        start_room()
        return
    

    # Kollisionsdetektion
    if room_map[player_y][player_x] not in items_player_may_stand_on:
        player_x = old_player_x
        player_y = old_player_y
        player_frame = 0
    
    # Move
    if player_direction == "right" and player_frame > 0:
        player_offset_x = -1 + (0.25*player_frame)
    if player_direction == "left" and player_frame > 0:
        player_offset_x = 1 - (0.25*player_frame)
    if player_direction == "up" and player_frame > 0:
        player_offset_y = 1 - (0.25*player_frame)
    if player_direction == "down" and player_frame > 0:
        player_offset_y = -1 + (0.25*player_frame)

## Ende Game Loop #################################################################

## Display ########################################################################

def draw_image(image, y, x):
    screen.blit(image, (top_left_x + (x*TILE_SIZE), top_left_y + (y*TILE_SIZE) - image.get_height()))

def draw_shadow(image, y, x):
    screen.blit(image, (top_left_x + (x*TILE_SIZE), top_left_y + (y*TILE_SIZE)))

def draw_player():
    player_image = PLAYER[player_direction][player_frame]
    draw_image(player_image, player_y + player_offset_y, player_x + player_offset_x)
    player_image_shadow = PLAYER_SHADOW[player_direction][player_frame]
    draw_shadow(player_image_shadow, player_y + player_offset_y, player_x + player_offset_x)

def draw():
    if game_over:
        return
    
    # Draw background image
    box = Rect((0, 150), (800, 600))
    screen.draw.filled_rect(box, RED)
    box = Rect((0, 0), (800, top_left_y + (room_height - 1)*TILE_SIZE))
    screen.surface.set_clip(box)
    floor_type = get_floor_type()
    
    # Lay down floor tiles, then items on floor
    for y in range(room_height):
        for x in range(room_width):
            draw_image(objects[floor_type][0], y, x)
            # Next line enables shadows to fall on top of objects on floor
            if room_map[y][x] in items_player_may_stand_on:
                draw_image(objects[room_map[y][x]][0], y, x)
                
    # Sonderbehandlung pressure pad (Raum 26)
    if current_room == 26:
        draw_image(objects[39][0], 8, 2)
        image_on_pad = room_map[8][2]
        if image_on_pad > 0:
            draw_image(objects[image_on_pad][0], 8, 2)
    
    for y in range(room_height):
        for x in range(room_width):
            item_here = room_map[y][x]
            # Player cannot walk on 255
            if item_here not in items_player_may_stand_on + [255]:
                image = objects[item_here][0]
                
                if ((current_room in outdoor_rooms and y == room_height - 1 and room_map[y][x] == 1)
                or (current_room not in outdoor_rooms and y == room_height - 1 and room_map[y][x] == 1
                and x > 0 and x < room_width - 1)):
                    image = PILLARS[wall_transparency_frame]
                    
                draw_image(image, y, x)
                
                # If object has a shadow
                if objects[item_here][1] is not None:
                    shadow_image = objects[item_here][1]
                    # if shadow might need horizontal tiling
                    if shadow_image in [images.half_shadow, images.full_shadow]:
                        shadow_width = image.get_width()//TILE_SIZE
                        # Use shadow across width of object
                        for z in range(0, shadow_width):
                            draw_shadow(shadow_image, y, x + z)
                    else:
                        draw_shadow(shadow_image, y, x)
        if (player_y == y):
            draw_player()
            
    screen.surface.set_clip(None)

def adjust_wall_transparency():
    global wall_transparency_frame
    
    if (player_y == room_height - 2
        and room_map[room_height - 1][player_x] == 1
        and wall_transparency_frame < 4):
        wall_transparency_frame += 1   # Fade wall out
        
    if ((player_y < room_height - 2 or room_map[room_height - 1][player_x] != 1)
        and wall_transparency_frame > 0):
        wall_transparency_frame -= 1   # Fade wall in

def show_text(text_to_show, line_number):
    if game_over:
        return
    text_lines = [15, 50]
    box = Rect((0, text_lines[line_number]), (800, 35))
    screen.draw.filled_rect(box, BLACK)
    screen.draw.text(text_to_show, (20, text_lines[line_number]), color = GREEN)

## Ende Display ###################################################################

## Start ##########################################################################

clock.schedule_interval(game_loop, 0.03)
generate_map()
clock.schedule_interval(adjust_wall_transparency, 0.05)

pgzrun.go()