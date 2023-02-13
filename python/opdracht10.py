from fruitmand import fruitmand

dict = {}
for fruit in (fruitmand):
    dict.update({
        fruit.get("weight"):
        fruit.get("name")
                })
print(sorted(dict.items(), reverse=True))
