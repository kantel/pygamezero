import pgzrun
import time, random, math

# Konstanten
TITLE = "Spacewalk 4 (Objects)"
WIDTH = 800
HEIGHT = 800
TILE_SIZE = 30
PLAYER_NAME = "Jörg"
FRIEND1_NAME = "Zebu"
FRIEND2_NAME = "Joey"

DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

LANDER_SECTOR = random.randint(1, 24)
LANDER_X = random.randint(2, 11)
LANDER_Y = random.randint(2, 11)

## Variablen #####################################################################

top_left_x = 100
top_left_y = 150
current_room = 31

## Ende Variablen ################################################################

## Game Map #################################################################

# Karten-Daten
MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH*MAP_HEIGHT

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
    
    room_map[2][4] = 7
    room_map[2][6] = 6
    room_map[1][1] = 8
    room_map[1][2] = 9
    room_map[1][8] = 12
    room_map[1][9] = 9
    
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = objects[room_map[y][x]][0]
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