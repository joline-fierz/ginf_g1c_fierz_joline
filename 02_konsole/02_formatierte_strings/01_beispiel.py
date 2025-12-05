import random as rd
# Zufallszahl zwischn 1 und 6
note = rd.randrange(1, 7)
# Eckige Klammer bedeuten Liste z.B Einkaufsliste 
# Eine Liste speichert mehrere Strings oder Integer
faecher = ["Informatik", "Mathematik", "Deutsch"]
# choice wählt in einer Liste zufällig ein ELement aus
# Element kann ein String oder Integer sein
fach = rd.choice(faecher)
# Geschweifte Klammer benötigt am Anfang (runde Klammern) immer ein f 
# f steht für formatierter String
print (f"Notenwürfel für das Fach {fach}")
print (f"Ihre gewürfelte Note lautet: {note}")