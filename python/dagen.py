dag = ("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag")

print("  ")
print ("Alle dagen van de week zijn:")
print("  ")
for x in range(7):
    print(dag[x])

print("  ")
print("De werkdagen zijn:")
print("  ")
for x in range(5):
    print(dag[x])

print("  ")
print("De weekenddagen zijn:")
print("  ")
for x in range(5,7):
    print(dag[x])

print("  ")
print("Alle dagen van de week in omgekeerde volgorde zijn:")
print("  ")
for x in range(6, 0, -1):
    print(dag[x])
print(dag[0])

print("  ")
print("De werkdagen in omgekeerde volgorde zijn:")
print("  ")
for x in range(4, 0 ,-1):
    print(dag[x])
print(dag[0])

print("  ")
print("De weekenddagen in omgekeerde volgorde zijn:")
print("  ")
for x in range(6,4, -1):
    print(dag[x])