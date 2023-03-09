from random import sample

naam_lijst = []
lootjes = {}
naam = True

print(" ")
print("in dit programma kan je met 3 of meer mensen lootjes trekken")

while naam:
    naam_kiezen = input('vul een naam in: ')
    if naam_kiezen not in naam_lijst:
        naam_lijst.append(naam_kiezen)
    elif naam_kiezen in naam_lijst:
        print('deze naam zit al in de lijst')
    if len(naam_lijst) >= 3:
        toevoegen = input('wilt u een naam toevoegen j/n: ')
        if toevoegen == "n":
            naam = False

lootje_verdeling = True
while lootje_verdeling:
    schudden = sample(naam_lijst, len(naam_lijst))
    lootje_verdeling = False
    for x in range(len(naam_lijst)):
        if schudden[x] == naam_lijst[x]:   
            lootje_verdeling = True

for y in range(len(naam_lijst)):
    print(f"{naam_lijst[y]} heeft {schudden[y]}'s lootje getrokken")
