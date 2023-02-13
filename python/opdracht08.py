from fruitmand import fruitmand

watermeloen = { 
    'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
              }
fruitmand.append(watermeloen)
weight = 0
for fruit in fruitmand:
    weight = weight + fruit['weight']
print(f' totaal gewicht van de fruitmand is: {weight}')
    