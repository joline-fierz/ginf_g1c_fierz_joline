import random as r


print("Nun erscheinen 10 Zufallszahlen")
for _ in range(10):
  zufallszahl = r.randrange(1, 11)
  print(zufallszahl)

print("Das waren 10 Zufallszahlen")
