boodschappen = {}
meer_boodschappen = ""
while meer_boodschappen != "J":
    boodschap = str(input("Wat wilt u kopen?: "))
    aantal_boodschap = int(input("Hoeveel?: "))
    if boodschap in boodschappen:
        boodschappen[boodschap] += aantal_boodschap
    else:
        boodschappen[boodschap] = aantal_boodschap

    meer_boodschappen = str(input("Klaar?: J/N "))
print(boodschappen)


        