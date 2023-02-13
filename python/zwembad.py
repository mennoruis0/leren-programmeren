from socketserver import UnixDatagramServer


lengte = int(input("hoe lang in meters: "))
breedte = int(input("hoe breed in meters: "))
diepte = float(input("hoe diep in meters: "))
afmeting = lengte * breedte * diepte
#print(afmeting)

uitgraven = 25 * afmeting
afvoeren = 32.50 * afmeting
voorrijkosten = 1
totaal = uitgraven + afvoeren + voorrijkosten

print(f' Offerte voor zwembad van {lengte} bij {breedte} bij {diepte} meter (inhoud: xx m3) ')
print(f' Uitgraven:        € {uitgraven}')
print(f' Afvoeren grond:   € {afvoeren}')
print(f' Voorrijkosten:    € {voorrijkosten}')
print(f' Totaal:           € {totaal}')