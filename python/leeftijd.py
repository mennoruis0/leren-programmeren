# vraagt een getal aan de gebruiker en geeft deze terug
def vraag_een_getal(vraag: str) -> int: # betekent defineer aan
    while True:
        try:
            getal = int(input(vraag))
            break
        except ValueError:
            print('je moet wel een getal invullen')
            continue
    return getal

leeftijd = vraag_een_getal('voer een getal in')
geboorte_jaar = vraag_een_getal('voer een getal in')
geboorte_maand = vraag_een_getal('voer een getal in')
geboorte_dag = vraag_een_getal('voer een getal in')

print(leeftijd)

