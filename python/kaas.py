
from xml.dom.expatbuilder import ElementInfo


duur = input('Is de kaas belachelijk duur?')
if duur == "ja":
    duur= input('zit er een korst om?')
    if duur == 'ja':
        print('De kaas doe jij bedoelt is de emmenthaler.')
    else:
        print('De kaas doe jij bedoelt is de Gouda.')
elif duur == "nee":
    print('De kaas doe jij bedoelt is de leerdammer.')
else:
    print('vul ja of nee in')

