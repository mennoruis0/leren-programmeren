
import random
getal= random.randint(1,1000)
raad = 0
min = 1
max = 1000
score = 10
goed=0
heel = " "
ronde = 1
print('in dit spel ga je max 10 keer een getal raden tussen 1 en 10000 voor 20 rondes ')
print('als je met het spel wilt stoppen typ: 9999 ')
while ronde < 11:
    print(f"ronde: {ronde}")
    print(f"u mag nog {score} keer raden deze ronde!")
    raad = int(input(f"raad een getal tussen {min}/{max}: "))
    som = abs(getal - raad)
    if getal == 9999:
        break
    if som <= 50:
        print(f"je bent{heel}warm")
    if som <= 20:
        heel = " heel "
    if raad > getal:
        max = raad
        print("lager")
    elif raad < getal:
        min = raad
        print ("hoger")
    elif raad == getal:
        print("geraden!")
        getal = random.randint(1,1000)
        goed+=1
        score=11
        min=1
        max=1000
        print(f"u heeft er {goed} goed")
        ronde+=1
    if score == 1:
        print(f"het getal was {getal}")
        print("er word een nieuw getal gekozen")
        teller = 11
        min=1
        max=1000
        getal = random.randint(1,1000)
        print(f"u heeft er {goed} goed")
        ronde+=1
    score -=1
print (f"EINDE\nje had er {goed} goed! het getal was:{getal}")