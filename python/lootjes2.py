import random
lijst1 = []

print(" ")
print("in dit programma kan je met 3 of meer mensen lootjes trekken")

while True:
        name = input('geef de naam van één van de deelnemers: ')
        lijst1.append(name)
        if input("zijn alle namen ingevult?: ") == "J" or "j" or "ja":
            if len(lijst1) > 3:
                break
            else:
                continue

check = True

while check:
    schudden = sample(naam_lijst, len(naam_lijst))
    lootje_verdeling = False
    for x in range(len(naam_lijst)):
        if schudden[x] == naam_lijst[x]:   
            lootje_verdeling = True

for y in range(len(naam_lijst)):
    lootjes.update({naam_lijst[y] : schudden[y]})
print(lootjes)