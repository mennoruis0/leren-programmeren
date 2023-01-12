import random
rondes = 1
hoeveelheid = 10
a = -20
b = -50
print('in dit spel raad je een getal tussen de 1 en de 1000')
print('je mag 10 keer raden')
print('dit spel heeft maximaal 20 rondes')
for x in range(20):
    for x in range(10):
        print("")
        print(f'ronde: {rondes}')
        rondes = rondes + 1
        getal = random.randint(1, 1000)
        print(getal)
        kansen = 0
        while kansen < 10:
            print(f'je hebt nog {hoeveelheid} pogingen deze ronde')
            raden = input()
            raden = int(raden)
            hoeveelheid -= 1
            kansen = kansen + 1
            som = getal - raden
            print(f'de som is {som}')  
            if raden < getal:
                print('ga hoger')
            if abs(raden - getal <20):
                print("heel warm!!!")
            elif abs(raden - getal <50):
                print("warm!!!")
            if raden > getal:
                print('ga lager')
            if raden == getal:
                print('dat was goed!')
                break
                
        if raden == getal:
            kansen = str(kansen)
            print(f'je hebt het getal geraden in {kansen} kansen')

