import random as r
import calendar as cal

jahr = r.randrange(1900, 2026)
antwort = cal.isleap(jahr)
print(f"Es ist das Jahr {jahr}. Ist es ein Schaltjahr? {antwort}")