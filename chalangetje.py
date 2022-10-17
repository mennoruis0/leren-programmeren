zin = input('voer een zin in')
zin2 = ""
woord = ""

for c in zin:

    if c == " ":
        zin2 += woord + " " + woord + " "
        woord = " "
    else:
        woord += c

print(zin2)