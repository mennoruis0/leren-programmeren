#bedrag_string = input('voer bedrag in :')
#bedrag = float(bedrag_string)

bedrag = int(input('voer bedrag in:'))

aantal_twee_euro = bedrag // 200
print(f"aantal 2 euro: {aantal_twee_euro}")
restant = bedrag - 200 * aantal_twee_euro

aantal_een_euro = bedrag // 100
print(f"aantal 1 euro: {aantal_een_euro}")
restant = restant - 100 * aantal_een_euro

aantal_50_cent = bedrag // 50
print(f"aantal 50 cent: {aantal_50_cent}")
restant = restant - 50 * aantal_50_cent

print(restant)










#restant = bedrag - aantal_twee_euro * 200
#aantal_een_euro = restant // 100
#print(f'aantal 1 euro: {aantal_een_euro}')
#aantal_50_cent = restant // 50
#print(f'aantal 50 cent: {aantal_50_cent}')
#print(restant)