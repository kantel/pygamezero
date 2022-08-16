# Mazegame-Template für 16x16 Tiles

import pgzrun

WIDTH = 480       # 30 Tiles weit
HEIGHT = 272      # 17 Tiles hoch
TITLE = "Mazegame Template"


def draw():
    # screen.fill("#94b0c2")  # Light gray
    screen.blit("pgzhack01", (0, 0))

pgzrun.go()