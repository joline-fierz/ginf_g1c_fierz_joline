import random as rd

zahl = rd.randrange(1, 11)
print("Würfelspass!")
print(f"Sie haben eine {zahl} gewürfelt.")
if zahl > 5:
    print("Sie dürfen gleich nochmal würfeln.")
    