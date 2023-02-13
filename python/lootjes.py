import random
lijst1 = []

print(" ")
print("in dit programma kan je met 3 of meer mensen lootjes trekken")

while True:
        name = input('geef de naam van één van de deelnemers: ')
        lijst1.append(name)
        if input("zijn alle namen ingevult?: ") == "J" or "j" or "ja":
            if len(lijst1) >=3:
                break
            else: 
                print('dat zijn niet genoeg namen')
                continue
lijst2 = lijst1.copy()
random.shuffle(lijst2)
ok = False
while not ok:
    random.shuffle(lijst2)
    for lootje in range(len(lijst1)):
        if lijst1[lootje] == lijst2[lootje]:
            ok = False
            break
        else:
            ok = True
for x in range(len(lijst1)):
    print(f"{lijst1[x]} heeft {lijst2[x]}")
