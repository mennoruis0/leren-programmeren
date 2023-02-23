import random
lijst1 = []
check = False

print(" ")
print("in dit programma kan je met 3 of meer mensen lootjes trekken")

while True:
        name = input('geef de naam van één van de deelnemers: ')
        lijst1.append(name)
        if input("zijn alle namen ingevult?: ") == "J" or "j" or "ja":
            if len(lijst1) >=3:
                break
            else:
                continue

lijst2 = lijst1.copy()
random.shuffle(lijst2)

while not check:
    random.shuffle(lijst2)
    for x in range(len(lijst1)): # x = to store the integer value
        if lijst1[x] == lijst2[x]:
            check = False
            break

        else:
            check = True
for x in range(len(lijst1)):
    print(f"{lijst1[x]} heeft {lijst2[x]}'s lootje getrokken")