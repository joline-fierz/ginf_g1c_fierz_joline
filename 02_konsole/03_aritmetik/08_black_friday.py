import random as r

print("Black Friday Aktion")
preis = r.randrange(100, 1000)
rabatt_in_prozent = r.randrange(1, 101)
print(f"Preis: {preis}")
print(f"Rabatt: {rabatt_in_prozent}")
rabatt_in_fr = preis / 100 * rabatt_in_prozent
print(f"{rabatt_in_prozent} % von CHF {preis} sind CHF {rabatt_in_fr}.")
preis_neu = preis - rabatt_in_fr
print(f"Neuer Preis: CHF {preis_neu}")
print("Was für ein Schnäppchen!")
