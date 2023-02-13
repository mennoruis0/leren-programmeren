


a = input('wat is uw leeftijd: ')
try:
    b = float(a)
    print("uw leeftijd is geregistreerd")
except ValueError:
    print(f'{a} is geen getal, voer een getal in')

