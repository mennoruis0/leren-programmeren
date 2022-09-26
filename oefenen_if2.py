# Vraag: console of pc
# Bereken prijs pc: 45 euro
# Console: 55 Euro
# print: De game kost je dan:
# vraag of iemand member is


CONSOLE_PRIJS = 55
PC_PRIJS = 45
MEMBER_KORTING = 15


platform = input('Ben je pc of console gamer?')

if platform == 'console':
    prijs = CONSOLE_PRIJS
    if input('bent u member?') == 'ja':
        prijs -= MEMBER_KORTING 
else:
    prijs = PC_PRIJS

print(f'U bent {platform} gamer, dan kost de game: {prijs} Euro')





if samsung_prijs == iphone_prijs:
    print(f'bijde telefoons zijn {iphone_prijs}Euro')
    print('het advies is dus om een Iphone te kopen')


prijs_iphone =  int(input('hoeveel kost de Iphone?'))
prijs_galaxy = int(input('hoeveel kost de Galaxy?'))

verschil = prijs_iphone - prijs_galaxy

if verschil > 50:
    advies = 'Galaxy'
    niet = 'Iphone'
    aankoop_prijs = prijs_galaxy
    niet_prijs = prijs_iphone
else:
advies = 'iphone'
niet =
