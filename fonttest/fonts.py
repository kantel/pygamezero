import pgzrun

WIDTH = 640
HEIGHT = 480
TITLE = "Seltsame Zeichen in Pygame Zero 🤡"

margin = 20
start = 80

palindrom = "Zwölf Boxkäpfer jagen Eva quer über den großen Sylter Deich."
russian   = "Ljudmila Michailowna Pawlitschenko (Людмила Михайловна Павличенко) gilt als erfolgreichste Scharfschützin aller Zeiten."

texts = [palindrom, russian]

def draw():
    global start
    screen.fill((30, 30, 30))
    for text in texts:
        screen.draw.text(text, (margin, start), fontname = "comichelvetic_medium", fontsize = 32,
                         color = (237, 118, 112),
                         width = WIDTH - 2*margin, lineheight = 1.5)
        print(text)
        start += 120

pgzrun.go()