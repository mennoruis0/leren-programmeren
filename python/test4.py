while beurt < 11:
    print(f"ronde: {ronde}")
    print(f"u mag nog {score} keer raden deze ronde!")
    raad=int(input(f"raad een getal tussen {min}/{max}: "))
    som=abs(getal - raad)
    if getal==000:
        break
    if som<=50:
        print(f"je bent{heel}warm")
    if som<=20:
        heel="heel "
    if raad>getal:
        max=raad
        print("lager")
    elif raad<getal:
        min=raad
        print ("hoger")
    elif raad==getal:
        print("geraden!")
        getal=random.randint(1,1000)
        score=11
        goed+=1
        min=1
        max=1000
        print(f"{goed}zijn correct")
        ronde+=1
    if score==1:
        print(f"het was{getal}")
        print("er is een nieuw getal")
        teller=11
        min=1
        max=1000
        getal=random.randint(1,1000)
        print(f"{goed}zijn correct")
        ronde+=1
    score-=1
print (f"einde, je had {goed} getallen goed!")

print('in dit spel raadje een getal tussen de 1 en de 1000')
print('je mag 10 keer raden')
print('dit spel heeft maximaal 20 rondes, maar je kan stoppen na elke ronde door 1234 te typen')
print('Voor elk geraden getal wordt de score opgehoogd met 1')