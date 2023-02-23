Giraffen = 4
Struisvogels = 2
Zebra = 4

Giraffen_aantal = int(input('hoeveel giraffen ziet u? '))
struisvogels_aantal = int(input('en hoeveel struisvogels ziet u? '))
zebra_aantal = int(input("en hoeveel zebra's ziet u? "))

Giraffen_poten = Giraffen_aantal * Giraffen
struisvogels_poten = struisvogels_aantal * Struisvogels
zebra_poten = zebra_aantal * Zebra

poten = Giraffen_poten + struisvogels_poten + zebra_poten

print(f'er zijn {poten} poten')