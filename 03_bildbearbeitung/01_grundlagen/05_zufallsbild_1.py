import PIL.Image as img
import random as rd

bild = img.new("RGB", (100, 100))

for _ in range(7500):
    rot = rd.randrange(0, 256)
    grün = rd.randrange(0, 256)
    blau = rd.randrange(0, 256)
    x = rd.randrange(0, 100)
    y = rd.randrange(0, 100)
    bild.putpixel((x, y), (rot, grün, blau))
bild.save("05_zufallsbild_ergebnis.png") 