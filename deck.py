from random import randint, random,shuffle
sort = ['harten', 'klaveren', 'schoppen', 'ruiten']
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'boer', 'vrouw', 'heer', 'aas']
deck = []

for x in range(4):
    for X in range(13):
        deck.append(sort[x] + '  ' + str(cards[X]))
for z in range(2):
    deck.append('joker')
print(" ")

shuffle(deck)
print(" ")

print(deck)
for c in range(1, 8):
    print(f'kaart {c}: {deck[0]}')
    deck.pop(0)
print(" ")

print(deck)