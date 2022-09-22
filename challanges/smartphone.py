# de keuze is tussen Iphone 13 en Samsung Galaxy S22
# Jonas koopt de Iphone als deze maximaal 50 euro duurder is dan de Galaxy S22

from lib2to3.pgen2.token import MINUS


iphone_prijs =  input('hoeveel kost de Iphone?')
samsung_prijs = input('hoeveel kost de Samsung?')

#prijsverschil1 = samsung_prijs - iphone_prijs 
#prijsverschil2 = iphone_prijs - samsung_prijs  


if iphone_prijs > samsung_prijs:
    print(f'De Iphone is het duurst, deze telefoon kost:{iphone_prijs}Euro')
    print(f'De Samsung is het goedkoopst, deze telefoon kost:{samsung_prijs}Euro')
    print(f'Het advies is dus de Samsung te kopen. Deze is namelijk {iphone_prijs - samsung_prijs} Euro goedkoper')


if samsung_prijs > iphone_prijs:
    print(f'De Samsung is het duurst, deze telefoon kost:{samsung_prijs}Euro')
    print(f'De Iphone is het goedkoopst, de telefoon kost {iphone_prijs}Euro')
    print(f'Het advies is dus de Iphone te kopen. Deze is namelijk {samsung_prijs - iphone_prijs}Euro goedkoper')

if samsung_prijs == iphone_prijs:
    print(f'bijde telefoons zijn {iphone_prijs}Euro')
    print('het advies is dus om een telefoon naar keuze te namen')


#print(f'De {X} is het duurst, deze telefoon kost:{iphone_prijs}Euro')
#print(f'De {X} is het goedkoopst, deze telefoon kost:{samsung_prijs}Euro')
#print(f'Het advies is dus de {x} te kopen. Deze is namelijk {X} euro {goedkoper/duurder} dan de {X}')
