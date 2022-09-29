#optellen,aftrekken, volgoorde k/ g
getal1 = int(input('voer getal 1 in:'))
getal2 = int(input('voer getal 2 in:'))
actie = input('welke actie wenst u, kies: (o)ptellen, (a)ftrekken, K(volgorde), g(volgorde) v(ermedigvuldigen), d(elen)')

antwoord = 0
if actie == 'a':
    zin = 'aftrekken:  '
    andwoord = getal1 - getal2
elif actie == 'o':
    zin = 'optellen'
    andwoord = getal1 + getal2
elif actie == 'v':
    zin = 'vermeningvuldigen'
    andwoord = getal1 * getal2
elif actie == 'd':
    if getal2 == 0:
        zin = 'je deelt door 0'
        actie = 'x'
    else:
        zin = 'delen door'
    andwoord = getal1 / getal2
elif actie == 'k':
    if getal1 > getal2:
        zin = 'volgorde(k):' + str(getal2) + ',  ' + str(getal1)
    else:
        zin = 'volgorde(k):' + str(getal1) + ',  ' + str(getal2)
    
elif actie == 'g':
    if getal1 > getal2:
        zin = 'volgorde(k):' + str(getal1) + ',  ' + str(getal2)
    else:
        zin = 'volgorde(k):' + str(getal2) + ',  ' + str(getal1)
else:
    zin = 'tik maar iets nuttigs in'

print(zin)
if actie !='k' or actie != 'o' or actie == 'v' or actie == 'd':
    print(andwoord)