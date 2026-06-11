import PIL.Image as img

bild = img.open("portland.png")

for x in range(0, bild.width):
    for y in range(0, bild.height):
        #getpixel: geht zu den Kordinaten (x, y)
        # Kopiert den Farbwert in die Variabeln r, g und b
        r, g, b = bild.getpixel((x, y))

        #Verdoppelt den Farbwert
        #Bild wird neu doppelt so hell.
        r_neu = r
        g_neu = 0
        b_neu = 0
        
        bild.putpixel((x, y), (r_neu, g_neu, b_neu))
bild.save("01_beispiel_ergebnis.png")
