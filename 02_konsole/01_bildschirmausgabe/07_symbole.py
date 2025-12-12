import random as r


print("Nun erscheinen 4 Reihen mit jeweils 4 Symbolen")
symbole = ["****", "$$$$", "¢¢¢¢"]
symbol = r.choice(symbole)
for _ in range(4):
  print(symbol)

print("Das waren die 4 ausgewählten symbole in jeweils 4 Reihen")


# Varante B
symbole = ["*", "$", "¢"]
symbol = r.choice (symbole)
for _ in range(4):
  print(4*symbol)
  