import random as rd

zahl_1 = rd.randrange(1, 7)
zahl_2 = rd.randrange(1, 7)
print(f"Die Würfel zeigen {zahl_1} und {zahl_2}.")

if zahl_1 == zahl_2:
    print("Das ist ein Pash! Juhu!")