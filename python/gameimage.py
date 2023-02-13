getal = 'appeltaart'
while true:
    try:
        getal = int(input('hoeveel small pizza wilt u?'))
        break
    except:
        print('vul een getal in')


print(getal)