grootste = 0
gedeeld = ""
kleinste = 1000


for x in range(10):
        getal = int(input("vul getallen in: "))
        if getal < kleinste:
                kleinste = getal        
        if getal > grootste:
                grootste = getal
        if getal %  3 == 0:
                gedeeld += (f' {getal }')
                


print (f"de grootste is {grootste}" )
print (f"de kleinste is {kleinste}" )
print (f"de aantal getallen door 3 gedeeld zijn {gedeeld}" )DW