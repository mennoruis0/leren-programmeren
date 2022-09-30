# de keuze is tussen Iphone 13 en Samsung Galaxy S22
# Jonas koopt de Iphone als deze maximaal 50 euro duurder is dan de Galaxy S22
#prijsverschil1 = samsung_prijs - iphone_prijs 
#prijsverschil2 = iphone_prijs - samsung_prijs  
#print(f'De {X} is het duurst, deze telefoon kost:{iphone_prijs}Euro')
#print(f'De {X} is het goedkoopst, deze telefoon kost:{samsung_prijs}Euro')
#print(f'Het advies is dus de {x} te kopen. Deze is namelijk {X} euro {goedkoper/duurder} dan de {X}')






iphone_prijs =  int(input('hoeveel kost de Iphone?'))
samsung_prijs = int(input('hoeveel kost de Samsung?'))


if iphone_prijs > samsung_prijs:
    print(f'De Iphone is het duurst, deze telefoon kost:{iphone_prijs}Euro')
    print(f'De Samsung is het goedkoopst, deze telefoon kost:{samsung_prijs}Euro')
    print(f'Het advies is dus de Samsung te kopen. Deze is namelijk {iphone_prijs - samsung_prijs}Euro goedkoper') 
    if iphone_prijs - samsung_prijs >= 50:
        print( 'de Iphone is maximaal 50 Euro duurder dan de Galaxy S22 dus het advies is om de Galaxy S22 te kopen')
        




if samsung_prijs > iphone_prijs:
    print(f'De Samsung is het duurst, deze telefoon kost {samsung_prijs}Euro')
    print(f'De Iphone is het goedkoopst, de telefoon kost {iphone_prijs}Euro')
    print(f'Het advies is dus de Iphone te kopen. Deze is namelijk {samsung_prijs - iphone_prijs}Euro goedkoper')


if samsung_prijs == iphone_prijs:
    print(f'bijde telefoons zijn {iphone_prijs}Euro')
    print('het advies is dus om een Iphone te kopen')

