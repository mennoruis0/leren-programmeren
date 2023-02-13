from tkinter import Menubutton


name = input('wat is je naam?')                      #string
age = int(input('wat is je leeftijd?'))              


if age < 18:
    if name == 'menno':
        print('je krijgt een vrijkaart.')
    else:
        print(f'helaas {name} je mag nog niet naar binnen.')
        print('je krijgt een sticker')
elif age >= 18 and age < 21:
    print(f'Hallo {name} kom binnen, je mag nog geen sterke drank kopen.')
else:
     print(f'Hallo {name} je mag naar binnen en je mag ook sterke drank bestellen.')


