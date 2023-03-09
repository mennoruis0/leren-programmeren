POTEN_GIRAF = 4
POTEN_ZEBRA = 4
POTEN_STRUISVOGEL = 2

aantal_zebras = int(input('hoeveel giraffen ziet u? '))
aantal_giraffen = int(input('en hoeveel struisvogels ziet u? '))
aantal_struisvogels = int(input("en hoeveel zebra's ziet u? "))

def bereken_poten(giraffen, zebras, struisvogels):

    aantal_poten = zebras * POTEN_ZEBRA + giraffen * POTEN_GIRAF + struisvogels * POTEN_STRUISVOGEL

    return aantal_poten


print(bereken_poten(aantal_giraffen,aantal_zebras,aantal_struisvogels))