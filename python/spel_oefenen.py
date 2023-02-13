


fysiek = input('Is het spel fysiek? ')
if fysiek == 'ja':
    bordspel = input('Is het een bordspel? ')
    if bordspel == 'nee':
        oranje = input('is het spel oranje? ')
        if oranje == 'ja':
            print('het is een kaartspel? ')
        elif oranje == 'nee':
            print('Sushi go')
    elif bordspel == 'ja':
        treintjes = input('heeft het spel treintjes? ')
        if treintjes == 'ja':
            print('Ticket to Ride')
        elif treintjes == 'nee':
            print('Catan')
elif fysiek == 'nee':
    sport = input('is het een sportspel? ')
    if sport == 'ja':
        print('Fifa 23')
    elif sport == 'nee':
        print('AOE 4')


    