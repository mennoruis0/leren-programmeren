print("")
print("Welkom bij de game: Het Bos")
print("")
print("Je zit in een vliegtuig naar het buitenland voor je werk.")
print("Het vliegtuig stort neer op een eilland je bent de enigste overlever in het vliegtuig.")
print("")
klimmen = input("je ziet een hoge boom wil je er in klimmen?  ja/nee: ")
print("")
if klimmen == 'ja':
        print("")
        print("Het uitzicht is erg mooi, je ziet een grote berg maar je ziet ook ergens rook tussen de bomen komen")
        print("")

elif klimmen == "nee":
    print("")
    print("je kijkt om je heen em je ziet veel kleurrijke bessen in de struiken")
    print("")

bessen = input("Je hebt honger dus je hebt al wat besjes gevonden welke ga je eten?  wolfskers/rozenbottel: ")
if bessen == "wolfskers":
    print("")
    print("Helaas, het waren giftige bessen")
    print("Je bent nu dood")
    print("")
    print("GAMEOVER")
    exit()

elif bessen == "rozenbottel":
    print("")
    print("De besjes waren erg lekker maar je voelt je nu wel moe")

slapen = input("Wil je gaan slapen?  ja/nee: ")
if slapen == 'ja':
    print("")
    print("Je wordt wakker met een groep canibalen om je heen. ")

elif slapen == "nee":
    print("")
    print("je wordt aangevallen door canibalen")
    print("")

canibalen = input("Kies je ervoor om te vechten om met ze te praten?  vechten/praten: ")
print("")
if canibalen == "praten":
    print("")
    print("ze verstaan je niet en je maar ze wijzen richting het bos, je besluit om mee te lopen")
    print("je loopt mee naar  hun kamp, maar je wordt helverwege knockout geslagen")

elif canibalen == "vechten":
    print("")
    print("Ze overmachtigen je en je wordt knockout geslagen.")
print("je word wakker in een kooi je ziet dat de kooi niet dicht is maar en je ziet ook een vrouw in de kooi")


vrouw = input("neem je de onbekende vrouw ook mee tijdens je ontsnappig?  ja/nee: ")
print("")
if vrouw == "ja":
    print("")
    print("Je rent weg met de onbekende vrouw naar het strand.")
    print("Je besluit S.O.S in het zand te tekenen en vervolgends te slapen.")
    print("Je word midden in de nacht vermood door de vrouw want het bleek een verbannen cannibaal te zijn.")
    print("")
    print("EINDE")
    raise NameError("Game over")

elif vrouw == "nee":
    print("")
    print("je rent weg uit het kamp naar een openplek")

locatie = input("ga je hier een schuilplaats bouwen of ga je naar het strand?  bouwen/strand: ")
if locatie == "strand":
    print("")
    print("je bent gaan slapen en je ziet de volgende dag een vliegtuig")
    print("")
    
    vuur = input("wil je de aandacht trekken met vuur?  ja/nee: ")
    print("")
    if vuur == "nee":
        print("")
        print("Je blijft op het strand en het voedsel raak langzaam op.")
        print("Je gaat langzaam dood van de honger.")
        print("EINDE")
        raise NameError("Game over")
    
    elif vuur == "ja":
        print("")
        print("Het vliegtuig ziet het vuur maar de canibalen eerder")
        print("je wordt levend opgegeten")
        print("EINDE")
        raise NameError("Game over")

elif locatie == "bouwen":
    print("")
    print("Je besluit een schuilplaats en je maakt van stenen de letters S.O.S op de grond.")
    print("Een vliegtuig spot het en een dag later wordt je gered door een helicopter.")
    print("")
    print(" GOOD ENDING")
22