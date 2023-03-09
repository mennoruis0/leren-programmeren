SPEL_PRIJS = 24.95 
KORTING = 0.4
aantal = int(input("hoeveel spellen wil je inkopen?: "))

def get_inkoop_totaal(aantal):
    inkoopprijs_spel = SPEL_PRIJS * (1 - KORTING)
    totaal_inkoop = inkoopprijs_spel * aantal

    print("inkoopprijs spellen: " + str(totaal_inkoop))
    print(inkoopprijs_spel)

    verzendkosten = 1 + ((aantal - 1) * 0,25)
    return(verzendkosten + totaal_inkoop)