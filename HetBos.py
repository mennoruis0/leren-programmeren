from asyncio import new_event_loop


print("Welkom bij de game: Het Bos")
print("Je zit in een vliegtuig naar het buitenland voor je werk.")
print("Het vliegtuig stort neer op een eilland je bent de enigste overlever in het vliegtuig.")
klimmen = input("je ziet een hoge boom wil je er in klimmen?  ja/nee: ")
if klimmen == 'ja':
        print("Het uitzicht is erg mooi je ziet een grote berg maar je ziet ook ergens rook tussen de bomen komen")
elif klimmen == "nee":
    print("Je ziet veel kleurrijke bessen in de struiken")
bessen = input("Je hebt honger dus je hebt al wat besjes gevonden welke ga je eten?  wolfskers/rozenbottel: ")
if bessen == "wolfskers":
    print("Helaas, het waren giftige bessen")
    print("Je bent nu dood")
    print("EINDE")
elif bessen == "rozenbottel":
    print("De besjes waren erg lekker maar je voelt je nu wel moe")
slapen = input("Wil je gaan slapen?  ja/nee: ")
if slapen == 'ja':
    print("Je wordt wakker met een groep canibalen om je heen. ")
elif slapen == "nee":
    print("je wordt aangevallen door canibalen")
canibalen = input("Kies je ervoor om te vechten om met ze te praten?  vechten/praten: ")
if canibalen == "praten":
    print("ze verstaan je niet en je maar ze wijzen richting het bos, je besluit om mee te lopen")
    print("je loopt mee naar  hun kamp, maar je wordt helverwege knockout geslagen")
if canibalen == "vechten":
    print("Ze overmachtigen je en je wordt knockout geslagen.")
print("je word wakker in een kooi je ziet dat de kooi niet dicht is maar en je ziet ook een vrouw in de kooi")