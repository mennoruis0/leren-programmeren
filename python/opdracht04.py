from fruitmand import fruitmand
import random
hoeveel = int(input('hoeveel wilt u?: ' ))

lijst = []
for fruit in range(hoeveel):
    lijst.append(random.choice(fruitmand)["name"])
print(lijst)