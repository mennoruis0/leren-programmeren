


gender = input('bent u een man of vrouw? M/V ')
if gender == 'M':
    snor = input('Heeft u een snor? J/N ') 
    snor_lengte = int(input('Hoeveel CM is uw snor? '))                                   #>10
if gender == 'V':
    haar_kleur = input('Draagt u rood krulhaar? J/N ') 
    haar_lengte = int(input('Hoeveel CM is de lengte uw haar? '))                             #>20
hoed = input('Heeft u een hoge hoed? J/N ')
rijbewijs = input('Heeft u een geldig Vrachtwagen rijbewijs? J/N ')
diploma = input('Heeft u een MBO-4 diploma? J/N ')
lengte = int(input('Wat is uw lengte in CM? '))                                               #>150 and <220 
gewicht = int(input('hoeveel weegt u in KG? '))                                               #>90 and <120  
certificaat = input('Heeft u de Certificaat overleven met gevaarlijk personeel? J/N ')  
dieren_dressuur = int(input('Hoeveel jaar praktijkervaring met dieren-dressuur heeft u? '))   #>4
jongleren = int(input('Hoeveel jaar ervaring met jongleren heeft u? '))                       #>5
acrobatiek = int(input('Hoeveel jaar praktijkervaring met acrobatiek heeft u? '))             #>3


if certificaat == 'J' and  diploma == 'J' and  rijbewijs == 'J' and  hoed == 'J' and snor == 'J' or haar_kleur == 'J' and snor_lengte >=10 or haar_lengte >=20 and lengte >=150 <=220 and gewicht >=90 <=120 and dieren_dressuur >=4 and jongleren >=5 and acrobatiek >=3:
    print('u bent geschikt ')
else:
    print('u bent niet geschikt')
