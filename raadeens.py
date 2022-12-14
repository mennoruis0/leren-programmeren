import random
ronde = 1
totaal = 10
print('in dit spel raadje een getal tussen de 1 en de 1000')
print('je mag 10 keer raden')
print('dit spel heeft maximaal 20 rondes, maar je kan stoppen na elke ronde door 1234 te typen')
print('Voor elk geraden getal wordt de score opgehoogd met 1')
for x in range(20):
    for x in range(10):
        print(f'ronde: {ronde}')
        ronde = ronde + 1
        cijfer = random.randint(1, 1000)
        print(cijfer)
        kansen = 0
        while kansen < 10:
            print('raad wat het getal is in 10 kansen')
            print(f'je hebt nog {totaal} kansen deze ronde')
            raden = input()
            raden = int(raden)
            totaal -= 1
            kansen = kansen + 1
            som = cijfer - raden

            if raden < cijfer:
                print('hoger')

            if cijfer - raden <=20:
                print("Je bent heel warm")

            elif cijfer - raden <=50:
                print("Je bent warm")

            if raden > cijfer:
                print('lager')

            if raden == cijfer:
                break


        if raden == cijfer:
            kansen = str(kansen)
            print(f'je hebt het cijfer in {kansen} kansen')