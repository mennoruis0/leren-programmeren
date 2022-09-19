#Menno Ruis,Pizza calculator


small_prijs = 6
medium_prijs = 8
large_prijs = 12


pizza_small = int(input("hoveel small pizza's wilt u?"))
pizza_medium = int(input("hoveel medium pizza's wilt u?"))
pizza_large = int(input("hoveel large pizza's wilt u?"))


totaalprijs_S= small_prijs*pizza_small
totaalprijs_M= medium_prijs*pizza_medium
totaalprijs_L= large_prijs*pizza_large

totaalprijs = totaalprijs_S+totaalprijs_M+totaalprijs_L


print(f'|   small pizza      :  {totaalprijs_S}')  
print(f'|   medium pizza     :  {totaalprijs_M}') 
print(f'|   pizza large      :  {totaalprijs_L}') 
print(f'|   totaal prijs     :  {totaalprijs}')