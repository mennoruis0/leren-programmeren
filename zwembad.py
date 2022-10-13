from socketserver import UnixDatagramServer


lengte = int(input("hoe lang in meters: "))
breedte = int(input("hoe breed in meters: "))
diepte = float(input("hoe diep in meters: "))
afmeting = lengte * breedte * diepte
#print(afmeting)

uitgraven = 25 * afmeting
afvoeren = 32.50 * afmeting
totaal = uitgraven + afvoeren

print(f' offerte voor zwembad van {lengte} bij {breedte} bij {diepte} meter (inhoud: xx m3) ')
print(f' uitgraven:        € {uitgraven}')
print(f' afvoeren grond:   € {afvoeren}')
print(f' totaal:           € {totaal}')