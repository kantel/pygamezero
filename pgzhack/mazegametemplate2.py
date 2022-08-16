# Mazegame-Template für 32x32 Tiles

import pgzrun

WIDTH = 960       # 30 Tiles weit
HEIGHT = 544      # 17 Tiles hoch
TITLE = "Mazegame Template 32x32"


def draw():
    # screen.fill("#94b0c2")  # Light gray
    screen.blit("pgzhack201", (0, 0))

pgzrun.go()