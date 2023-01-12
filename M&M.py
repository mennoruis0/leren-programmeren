import random
zak = []
aantal_mnm = int(input("Hoeveel M&M?: "))
kleuren = ['orange', 'blauw', 'groen', 'bruin']
for x in range(aantal_mnm):
    kleur = random.choice(kleuren)
    zak.append(kleur)
print(zak)
