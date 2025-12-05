import random as rd
import calendar as c

jahr = rd.randrange(1900, 2026) 
print("Zufälliges Jahr:")
print(jahr)
antwort = c.isleap(jahr)
print("Ist es ein Schaltjahr?")
print(antwort)