land1 = input('welk land wil je in groep A: ')
land2 = input('welk land wil je in groep A: ')
land3 = input('welk land wil je in groep A: ')
goal1 = input(f'hoveel goals maakt {land1}: ')
goal2 = input(f'hoveel goals maakt {land2}: ')
if goal1 >= goal2: 
    print(f'Wedstrijd {land1}-{land2} eindigde in {goal1}-{goal2}')
    print(f'Overzicht Groep A')
    print(f'het doelsaldo is {goal1 - goal2}')
if goal2 >= goal1:
    print(f'Wedstrijd {land1}-{land2} eindigde in {goal1}-{goal2}')
    print(f'Overzicht Groep A')
    print(f'het doelsaldo is {goal2 - goal1} ')



print(f'Wedstrijd {land1}-{land2} eindigde in {goal1}-{goal2}')















# print('-----------------------------------------------------------------')
# print('|    LAND    |  DOELSALDO (gemaakt - tegen)  |    PUNTENTOTAAL   |')
# print('-----------------------------------------------------------------')
# print(f'|  {land1}   |                               |                  |')
# print(f'|  {land2}   |                                |                 |') 
# print(f'|  {land3}   |                               |                  |')    
# print('-----------------------------------------------------------------')
 
 
