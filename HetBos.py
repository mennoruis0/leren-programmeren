from asyncio import new_event_loop


print("Welkom bij de game: Het Bos")
print("Je zit in een vliegtuig naar het buitenland voor je werk.")
print("Het vliegtuig stort neer op een eilland je bent de enigste overlever in het vliegtuig.")
klimmen = input("je ziet een hoge boom wil je er in klimmen? ja/nee: ")
if klimmen == 'ja':
        print("Het uitzicht is erg mooi je ziet een grote berg maar je ziet ook ergens rook tussen de bomen komen")
elif klimmen == "nee":
    print("Je ziet veel kleurrijke bessen in de struiken")
bessen = input("Je hebt honger dus je hebt al wat besjes gevonden welke ga je eten: wolfskers/rozenbottel: ")
if bessen == "wolfskers":
    print("Helaas, het waren giftige bessen")
    print("je bent nu dood")
    print("EINDE")
elif bessen == "rozenbottel":
    print("De besjes waren erg lekker maar je voelt je nu wel moe")