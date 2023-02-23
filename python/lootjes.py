import random 
lijst1 = []
check = True

print(" ")
print("in dit programma kan je met 3 of meer mensen lootjes trekken")

while check:
    toevoegen = input("zijn alle namen ingevult?: ")
    if toevoegen == "J" or "j" or "ja":
        naam_kiezen = input('geef de naam van één van de deelnemers: ')
        if naam_kiezen not in lijst1:
            lijst1.append(naam_kiezen)
        elif naam_kiezen in lijst1:
            print('deze naam zit al in de lijst')
    elif toevoegen == "nee" and len(lijst1) < 3:
        print("er zitten nog niet minimaal 3 woorden in")
    else:
        check = False
        
           
lijst2 = lijst1.copy()
random.shuffle(lijst2)
check2 = True

while check2:
    random.shuffle(lijst2)
    for x in range(len(lijst1)): # x = to store the integer value
        if lijst1[x] == lijst2[x]:
            check2 = False
            break

        else:
            check2 = True
for x in range(len(lijst1)):
    print(f"{lijst1[x]} heeft {lijst2[x]}'s lootje getrokken")