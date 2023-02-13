from fruitmand import fruitmand
kleuren = []

for fruit in fruitmand:
    if fruit['color'] not in kleuren:
        kleuren.append(fruit['color'])
a = True
while a == True:
        kleur = input ('kies een kleur uit van: yellow, green, red, orange and  brown ')
        if kleur in kleuren:
            a = False
        else:
            print('die kleur ken ik niet ')
rond = 0
niet= 0
for fruit in fruitmand:
    kleuren = fruit['color']
    if kleuren == kleur:
        fruit['round']
        if fruit['round'] == True:
            rond += 1 
        elif fruit['round'] == False:
            niet += 1
print(f'het aantal ronde fruit is: {rond}')
print(f'het aantal niet ronde fruit is: {niet}')     

x = rond - niet
xx = niet - rond       

if rond > niet:
    print(f'Er zijn {x} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
elif rond < niet:
    print(f'Er zijn {xx} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
elif rond == niet:
    print(f'Er zijn {rond} ronde vruchten en {niet} niet ronde vruchten in de kleur {kleur}')
