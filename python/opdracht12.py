from fruitmand import fruitmand

kleuren = {'yellow' : 'geel','green' : 'groen','orange' : 'oranje','red' : 'rood','brown' : 'bruin', "pink" : "roze"}
name = []
gewicht = []
for fruit in fruitmand:
    name.append(fruit['name'])
    names = (max(name))
    gewicht.append(fruit['weight'])
kleuren = kleuren.get('pink')
print(f'De "{max(name)}" ({len(name)} letters) heeft een {kleuren} kleur en een gewicht van {gewicht[2] / 1000} kg.')


