import random

kleuren = ["rood", "blauw", "groen", "geel", "bruin"]
zak = {}
aantal_mnm = int(input("Hoeveel M&M?: "))

for x in range(aantal_mnm):
    kleur = random.choice(kleuren)
    if kleur not in zak:
        zak.update({kleur: 1})

    elif kleur in zak:
        zak[kleur] +=1
    


print(zak)

