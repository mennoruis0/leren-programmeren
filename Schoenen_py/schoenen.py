from schoenen_data import schoenen_lijst

# opdracht 1:
# Print alle schoenen van het merk Adidas

# for i in schoenen_lijst:
#     print(schoenen_lijst[0])
#     print(schoenen_lijst[1])
#     print(schoenen_lijst[2])
#     break

# filteren
# opdracht 2:
# Vraag een merk en print vervolgens alle modellen van het merk en de bijbehorende prijs.

# merk = input("van welk merk wilt u de schoenen zien? kies uit  Adidas/Nike/Puma/Gaastra: ")
#  for x in schoenen_lijst:
#    if merk in schoenen_lijst['merk']:
#          print(x['model'])
#          print(x['prijs'])
#          print(" ")
    

# opdracht 3:
# Vraag een merk en print vervolgens alle witte schoenen mits duurder dan €100.

merk = input("van welk merk wilt u de schoenen zien? kies uit  Adidas/Nike/Puma/Gaastra: ")
for x in schoenen_lijst:
    if merk in x['merk']:
        print(x['merk'])
        if x['kleur'] == 'wit':
            print(x['kleur'])    
            if x['prijs'] > 100:
                print(x['prijs'])


