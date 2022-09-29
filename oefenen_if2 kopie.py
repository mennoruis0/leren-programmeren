# Vraag: console of pc
# Bereken prijs pc: 45 euro
# Console: 55 Euro
# print: De game kost je dan:
# vraag of iemand member is


#vraag = input('waar speel je op')
#if vraag == 'console':
    #print('de game kost 55 euro op je console naar keuze')
    #if member = input('ben je een member?')
    #member = input('ben je een member?')
    #if member == 'ja':
        #print('door je membership kost het nu maar 40 euro')
        
        #if vraag == 'pc':
    #print('de game kost 45 euro op je pc')

#if platform == 'console' and member == 'ja':
    #print(F'u krijgt {MEMBER_KORTING} korting van de game prijs af')
    #prijs = CONSOLE_PRIJS - MEMBER_KORTING

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




