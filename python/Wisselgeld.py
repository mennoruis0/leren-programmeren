# name of student: Menno Ruis
# number of student: 99072685
# purpose of program: wisselgeld berekenen
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # varanderd euros naar cents
paid = int(float(input('Paid amount: ')) * 100) # veranderd de betaalde aantal centen
change = paid - toPay # trek het met topay betaalde bedrag af

if change > 0: # als er nog terug betaald moet worden
  coinValue = 500 # de muntwaarde begint bij 500 cent
  
  while change > 0 and coinValue > 0: # controleert of er wisselgeld is en of er nog muntgeld ingeleverd moet worden
    nrCoins = change // coinValue #
    

    if nrCoins > 0: # als er munten zijn die moeten worden gegeven
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # drukt het in te geven bedrag af in munten
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # vraagt ​​hoeveel munten je hebt ingeleverd

      print(f"Given {nrCoinsReturned} of {coinValue / 100} euro")

      change -= nrCoinsReturned * coinValue # trekt het bedrag af met wisselgeld
    

# comment on code below: 
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # als er nog change is 
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')